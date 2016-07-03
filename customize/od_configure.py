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
Custom OpenDailies configuration
"""

from odict import OrderedDict

oiiotool_command = 'env LD_PRELOAD=/tools/package/gcc/4.8.5/lib64/libstdc++.so \
        /dd/dept/software/users/bsloan/swdevl/bsloan/3ps/openimageio/1.7.2/private/build/openimageio/bin/oiiotool'

fonts = { 
        'normal':'/dd/facility/lib/fonts/Arial.ttf' , 
        'bold':'/dd/facility/lib/fonts/Arial\ Bold.ttf'}

colors = { 
        'red':'1.0,0.0,0.0', 
        'white':'1.0,1.0,1.0', 
        'gray':'0.3,0.3,0.3'}

font_sizes = {
        'large':0.05555 * 1.5 , 
        'venti':0.03333 * 1.5 , 
        'medium':0.0277 * 1.5, 
        'small':0.0185 * 1.5}

formats = {
        'editorial':{'width':1920,'height':1080},
        'full':{'width':2150,'height':1210}
        }


slate_backdrop = {
        'file':'/dd/shows/@show/SHARED/IMG/comp/slate.odd/DD3_Slate_8K_v10.exr',
        'x_offset':0,
        'y_offset':0.08518
        }

slate_labels_top = 0.2148 - 0.05555 * 1.5
slate_labels_left = 0.0666

slate_thumb_top = 0.15 
slate_thumb_left = 0.5
slate_thumb_size = 0.14

slate_version_top = 0.4
slate_version_left = 0.85

temp_dir = '/var/tmp'

slate_labels = [
        ["@show", 'white', 'large', 'normal'],
        ["@baked", 'red', 'medium', 'bold'],
        ['@time', 'gray', 'small', 'normal'],
        ["---", 0.1],
        ["@shot", 'white', 'venti', 'normal'],
        ]

slate_fields = OrderedDict()
slate_fields["---"]= 0.03
slate_fields["DD Name"]="@daily"
slate_fields["User"]="@user"
slate_fields["Notes"]="@notes"
slate_fields["----"]=0.1
slate_fields["Frames"]="@start-@end"
slate_fields["Lens"]="@lens"


version = 154

overlay_labels = [
    [0.451,0.062, 0.028, "@delivery_name"],
    [0.8,0.062, 0.028, "@time"],
    [0.381,0.955, 0.028, "Property of @client"],
    [0.881,0.955, 0.028, "@frame"]
        ]

movie_extensions = ['mp4', 'mov', 'webm', 'mpg']
sequence_extensions = ['exr', 'tiff', 'jpg', 'dpx']

fields = ['@time', '@frame', '@daily', '@delivery_name',
          '@user', '@lens', '@client', '@notes', '@baked',
          '@show', '@shot', '@sequence', '@version',
          '@start', '@end']
