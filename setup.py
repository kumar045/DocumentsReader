from setuptools import setup, find_packages

setup(
    name='DocumentsReader',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'WeasyPrint==62.1',
        'Pillow==9.4.0',
        'python-docx==1.1.2',
        'python-pptx==0.6.23',
        'openpyxl==3.1.2',
        'pdf2image==1.17.0',
        'Pillow==10.1.0',
        'torch==2.1.2',
        'torchvision==0.16.2',
        'transformers==4.40.0',
        'sentencepiece==0.1.99',
        'accelerate==0.30.1',
        'bitsandbytes==0.43.1'
    ],
    url='',
    license='MIT',
    author='Shivam Kumar',
    author_email='kumarshivam066@gmail.com',
    description='A package to read and process documents to extract data in json format',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
