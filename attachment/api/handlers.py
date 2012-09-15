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
from django.conf import settings
from django import forms
from piston.utils import rc
from piston.utils import throttle
from piston.handler import BaseHandler

from attachment.models import Attachment


class AttachmentHandler(BaseHandler):
    model = Attachment
    allowed_method = ('GET', 'POST', 'DELETE')
    fields = ('pk', 'file', 'created_at')

    def read(self, request):
        qs = Attachment.objects.all()
        response = [instance.get_api_dict() for instance in qs.iterator()]
        return response

    #@throttle(100, 10*60)
    def create(self, request):
        attachments = []
        for f in request.FILES.getlist('files[]'):
            attachment = Attachment.objects.create(file=f)
            attachment = attachment.get_api_dict()
            attachments.append(attachment)
        return attachments

    @throttle(100, 10*60)
    def delete(self, request, pk):
        Attachment.objects.filter(pk=int(pk)).delete()
        return rc.DELETED
    
