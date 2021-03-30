### #!/usr/bin/env python
# encoding: utf-8
"""
Python bindings of webrtc audio processing
"""

from glob import glob
import platform
import sys
from setuptools import setup, Extension, find_packages


with open('README.md') as f:
    long_description = f.read()

include_dirs = ['src', 'pesq']

ap_sources = []
ap_dir_prefix = 'pesq/'
for i in range(8):
    ap_sources += glob(ap_dir_prefix + '*.c*')
    ap_dir_prefix += '*/'

print(ap_sources)

sources = (
    ap_sources +
    ['src\\pypesq.c', 'src\\pypesq.i']
)

setup(
    name='pypesq',
    version='0.1.0',
    description='Python bindings of PESQ(P.862 and P.862.2)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='James Park',
    author_email='youngjamespark@gmail.com',
    url='https://github.com/youngjamespark/python-pypesq',
    download_url='https://github.com/youngjamespark/python-pypesq',
    packages=['pypesq'],
    ext_modules=[
        Extension(
            name='pypesq._pypesq',
            sources=sources,
            include_dirs=include_dirs,
        )
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: C'
    ],
    license='BSD',
    keywords=['pesq', 'P.862', 'P.862.2', 'PESQ'],
    package_dir={
        'pypesq': 'src'
    }
)
