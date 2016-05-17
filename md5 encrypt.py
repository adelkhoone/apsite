# -*- coding: utf-8 -*-

import hashlib
import random

def random_password():
    tmp = random.randrange(1000000, 9999999)
    tmp2 = str(tmp)
    m = hashlib.md5()
    m.update(tmp2)
    return (str(m.hexdigest()), tmp2)


def encryptor(password):
    m = hashlib.md5()
    m.update(password)
    return str(m.hexdigest())

