from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = r.read():

setup(
        name='pgbackup',
        version='0.1.0',
        author='Charles Moore',
        author_email='chuckm224@gmail.com'
        description='A utility for backing up PostgreSQL databases',
        long_description=long_description,long_description_content_type='text/markdown',
        url='https://github.com/ChuckM2196/pgbackup',
        packages=find_packages('src')
        )
