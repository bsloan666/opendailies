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
Given a path to an image sequence, generate a slate frame. 
"""

import os
import re
import subprocess
import sys

import drawing
import process as proc
import od_configure as conf 

def build_thumbnail_command(seq_fmt_str,frame,dims, outpath ):
    cmd = [conf.oiiotool_command]
    cmd.append( '-v' )
    #cmd.append( '--autocc' )
    cmd.append(seq_fmt_str%frame)
    cmd.append( '--ch R,G,B --resize %dx%d'%(
            int(dims['width'] * conf.slate_thumb_size), int( dims['height']* conf.slate_thumb_size )))
    cmd.append('-o %s'%outpath)
    return " ".join(cmd)

def build_slate_command(seq_fmt_str, out_fmt_str, start, end, dims, labels, fields, context):
    if not os.path.exists(conf.temp_dir):
        os.makedirs(conf.temp_dir)
    context.set_range(start, end)    
    thumb_1_path = conf.temp_dir+"/"+os.path.basename(seq_fmt_str)%start
    thumb_2_path = conf.temp_dir+"/"+os.path.basename(seq_fmt_str)%(start+(end - start)/2)
    thumb_3_path = conf.temp_dir+"/"+os.path.basename(seq_fmt_str)%end
    cmd = build_thumbnail_command(seq_fmt_str,start,dims, thumb_1_path)
    print proc.extract_output(cmd)
    cmd = build_thumbnail_command(seq_fmt_str,start+(end - start)/2,dims, thumb_2_path)
    print proc.extract_output(cmd)
    cmd = build_thumbnail_command(seq_fmt_str,end,dims, thumb_3_path)
    print proc.extract_output(cmd)

    thumb_width,thumb_height = proc.get_dimensions(thumb_1_path)

    thumb_width = int(thumb_width)
    thumb_height = int(thumb_height)

    backdrop_shift = int(dims['height'] * conf.slate_backdrop['y_offset'])   
    cmd = [conf.oiiotool_command]
    cmd.append( context.translate(conf.slate_backdrop['file']))
    cmd.append( '-v' )
    #cmd.append( '--autocc' )
    cmd.append( '--resize %dx0 --crop %dx%d+0+%d --cut %dx%d'%(
            dims['width'], dims['width'], dims['height'] - backdrop_shift,
            backdrop_shift, dims['width'], dims['height']))
    cmd.append( drawing.box(conf.colors['red'], 0,0,dims['width']-1, dims['height']-1))
    cmd.append( drawing.box(conf.colors['red'], 1,1,dims['width']-2, dims['height']-2))
    vpos = int(conf.slate_labels_top * dims['height'])
    hpos = int(conf.slate_labels_left * dims['width'])

    # column of labels along left edge
    for label in labels:
        if label[0] == "---":
            vpos += int(label[1]*dims['height'] )
        else:    
            vpos += int(conf.font_sizes[label[2]]*dims['height'] ) + 4
            cmd.append(drawing.text(hpos, vpos, 
                int(conf.font_sizes[label[2]]*dims['height'] ),
                conf.colors[label[1]], conf.fonts[label[3]], context.translate(label[0])))
    widest = 0
    for key in fields.items():
        if len(key) > widest:
            widest = len(key)

    # 2 columns of key-value fields along left edge below labels
    for key,value in fields.items():
        if key.startswith("---"):
            vpos += int(value*dims['height'] )
        else:    
            vpos += int(conf.font_sizes['small']*dims['height'] ) + 4
            cmd.append(drawing.text(hpos, vpos, 
                int(conf.font_sizes['small']*dims['height'] ),
                conf.colors['white'], conf.fonts['normal'], key+':'))
            cmd.append(drawing.text(int(hpos + widest * conf.font_sizes['medium'] * dims['width']), 
                vpos, int(conf.font_sizes['small']*dims['height'] ),
                conf.colors['gray'], conf.fonts['normal'], context.translate(value)))

    # big version at right 
    cmd.append(drawing.text(int(conf.slate_version_left * dims['width']), 
        int(conf.slate_version_top * dims['height']), 
        int(conf.font_sizes['small']*dims['height'] ),
        conf.colors['gray'], conf.fonts['normal'], 'V'))

    cmd.append(drawing.text(int(conf.slate_version_left * dims['width'] + conf.font_sizes['small'] * dims['height']), 
        int(conf.slate_version_top * dims['height']), int(conf.font_sizes['venti']*dims['height'] ),
        conf.colors['white'], conf.fonts['bold'], '%s'%conf.version))

    cmd.append(drawing.thumbnail(thumb_1_path, int(dims['width'] * conf.slate_thumb_left), 
            int(dims['height'] * conf.slate_thumb_top)))
    cmd.append(drawing.thumbnail(thumb_2_path, int(dims['width'] * conf.slate_thumb_left)+ thumb_width + 14, 
            int(dims['height'] * conf.slate_thumb_top)))
    cmd.append(drawing.thumbnail(thumb_3_path, int(dims['width'] * conf.slate_thumb_left)+ (thumb_width + 14)*2, 
            int(dims['height'] * conf.slate_thumb_top )))

    slate_path = out_fmt_str%(int(start)-1)
    cmd.append('-o %s'%slate_path)
    return ' '.join(cmd)

if __name__ in "__main__":
            
    cmd = build_slate_command(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]),  
            conf.formats['editorial'], conf.slate_labels, conf.slate_fields)

    print cmd
    out = proc.extract_output(cmd)
    print out





