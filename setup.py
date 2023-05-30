from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.85.1',
        'torch==1.9.0',
        'soundfile==0.10.3.post1',
        'transformers==4.10.3',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio=app:main',
        ],
    },
    setup_requires=[
        'numpy',
        'Cython',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
)
