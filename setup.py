from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Generic HR utility.',
    long_description=readme,
    author='Felix Brilej',
    author_email='felix.brilej@googlemail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main'
        ]
    }
)