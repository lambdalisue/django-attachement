#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""
short module explanation


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
from django.contrib.contenttypes.models import ContentType
from attachment.models import Attachment

def get_filename_pattern(pattern, filename):
    """get filename with pattern. the pattern can be string or function."""
    if callable(pattern):
        filename = pattern(filename)
    else:
        filename = pattern % {'filename': filename}
    return filename

def bind_attachments(form, instance):
    """bind attachments to the instance"""
    # set pks
    ct = ContentType.objects.get_for_model(instance)
    attachment_pks = form.cleaned_data['attachment_pks']
    attachment_pks = attachment_pks.split(',')
    attachment_pks = filter(lambda x: x.strip(), attachment_pks)
    attachment_pks = filter(bool, attachment_pks)
    qs = Attachment.objects.filter(pk__in=attachment_pks)
    for attachment in qs.iterator():
        attachment.content_type = ct
        attachment.object_id = instance.pk
        attachment.save()

