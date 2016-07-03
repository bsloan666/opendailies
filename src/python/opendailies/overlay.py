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
Given an image sequence and a frame number, generate an overlay
that may include masks, burn-in, watermark, etc. 
"""

import os
import re
import subprocess
import sys

import drawing
import process as proc
import od_configure as conf 

def render_with_overlay_command(seq_fmt_str, out_fmt_str, frame, dims, labels, context):

    cmd = [conf.oiiotool_command]
    cmd.append( seq_fmt_str%frame)
    context.set_frame('%04d'%frame)
    cmd.append( '-v' )
    cmd.append( '--autocc' )
    cmd.append( '--resize:filter=blackman-harris %dx0 --cut %dx%d'%(
            dims['width'], dims['width'], dims['height']))

    # column of labels along left edge
    for label in labels:
        hpos = int(label[0]*dims['width'] )
        vpos = int(label[1]*dims['height'] )
        size = int(label[2]*dims['height'] )
        text = context.translate(label[3])

        cmd.append(drawing.drop_shadow_text(hpos, vpos, size, 
              conf.fonts['normal'], text))

    overlay_path = out_fmt_str%frame
    cmd.append('--ch R,G,B -o %s'%overlay_path)
    return ' '.join(cmd)

if __name__ in "__main__":
            
    cmd = render_with_overlay_command(sys.argv[1], sys.argv[2], int(sys.argv[3]),  
            conf.formats['editorial'], conf.overlay_labels)

    print cmd

    out = proc.extract_output(cmd)
    print out

