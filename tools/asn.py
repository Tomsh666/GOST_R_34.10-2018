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








def asn_decode():
    pass