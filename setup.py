from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='falk',
      version=0.1,
      description="python course test",
      long_description="""\
python course test""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python',
      author='Elin',
      author_email='elin.falk_sorqvist@igp.uu.se',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts = ['scripts/getting_data.py'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
