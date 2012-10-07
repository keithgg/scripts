# -*- coding: utf-8 -*-
"""print "Usage: python movemp3.py source_dir dest_dir"

Gets list of files with valid tags in a source_dir and it's sub dirs
and move files to dest_dir/artistname only if dest_dir/artistname exists.
If there are 10 or more files by artist in source_dir the dest_dir/artistname
is created."""


import os
import re
import sys
import shutil

import puddlestuff.audioinfo as audioinfo

from collections import defaultdict
from os.path import isdir, join
from puddlestuff.audioinfo import to_string, encode_fn, decode_fn

try:
    source = sys.argv[1]
    dest = sys.argv[2]
except IndexError:
    print "Usage: python movemp3.py source_dir dest_dir"

if not isdir(source):
   print "The source directory, %s, does not exist." % source
   sys.exit()
elif not isdir(dest):
   print "The destination folder, %s, does not exist." % dest
   sys.exit()


def getfiles(dirpath):
    """Sets the values of artists
    with the artist name as key and a list of the
    music by that artist as a list."""

    #files has key=artist name and value=list of filenames with the same artist.
    files = defaultdict(lambda: [])
    
    for f in os.listdir(dirpath):
        f = join(dirpath, f)
        try:
            tag = audioinfo.Tag(f)
        except:
            pass
        if tag is not None and 'artist' in tag:
            files[to_string(tag['artist'])].append(f)
    return files
                
musicfiles = getfiles(source)

#Move files to their respective dirs.

for artist in musicfiles.keys():
    dirpath = os.path.join(dest, encode_fn(artist))
    if not os.path.isdir(dirpath):
        if len(musicfiles[artist]) > 9:
            os.mkdir(dirpath)
            print "\nCreated folder: %s" % decode_fn(dirpath)
        else:
            continue
       
    for f in musicfiles[artist]:
        try:
            shutil.move(f, join(dest, encode_fn(artist)))
            print "Moved: %s to %s." % (decode_fn(f),
                join(decode_fn(dest), artist))
        except Exception, e:
            print unicode(e)
    del(musicfiles[artist])

#Use it for my own purposes.
#import glob
#misc = {'[0123456789A-F]*': 'Misc[A-F]',
        #'[G-L]*': 'Misc[G-L]',
        #'[M-R]*': 'Misc[M-R]',
        #'[S-Z]*': 'Misc[S-Z]'}

#for reg, misc_dest in misc.items():
    #for f in glob.glob(reg):
        #try:
            #shutil.move(f, os.path.join(dest, misc_dest))
        #except Exception, e:
            #print z
            #print unicode(e)