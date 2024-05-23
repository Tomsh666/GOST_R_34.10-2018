from random import randint
import tools
from pygost import gost34112012


def create(d, p, q, curve, P, M):
    h = gost34112012.GOST34112012(M).hexdigest()

    alpha = int(h, 16)
    e = alpha % q
    if e == 0:
        e = 1

    k = 0
    s = 0
    r = 0
    while s == 0:
        r = 0
        while r == 0:
            k = randint(1, q-1)

            C = tools.scalar_multiply(k, P, curve[0], p)
            r = C[0] % q

        s = (r * d + k * e) % q

    return r, s


