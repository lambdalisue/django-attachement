# vim: set fileencoding=utf-8 :
"""
Models of Attachment


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
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.text import ugettext_lazy as _


class AttachmentManager(models.Manager):
    def get_for_model(self, model):
        ctype = ContentType.objects.get_for_model(model)
        return self.filter(content_type=ctype)

    def get_for_object(self, obj):
        qs = self.get_for_model(obj)
        return qs.filter(object_id=obj.pk)


def _get_upload_to(self, filename):
    upload_to = settings.ATTACHMENT_UPLOAD_PATH_RAW
    if callable(upload_to):
        upload_to = upload_to(filename, self)
    else:
        upload_to = upload_to % {'filename': filename}
    return upload_to


class Attachment(models.Model):
    file = models.FileField(_('attachment file'), upload_to=_get_upload_to)

    content_type = models.ForeignKey(
            ContentType, verbose_name=_('content type'),
            blank=True, null=True, editable=False)
    object_id = models.PositiveIntegerField(_('object id'),
            blank=True, null=True, editable=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    content_object = generic.GenericForeignKey(
            ct_field="content_type", fk_field="object_id")

    objects = AttachmentManager()


    def __unicode__(self):
        return self.file.name

    def get_api_dict(self):
        api_dict = {
                'pk': self.pk,
                'name': self.file.name,
                'size': self.file.size,
                'url': self.file.url,
                'thumbnail_url': reverse('attachment-thumbnail', kwargs={'pk': self.pk}),
                'delete_url': reverse('attachment-api-delete', kwargs={'pk': self.pk}),
                'delete_type': 'DELETE',
            }
        return api_dict

    @models.permalink
    def get_thumbnail_url(self):
        return ('attachment-thumbnail', (), {'pk': self.pk})
