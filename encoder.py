import hashlib


class encoder:

    def __init__(self):
        pass

    def md5_encode_string(self, s):
        e = hashlib.md5(s).hexdigest()
        # e = hashlib.md5(s).digest()
        return e
