import Signature
from tools import signature_params, generate_keys, asn_encode, asn_decode


def main():
    print("1.Create signature")
    print("2.Verify signature")

    p, q, curve, P = signature_params()
    d, Q = generate_keys(q, P, curve[0], p)
    file_name = "plain_text.txt"
    sign_file_name = "sign.asn1"
    #choice = input("Select an option:")
    choice = "1"
    if choice == "1":
        with open(file_name, 'rb') as f:
            M = f.read()
        r, s = Signature.create(d, p, q, curve, P, M)
        asn_data = asn_encode(Q, p, curve[0], curve[1], P, q, r, s)
        with open(sign_file_name, 'wb') as f:
            f.write(asn_data)
        print("Done")
    elif choice == "2":
        Signature.verify()
        print("Done")
    else:
        print("Wrong option")


if __name__ == '__main__':
    main()

