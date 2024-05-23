from Crypto.Util.number import inverse

from pygost import gost34112012

import tools


def verify(Q, p, P, q, curve, r, s, M):
    if not (0 < r < q):
        return False
    if not (0 < s < q):
        return False

    h = gost34112012.GOST34112012(M).hexdigest()

    alpha = int(h, 16)
    e = alpha % q
    if e == 0:
        e = 1

    vi = inverse(e, q)
    z_1 = s * vi % q
    z_2 = -r * vi % q
    tmp_P = tools.scalar_multiply(z_1, P, curve[0], p)
    tmp_Q = tools.scalar_multiply(z_2, Q, curve[0], p)
    C = tools.algebraic_add(tmp_P, tmp_Q, curve[0], p)
    R = C[0] % q
    if r == R:
        return True

