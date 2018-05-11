from setuptools import setup, find_packages

setup (
       name='GenerateUserName',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Andrzej Grenczuk',
       author_email='andrzej.grenczuk@gmail.com',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Simple Python script to generate user name (7 digits) with password lenght 14 character',

       # could also include long_description, download_url, classifiers, etc.

  
       )