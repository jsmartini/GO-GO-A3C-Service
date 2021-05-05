import pickle
import lz4.frame

def pack(data):
    #compresses and serializes weight data
    return pickle.dumps(
        lz4.frame.compress(data)
    )

def unpack(data):
    #decompresses and serializes weight data
    return pickle.loads(
        lz4.frame.decompress(data)
    )

    