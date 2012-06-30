from distutils.extension import Extension
from setuptools import setup, Extension
from Cython.Distutils import build_ext

import os.path
here = os.path.dirname(os.path.abspath(__file__))


setup(
  name = 'notifout',
  version = '1.0',
  author = 'Sergey Kirilov',
  author_email = 'sergey.kirillov@gmail.com',
  url='https://github.com/pistolero/notifout-python', 
  install_requires=['simplejson'],
  license="Apache License 2.0",   
  keywords="sass scss libsass",  
  description='Python bindings for libsass',
  long_description=open(os.path.join(here, 'README.rst')).read().decode('utf-8')    
)