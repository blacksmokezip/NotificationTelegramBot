import zlib
from random import randint


def create_hash(key):
    hash = zlib.crc32(
        bytes(key, "UTF-8")
    ) % 100000
    hash += randint(1, 100)
    return hash
