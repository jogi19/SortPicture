
from __future__ import print_function

import exifread
f = open('DSCF8811.JPG')

tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print("Key: %s , value %s" % (tag, tags[tag]))