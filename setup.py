#!/usr/bin/env python
from setuptools import setup

req = ['numpy','scipy','matplotlib','seaborn','python-dateutil','pytz',
       'sciencedates']

#%% install
setup(name='wspr_spectrum_plot',
      packages=['wspr_spectrum_plot'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/wspr_spectrum_plot',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python :: 3',
      ],
      install_requires=req,
	  )
