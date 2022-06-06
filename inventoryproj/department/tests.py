from zipfile import *

f=ZipFile('files.zip','w',ZIP_DEFLATED)

f.write('file1.txt')
f.write('file2.txt')
f.close()

