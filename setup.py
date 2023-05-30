from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'torch',
        'transformers',
        'pydub',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio=app:main',
        ],
    },
)
