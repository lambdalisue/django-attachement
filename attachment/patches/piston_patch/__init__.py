# vim: set fileencoding=utf-8 :
"""
Monkey patch for django-piston 0.2.3
This patch must be called with ``INSTALLED_APPS``

AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
License:
    The MIT License (MIT)

    Copyright (c) 2012 Alisue allright reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.

"""
from __future__ import with_statement

# just in case, the critical patch hasn't patched
from criticals import *

# support GenericForeignKey
from django.contrib.contenttypes.generic import GenericForeignKey
GenericForeignKey.serialize = None

# support django 1.4
import django
if django.get_version().startswith('1.4'):
    from django.http import HttpResponse
    def _get__is_string(self):
        return self.__is_string
    def _set__is_string(self, value):
        self.__is_string = value
        self._base_content_is_iter = not value
    # to pass unittest, the string value is a matter.
    HttpResponse.__is_string = 'Expected response content to be a string'
    HttpResponse._is_string = property(_get__is_string, _set__is_string)
    HttpResponse._base_content_is_iter = True
    
