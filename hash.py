# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org/>

import argparse
import hashlib

# blocksize = 256 kibibytes
def hashfile(afile, hasher, blocksize=262144):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar='file', nargs='+', help='file(s) to hash')
    filelist = parser.parse_args().files
    for f in filelist:
        print "\n\tHash\t", f
        print "\tMD5   \t", hashfile(open(f, 'rb'), hashlib.md5())
#       print "\tSHA1  \t", hashfile(open(f, 'rb'), hashlib.sha1())
        print "\tSHA256\t", hashfile(open(f, 'rb'), hashlib.sha256())
        print "\tSHA512\t", hashfile(open(f, 'rb'), hashlib.sha512())
        

