import hashlib

file1 = open('newfile.txt','r').read().encode('utf-8')
file2 = open('oldfile.txt','r').read().encode('utf-8')

hash1 = hashlib.md5(file1).hexdigest()
hash2 = hashlib.md5(file2).hexdigest()

print(hash1)
print(hash1)

if(hash == hash2):
    print('Duplicate file found!')
else:
    print('The files do not mathc')