from Crypto.Util import asn1
from pyasn1.type import univ
from pyasn1.codec.der import encoder


def asn_encode(Q, p, A, B, P, q, r, s):
    gost_sign_oid = univ.ObjectIdentifier('1.2.643.7.1.1.3.2')
    gost_sign_encoded_oid = encoder.encode(gost_sign_oid)

    asn1_structure = asn1.DerSequence([
        asn1.DerSetOf({
            asn1.DerSequence([
                asn1.DerOctetString(gost_sign_encoded_oid),
                asn1.DerSequence([
                    asn1.DerInteger(Q[0]),
                    asn1.DerInteger(Q[1]),
                ]),
                asn1.DerSequence([
                    asn1.DerSequence([
                        asn1.DerInteger(p),
                    ]),
                    asn1.DerSequence([
                        asn1.DerInteger(A),
                        asn1.DerInteger(B),
                    ]),
                    asn1.DerSequence([
                        asn1.DerInteger(P[0]),
                        asn1.DerInteger(P[1]),
                    ]),
                    asn1.DerInteger(q),
                ]),
                asn1.DerSequence([
                    asn1.DerInteger(r),
                    asn1.DerInteger(s),
                ]),
            ])
        }),
        asn1.DerSequence([])
    ])
    return asn1_structure.encode()


def asn_decode(asn_content):
    asn_seq1 = asn1.DerSequence()
    asn_seq1.decode(asn_content)
    asn_set = asn1.DerSetOf()
    asn_set.decode(asn_seq1[0])
    asn_seq2 = asn1.DerSequence()
    asn_seq2.decode(asn_set[0])
    asn_seq3 = asn1.DerSequence()
    asn_seq3.decode(asn_seq2[1])
    Q = (asn_seq3[0], asn_seq3[1])
    asn_seq3.decode(asn_seq2[2])
    asn_seq4 = asn1.DerSequence()
    asn_seq4.decode(asn_seq3[0])
    p = asn_seq4[0]
    asn_seq4.decode(asn_seq3[2])
    P = (asn_seq4[0], asn_seq4[1])
    q = asn_seq3[3]
    asn_seq4.decode(asn_seq3[1])
    curve = (asn_seq4[0], asn_seq4[1], p)
    asn_seq3.decode(asn_seq2[3])
    r = asn_seq3[0]
    s = asn_seq3[1]
    print("p:", p)
    print(f"E: y^2 = x^3 + {curve[0]}x + {curve[1]} (mod {curve[2]})")
    print("q:", q)
    print("P:", P)
    print("Q:", Q)
    return Q, p, P, q, curve, r, s
