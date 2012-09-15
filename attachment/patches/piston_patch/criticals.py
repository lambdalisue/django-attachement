# vim: set fileencoding=utf-8 :
"""
A piston patch for fixing piston package structures

1.  Add ``__init__.py`` file to piston module directory
    
    piston 0.2.3 does not have ``__init__.py`` in its PyPI package and it
    cause critical module importing errors in unittests. This patch simply add
    empty ``__init__.py`` file.

2.  Add ``fixtures`` directory and files to piston module directory

    piston 0.2.3 does not have ``fixtures`` directory in its PyPI package and it
    cause critical fixture loading errors in unittests. This patch simply copy
    previously downloaded fixtures to that directory if the directory does not
    exists.

.. Note::
    This patch is not django depended.


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
import shutil
import logging
import piston

logger = logging.getLogger(__name__)

module_dir = piston.__path__[0]

# piston 0.2.3 does not have ``__init__.py`` thus it is not recognized as module
path = os.path.join(module_dir, '__init__.py')
if not os.path.exists(path):
    logger.info("'%s' file is not found in piston. create new one." % path)
    open(path, 'wb').close()
    logger.info("'%s' is created." % path)

# piston 0.2.3 does not have ``fixtures`` directory
path = os.path.join(module_dir, 'fixtures')
if not os.path.exists(path):
    logger.info("'fixtures' for piston is not found. copy from saved.")
    if not os.path.exists(path):
        os.makedirs(path)
    src = os.path.dirname(__file__)
    shutil.copy(os.path.join(src, 'models.json'), path)
    shutil.copy(os.path.join(src, 'oauth.json'), path)
    logger.info("'fixtures' for pistons are created.")
