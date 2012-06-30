from setuptools import setup


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
  keywords="python notifout",
  description='Python API for Notifout.com',
  long_description=open(os.path.join(here, 'README.rst')).read().decode('utf-8')    
)