#
# (C) Copyright 2014 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source software distributed according to the terms in
# LICENSE.txt
#
from __future__ import absolute_import

__all__ = ['_kernel32', '_advapi32', '_winerrors', '_common']

try:
    from win32ctypes.core.cffi import _advapi32, _common, _kernel32
except ImportError:
    from win32ctypes.core.ctypes import _advapi32, _common, _kernel32

from win32ctypes.core import _winerrors
