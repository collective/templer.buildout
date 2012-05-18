from setuptools import setup, find_packages
import os

version = '1.0b1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

tests_require = [
    'unittest2',
    'Cheetah',
    'PasteScript',
    'templer.core'],

setup(name='templer.buildout',
      version=version,
      description="Templer system extensions for buildouts and buildout recipes",
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 3.2",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        ],
      keywords='',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='https://github.com/collective/templer.buildout',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      [paste.paster_create_template]
      recipe = templer.buildout:Recipe
      basic_buildout = templer.buildout:BasicBuildout

      [templer.templer_structure]
      bootstrap = templer.buildout.structures:BootstrapStructure
      """,
      )
