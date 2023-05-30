from setuptools import setup, find_packages

setup(
    name='txt-audio',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'fairseq',
        'huggingface_hub',
        'IPython',
        'tensorboardX',
    ],
    entry_points={
        'console_scripts': [
            'txt-audio = app:main',
        ],
    },
)
