from eth_hash.backends import pysha3
from eth_hash import Keccak256

keccak = Keccak256(pysha3)
print(keccak(b''))