from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.85.1',
        'torch==1.9.0',
        'transformers==4.10.3',
        'pydub==0.25.1',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio=app:main',
        ],
    },
)
