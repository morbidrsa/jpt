#!/usr/bin/env python
# vim: sw=4 ts=4 et si:
"""
Setup file for installation
"""

import os
import sys
import shutil
import site
from distutils.core import setup, Command


class CleanCommand(Command):
    description = "custom clean command that forcefully removes dist/build directories"
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        print "removing './build', and everything under it"
        os.system('rm -rf ./build')
        print "removing './scripts', and everything under it"
        os.system('rm -rf ./scripts')

shutil.rmtree("scripts", ignore_errors=True)
os.makedirs("scripts")
shutil.copyfile("exportpatch.py", "scripts/exportpatch")
shutil.copyfile("fixpatch.py", "scripts/fixpatch")

if os.access("/etc", os.W_OK):
    path = "/etc"
else:
    path = "etc"

setup(# distribution meta-data
        cmdclass={
            'clean': CleanCommand
            },
        author="Jeff Mahoney",
        author_email="jeffm@suse.com",
        name="patchopts",
        packages=["patch"],
        scripts=["scripts/exportpatch", "scripts/fixpatch"],
        version="2.0",
	data_files=[(path, ['patch.cfg'])])

if path[0] != '/':
    path = "%s/%s" % (site.USER_BASE, path)

print "Config file installed at %s/patch.cfg" % (path)
