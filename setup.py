from setuptools import setup, find_packages

setup(
    name='streamlit_tts_demo',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fairseq==0.10.2',
        'streamlit==0.89.0',
        'ipython==7.29.0'
    ],
    entry_points={
        'console_scripts': [
            'streamlit_tts_demo = app:main'
        ]
    },
)
