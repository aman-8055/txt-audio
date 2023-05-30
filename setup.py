from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.89.0',
        'torch==1.9.0',
        'soundfile==0.10.3.post1',
        'transformers==4.10.3',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio=app:main',
        ],
    },
)
