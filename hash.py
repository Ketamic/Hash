import sys
import hashlib
import argparse

BUF_SIZE = 102400;

md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1();
sha224_hash = hashlib.sha224();
sha256_hash = hashlib.sha256();
sha384_hash = hashlib.sha384();
sha512_hash = hashlib.sha512();

if len(sys.argv) < 2:
    print("Please input the file you would like to checksum")
    sys.exit(-1)
filename = sys.argv[1]

try:
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5_hash.update(data)
            sha1_hash.update(data)
            sha224_hash.update(data)
            sha256_hash.update(data)
            sha384_hash.update(data)
            sha512_hash.update(data)
except:
    print("File could not be found/opened")


print("MD5: {0}".format(md5_hash.hexdigest()))
print("SHA1: {0}".format(sha1_hash.hexdigest()))
print("SHA224: {0}".format(sha224_hash.hexdigest()))
print("SHA256: {0}".format(sha256_hash.hexdigest()))
print("SHA384: {0}".format(sha384_hash.hexdigest()))
print("SHA512: {0}".format(sha512_hash.hexdigest()))
    