from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'torch',
        'soundfile',
        'streamlit',
        'datasets',
    ],
)
