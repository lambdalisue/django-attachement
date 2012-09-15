# vim: set fileencoding=utf-8 :
"""
Form decorator to enable attachment feature


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
from django import forms
from attachment.utils import bind_attachments

def attachmentable(form_class):
    """A form decorator to enable attachment feature"""
    # store original ``__init__()`` method
    original__init__method = form_class.__init__
    # store original ``save()`` method
    original_save_method = form_class.save

    def __init__(self, *args, **kwargs):
        # call original __init__ method
        original__init__method(self, *args, **kwargs)
        # add required field
        self.fields['attachment_pks'] = \
                forms.CharField()
                #forms.CharField(widget=forms.HiddenInput())

    def save(self, commit=True):
        # force saving
        instance = original_save_method(self, commit=True)

        # bind attachments to the instance
        bind_attachments(self, instance)

        return instance

    # overwrite methods
    form_class.__init__ = __init__
    form_class.save = save

    return form_class
