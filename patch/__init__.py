#!/usr/bin/env python
# vim: sw=4 ts=4 et si:
#
"""patch class"""

import os
from Config import Config

__version__ = '1.2'

__all__ = [
	"Patch",
	"PatchOps",
]

class PatchException(Exception):
    pass

config = Config()
