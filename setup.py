from setuptools import setup, find_packages

setup(
    name='words2number',
    version='1.0.0',
    author='Benjamin Bonneton',
    author_email='contact@benjamin-bonneton.com',
    description='Convert sentences containing numbers written in words into numeric values.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/benjamin-bonneton/words2number',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
