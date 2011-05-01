import os
import sys
import shutil
from shutil import Error, WindowsError, copy2, copystat

from django.conf import settings
from django.utils.importlib import import_module
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    """
    Command that copies the media-fixtures from "fixtures/media/" form every app
    to the media/ directory of the project. 
    Usefull alongside initial_data.* fixtures, so that you can have DB-fixtures
    and matching media-file fixtures. 
    """

    help = "TODO"

    def handle(self, *args, **options):
        self.apps = []

        print "\nSearch for apps with media fixtures..."

        apps = settings.INSTALLED_APPS
        for app in apps:
            mod = import_module(app)
            mod_path = os.path.dirname(mod.__file__)
            location = os.path.join(mod_path, 'fixtures', 'media')

            if os.path.isdir(location):
                print "  - " + app
                copytree(location, settings.MEDIA_ROOT)

        print ""


def copytree(src, dst, symlinks = False, ignore = None):
    """
    Copied from Python 2.6 to add the following line: 
    
      if not os.path.isdir(dst):
    
    this way, we can copy/overwrite existing directories. Very important here
    
    If anyone knows a better way, say it
    """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.isdir(dst):
        os.makedirs(dst)

    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error, err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except OSError, why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error, errors






