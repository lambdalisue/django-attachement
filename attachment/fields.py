#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""
Model field for Attachment


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
from django.contrib.contenttypes import generic
from attachment.models import Attachment

class AttachmentField(generic.GenericRelation):
    """Reverse generic relation field of Attachment for Model"""
    def __init__(self, *args, **kwargs):
        # override 'to' kwargs
        kwargs['to'] = Attachment
        if len(args) > 0:
            kwargs['verbose_name'] = args[0]
            args = args[1:]
        super(AttachmentField, self).__init__(*args, **kwargs)

# Add south
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r'^attachment\.fields\.AttachmentField'])
except ImportError:
    pass
