from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers==4.12.0',
        'torch',
        'soundfile',
        'streamlit',
        'datasets',
    ],
)
