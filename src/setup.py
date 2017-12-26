from setuptools import setup, find_packages

setup(
    name = 'mhzXX',
    version = '0.1',
    author = 'Tomas \'Jethro\' Pokorny',
    author_email = 'xtompokAT_MARKgmailDOTcom',
    packages = find_packages(),
    license = 'LICENSE.txt',
    description = 'Reads CO2 concetration from a MH-Zxx sensor.',
    long_description = open('README.txt').read(),
    keywords = "CO2 concentration MH-Z16",
    url = "",
    install_requires = "pyserial>=3.4",
)
