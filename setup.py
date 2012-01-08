#!/usr/bin/env python

from distutils.core import setup

setup(name='todo',
      version='1.0',
      description='todolist manager',
      author='Nicholas Harteau',
      author_email='n@hep.cat',
      url='http://github.com/nrh/todo',
      packages=['distutils','distutils.command'],
      scripts=['scripts/todo'],
     )

