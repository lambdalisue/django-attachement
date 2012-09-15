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
from django import template
from django.template import TemplateSyntaxError
from django.template.loaders.app_directories import load_template_source
 
register = template.Library()
 
def do_include_raw(parser, token):
    """ 
    Performs a template include without parsing the context, just dumps the template in.
    """
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError, "%r tag takes one argument: the name of the template to be included" % bits[0]
 
    template_name = bits[1]
    if template_name[0] in ('"', "'") and template_name[-1] == template_name[0]:
        template_name = template_name[1:-1]
 
    source, path = load_template_source(template_name)
 
    return template.TextNode(source)
register.tag("include_raw", do_include_raw)

