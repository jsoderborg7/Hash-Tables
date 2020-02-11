import hashlib

key = b"str"
# the b strips everything away and makes it a bytes like object (necessary for hash)
my_string = b"this is a normal string..."

for i in range(10):
  hashed = hashlib.sha256(key).hexdigest()
  print(hashed)
  
for i in range(10):
  hashed = hash(key)
  print(hashed)