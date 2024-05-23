from Crypto.Util.number import getPrime, inverse
from random import randint
from .tools import scalar_multiply


def signature_params():
    p = 57896044620753384133869303843568937902752767818974600847634902975134129543643
    q = 28948022310376692066934651921784468951377218528270520403696863131129758387393
    a = 1
    b = 52259530098387149819562511889780651425271270942919542722038553712464420235875
    xP = 14539175448068301073584752148116082765715462525899666138074034449285211025933
    yP = 8328801466633898282311029798556417767141491055036399348346324804478619400451
    curve = (a, b, p)
    P = (xP, yP)
    print("p:", p)
    print(f"E: y^2 = x^3 + {curve[0]}x + {curve[1]} (mod {curve[2]})")
    print("q:", q)
    print("P:", P)
    return p, q, curve, P


def generate_keys(q, P, a, p):
    d = randint(1, q - 1)
    Q = scalar_multiply(d, P, a, p)
    print("d:", d)
    print("Q:", Q)
    return d, Q
