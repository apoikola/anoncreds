from hashlib import sha256
from random import randint

from charm.core.math.integer import random, isPrime, integer
from charm.toolbox.conversion import Conversion


def randomQR(n):
    return random(n) ** 2


def encodeAttrs(attrs):
    """
    This function will encode all the attributes to 256 bit integers
    :param attrs: The attributes to pass in credentials
    :return:
    """
    return {key: Conversion.bytes2integer(sha256(value.encode()).digest())
            for key, value in attrs.items()}


def get_hash(*args):
    """
    Enumerate over the input tuple and generate a hash using the tuple values
    :param args:
    :return:
    """
    h_challenge = sha256()
    for i, val in enumerate(args):
        h_challenge.update(Conversion.IP2OS(val))
    return h_challenge.digest()


def get_tuple_dict(*args):
    l = list()
    for i, v in enumerate(args):
        l.extend(list(v.values()))
    return l


def get_prime_in_range(start, end):
    # TODO: Remove ina actual code. This is there to avoid unnecessary running time
    return integer(259344723055062059907025491480697571938277889515152306249728583105665800713306759149981690559193987143012367913206299323899696942213235956742930041765617089060464412844297321155427)
    n = 0
    maxIter = 100000
    while n < maxIter:
        r = randint(start, end)
        if isPrime(r):
            print("Found prime in {} iteration between {} and {}".
                  format(n, start, end))
            return r
        n += 1
    raise Exception("Cannot find prime in {} iterations".format(maxIter))
