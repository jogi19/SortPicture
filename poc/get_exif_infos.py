import exifread
f = open('2013-06-21 09.24.32.jpg')

tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        # print("Key: %s , value %s" % (tag, tags[tag]))
        if "DateTimeDigitized" in tag:
            print('#####################################')
            print("Key: %s , value %s" % (tag, tags[tag]))
            print('#####################################')
        if "Image DateTime" in tag:
            print('#####################################')
            print("Key: %s , value %s" % (tag, tags[tag]))
            print('#####################################')
