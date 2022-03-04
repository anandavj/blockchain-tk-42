from eth_hash.auto import keccak

print(keccak(b''))

preimage = keccak.new(b'part-a')
preimage_two = preimage.copy()
preimage.update(b'part-b')
print(preimage.digest())
preimage_two.update(b'part-c')
print(preimage_two.digest())