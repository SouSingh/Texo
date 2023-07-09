from setuptools import setup, find_packages
import codecs
import os


with open("README.md","r") as fh:
    long_desc = fh.read()


setup(
    name='Texo',
    version='0.0.4',
    description='Sentiment Analysis Multiple language and for all products',
    author='Sourabh singh',
    author_email='Sourabh52.singh@gmail.com',
    long_description=long_desc,
    long_description_content_type = "text/markdown",
    package_dir={'':'src'},
    url='https://github.com/Sourabh20022002/Texo',
    download_url = 'https://github.com/Sourabh20022002/Texo/archive/refs/tags/python.tar.gz',    
    packages=['Texo'],
    install_requires=[
        'transformers',
        'translate',
    ],
    keywords=['python', 'Sentiment', 'NLP', 'Tokenizer', 'Text-Analyzer', 'sockets','torch', 'PIL', 'torchvision'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
