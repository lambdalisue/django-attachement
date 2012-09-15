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
import os
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import default_storage
from attachment.utils import get_filename_pattern

try:
    from PIL import Image
except ImportError:
    import Image

class ThumbnailBase(object):

    def get_storage(self):
        """get django storage instance which is used to save thumbanil file"""
        return default_storage

    def get_thumbnail_filename(self, f):
        """get thumbnail filename"""
        filename = os.path.basename(f.path)
        pattern = settings.ATTACHMENT_UPLOAD_PATH_THUMBNAIL
        return get_filename_pattern(pattern, filename)

    def create_thumbnail_response(self, f, width, height, mimetype):
        """get HttpResponse instance for thumbanil"""
        response = HttpResponse(mimetype='image/png')
        thumbnail = self.get_thumbnail(f, width, height, mimetype)
        thumbnail.save(response, "png")
        return response

    def get_thumbnail(self, f, width, height, mimetype):
        storage = self.get_storage()
        thumbnail_filename = self.get_thumbnail_filename(f)

        if storage.exists(thumbnail_filename):
            thumbnail = Image.open(storage.open(thumbnail_filename))
            return thumbnail

        # no thumbnail file exists yet
        return self.create_thumbnail(f, width, height, mimetype)

    def create_thumbnail(self, f, width, height, mimetype):
        raise NotImplementedError

