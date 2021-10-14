"""Sets up the package"""


from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='django-auth-template',
    version='0.1.0',
    description='Moon project',
    long_description=README,
    author='<author>',
    author_email='<email>',
    url='https://git.com',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
