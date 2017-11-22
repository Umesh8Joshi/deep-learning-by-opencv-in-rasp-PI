"""
	Setup file for project. All the dependencies of python libraries are imported here. with shell script installing
	all the dependencies by using pip (python package installer)
"""
#Author : Umesh8Joshi

"""
	python version : 3.6.3
	pip version	   : 9.0.1
	License		   : MIT (open source)
"""
#!/usr/bin/python3.6

from distutils.core import setup
setup(name='',
	  version='1.0',
	  description='Automatic Dust sensing machine',
	  author='',
	  author_email='',
	  packages=['opencv','time','numpy','imutils','picamera',
	  			'grovepi'])

package_dir = {'': 'lib'}
