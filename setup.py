from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.87.0',
        'fairseq==0.10.2',
        'huggingface_hub==0.0.12',
        'IPython==7.33.0',
        'tensorboardX',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio = app:main',
        ],
    },
)
