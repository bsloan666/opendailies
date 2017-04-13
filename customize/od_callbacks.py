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

import copy
import os
import re
import sys
import time
import od_configure as conf

"""
# These fields need <field>_string() functions defined

fields = ['$time', '$frame', '$daily', '$delivery_name',
          '$user', '$lens', '$client', '$notes', '$baked',
          '$show', '$shot', '$sequence']

"""

path_fields = [
    ('head','(/dd/shows)'),    
    ('show','/([A-Z0-9]+)'),        
    ('sequence','/([A-Z]+)'),        
    ('shot','/([0-9]+)'),        
    ('dummy','/([A-Z]+/[A-Z]+)'),        
    ('role','/([a-z]+)'),
    ('allocation','/([A-Za-z0-9_]+)'),        
    ('version','_v(\d+)'),
    ('format','\.([a-z0-9]+)'),
    ('alloc_2','/([A-Za-z0-9_]+)'),        
    ('ver_2','_v(\d+)'),
    ('pad','\.(%0[\d]d)'),        
    ('extension','\.([a-z0-9]+)')
]

class DailyContext(object):
    def __init__(self, path=""):
        self.fields = {}
        self.frameno = -1
        self.frame_start = -1
        self.frame_end = -1
        path_pattern = re.compile("".join([field[1] for field in path_fields])) 
        if path != "":
            self.path = path
            match = path_pattern.match(path)
            if match:
                for i,field in enumerate(path_fields):
                    self.fields[field[0]]=match.groups()[i]


    def time_string(self):
        """Textual representation of local time"""
        ts = time.localtime()
        tm = time.mktime(ts)
        tt = time.ctime(tm)
        return tt
    
    def set_range(self,s,e):
        self.frame_start = s 
        self.frame_end = e 

    def set_frame(self,fn):
        self.frameno = fn

    def frame_string(self):
        return self.frameno   

    def daily_string(self):
        return '_'.join([self.allocation_string(), self.version_string() ]) 

    def shot_string(self):
        shot = '9999' 
        try:
            shot = self.fields['shot']
        except KeyError, e:
            pass
        return shot
            

    def delivery_name_string(self):
        return '_'.join([self.sequence_string(), self.shot_string(), self.version_string() ])

    def user_string(self):
        return os.getenv('USER')

    def lens_string(self):
        return '35mm' 

    def client_string(self):
        return 'The Clam Dealio Bros.' 

    def notes_string(self):
        return 'Notes go here' 

    def baked_string(self):
        return 'LUT ON' 

    def show_string(self):
        show = 'DEVTD'
        try:
            show = self.fields['show'] 
        except KeyError, e:
            pass
        return show

    def version_string(self):
        version = '001' 
        try:
            version = self.fields['version']
        except KeyError, e:
            pass
        return version
        return self.fields['version']

    def sequence_string(self):
        sequence = 'RD' 
        try:
            sequence = self.fields['sequence']
        except KeyError, e:
            pass
        return sequence

    def allocation_string(self):
        return "".join([self.sequence_string(), self.shot_string()])

    def start_string(self):
        return str(self.frame_start)

    def end_string(self):
        return str(self.frame_end)

    def translate(self,field):
        result = copy.copy(field)
        for string in conf.fields:
            if string in field:
                execstr = 'self.'+string.lstrip('@')+'_string()'
                #print execstr
                val = eval(execstr)
                #print "sub ",string, "with",val,"in",'"',result,'"'
                result = re.sub(string, val, result)
        return result   

if __name__ in '__main__':
    dc = DailyContext(path=sys.argv[1])
    print 'show:',dc.translate('@show')
    print 'shot:',dc.translate('@sequence@shot')
    print 'version:',dc.translate('@version')
    print 'string:',dc.translate('sphincter')
    print 'start:',dc.translate('@start')
    print 'end:',dc.translate('@end')

     

