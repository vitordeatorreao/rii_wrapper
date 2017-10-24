"""A simple setup for the wrapper"""

from setuptools import setup

setup(name='wrapper',
      version='0.1',
      description='A simple wrapper for car craigslist in portuguese',
      url='http://github.com/vitordeatorreao/wrapper',
      author='Vitor Torreao',
      author_email='vat@cin.ufpe.br',
      license='MIT',
      packages=['wrapper'],
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[
          'unidecode',
      ],
      zip_safe=False)
