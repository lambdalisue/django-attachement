# vim: set fileencoding=utf-8 :
"""
Urls of


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
from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from piston.doc import documentation_view

from attachment.api.handlers import AttachmentHandler

res = Resource(AttachmentHandler)

urlpatterns = patterns('',
    #url(r'^attach/$', res, {'emitter_format': 'fileupload_json'}, name='attachment-api-attach'),
    url(r'^(?P<content_type>\d+)/(?P<object_id>\d+)/$', res, name="attachment-api-attach"),
    url(r'^attach/$', res, name="attachment-api-attach"),
    url(r'^delete/(?P<pk>\d+)/$', res, name='attachment-api-delete'),
    url(r'^doc/$', documentation_view),
)
