from setuptools import setup, find_packages
import sys, os

version = '0.2'

readme = open('README.txt').read()

setup(name='hyperbmp',
      version=version,
      description="display and edit hyperbitmaps",
      long_description=readme,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "svenweb",
        ],
      entry_points="""
[paste.app_factory]
main = hyperbmp.wsgi:app_factory
      """,
      )
