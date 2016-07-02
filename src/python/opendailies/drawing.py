#!/usr/bin/env python

# Copyright (c) 2016, bsloan
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
# 
#     2. Redistributions in binary form must reproduce the above copyright notice,
#        this list of conditions and the following disclaimer in the documentation
#        and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Add Text, lines and shapes to images. 
"""

import os
import re
import sys
import subprocess

global frameno
frameno = ""

def text( x, y, size, color, font, string):
    """Draw a text string of a certain font, size, color, position"""
    return '--text:x={0}:y={1}:size={2}:color={3}:font={4} "{5}"'.format(
            x, y, size, color, font, string)

def drop_shadow_text(x, y, size, font, string):
    cmd = text( x+4, y+4, size, '0.0,0.0,0.0', font, string)
    cmd += " "    
    cmd += text( x, y, size, '0.73,0.73,0.73', font, string)
    return cmd 

def box(color, x1, y1, x2, y2):
    """Draw a hollow, single pixel wide rectangle"""
    return '--box:color=%s %d,%d,%d,%d'%(color, x1, y1, x2, y2)

def thumbnail(thumb_fname, x, y):  
    return ' %s --origin +%d+%d --add'%(thumb_fname, x, y) 
 


