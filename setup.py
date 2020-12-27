from setuptools import find_packages, setup
setup(
    name='nelxte',
    packages=find_packages(include=['mypythonlib']),
    version='1.0',
    download_url = 'https://github.com/amay428/nelxte_lib/archive/1.0.tar.gz',
    description='Nelxte is a fast and open source python library for checking password strength. It comes with features such as, "Check for common passwords", "Special character checker", etc. All this can be done in just 2 lines of code and only takes 0.098 seconds(Most cases).',
    author='Amay Agarwal',
    license='MIT',
)