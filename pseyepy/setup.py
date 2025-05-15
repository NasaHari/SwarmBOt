from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import os, sys

# Check OS and set up libusb paths
if sys.platform in ('darwin', 'linux', 'linux2'):
    libusb_incl = []
    libusb_libpath = ''
    libs = ['usb-1.0']
else:
    libusb_incl = [os.path.join('pseyepy', 'ext', 'win', 'include', 'libusb-1.0')]
    libusb_libpath = 'pseyepy/ext/win/lib'
    libs = ['libusb-1.0']

# Set up compilation parameters
os.environ["CC"] = "g++"
srcs = ['pseyepy/src/ps3eye.cpp', 'pseyepy/src/ps3eye_capi.cpp', 'pseyepy/cameras.pyx']
extensions = [Extension('pseyepy.cameras',
                        srcs,
                        language='c++',
                        extra_compile_args=['-std=c++11'],
                        extra_link_args=['-std=c++11'],
                        include_dirs=['pseyepy/src'] + libusb_incl,
                        library_dirs=[libusb_libpath],
                        libraries=libs,
                    )]

# Run setup
setup(name='pseyepy',
      version='0.0',
      description='pseyepy camera package',
      author='Ben Deverett',
      author_email='deverett@princeton.edu',
      url='https://github.com/bensondaled/pseyepy',
      packages=['pseyepy'],
      package_data={'pseyepy': ['cameras.pyx']},
      ext_modules=cythonize(extensions))
