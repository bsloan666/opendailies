
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
import time
import od_configure as conf 
import od_callbacks as cb 

def execute_command(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, env=os.environ)

def extract_output(cmd):
    proc = execute_command(cmd)
    out, err = proc.communicate()
    return out+err

def get_dimensions(fname):
    cmd = [conf.oiiotool_command]
    cmd.append('--info')
    cmd.append(fname)
    out = extract_output(" ".join(cmd))
    infarray = re.split("\s+", out)
    return infarray[2], infarray[4].rstrip(',')

