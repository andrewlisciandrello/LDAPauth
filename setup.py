#!/usr/bin/env python

from distutils.core import setup

setup(name='LDAPauth',
      version='1.0.1',
      description='LDAP Authentication - Returns True if user is memeber of "devnull" group and False if not',
      author='Andrew Lisciandrello',
      author_email='andrew.lisciandrello@rackspace.com',
      url='https://github.rackspace.com/andr5697/LDAP-auth',
      py_modules = ['LDAPauth'],
      install_requires = ['python-ldap']
     )
