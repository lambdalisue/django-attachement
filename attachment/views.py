# vim: set fileencoding=utf-8 :
"""
Views of


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
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.utils.text import ugettext_lazy as _

from attachment.models import Attachment

class AttachmentThumbnailView(DetailView):
    model = Attachment

    def render_to_response(self, context):
        width = 160
        height = 120
        import mimetypes
        mimetype = mimetypes.guess_type(self.object.file.path)

        if mimetype[0].startswith('image'):
            from attachment.thumbnails.image import ImageThumbnail
            thumbnail = ImageThumbnail()
            return thumbnail.create_thumbnail_response(self.object.file, width, height, mimetype[0])
        return HttpResponse()

class AttachmentWindowView(TemplateView):
    template_name = r"attachment/attachment_window.html"

    def get_context_data(self, **kwargs):
        context = super(AttachmentWindowView, self).get_context_data(**kwargs)
        # Add ATTACHMENT_MEDIA_URL
        context['ATTACHMENT_MEDIA_URL'] = "%sattachment/" % settings.STATIC_URL
        return context

