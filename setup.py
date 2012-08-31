from setuptools import setup, find_packages



setup(name = 'mediafixtures',
      version = '0.1',
      description = 'Handles media fixtures like django does it for db content',
      author = 'Leander Hanwald',
      author_email = 'shockflash@web.de',

      url = 'https://github.com/shockflash/mediafixtures/',
      download_url = 'https://github.com/shockflash/mediafixtures/tarball/master',

      packages = find_packages(),

      license = 'BSD',

      classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )