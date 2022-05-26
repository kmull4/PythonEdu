'''
In a file called extensions.py, implement a program that prompts the
 user for the name of a file and then outputs that file’s media type
  if the file’s name ends, case-insensitively, in any of these
   suffixes:
.gif    image/gif
.jpg    image/jpeg
.jpeg   image/jpeg
.png    image/png
.pdf    application/pdf
.txt    text/plain
.zip    application/zip
unkn    application/octet-stream

...for instance, the media type for a GIF is "image/gif", and the
 media type for a JPEG is "image/jpeg"

See
 developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
  for common types.

If the file’s name ends with some other suffix or has no suffix at all,
 output application/octet-stream instead, which is a common default.
'''

# dictionary of fileTypes:mediaTypes
mydict = {'gif':'image/gif','jpg':'image/jpeg','jpeg':'image/jpeg',
    'png':'image/png','pdf':'application/pdf','txt':'text/plain',
    'zip':'application/zip'}

# get user input and homogenize it
fileName = input('What is the file name?').lower()

# estabhlish a tracker for your index point
index = -1
# start from the back and loop until you hit a period
try:
    while 1:
        # if the index character is a period, exit
        if fileName[index] == '.':
            break
        else: # else, go back one more character in the string
            index -= 1
    # index should be at the period now
    # match fileName[index+1:] with the dictionary
    print(mydict[fileName[index+1:]])
except:
    # if no match or no period in name, give the common default
    print("application/octet-stream")