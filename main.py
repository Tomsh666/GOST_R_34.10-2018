import signature
from tools import signature_params, generate_keys, asn_encode, asn_decode


def main():
    print("1.Create signature")
    print("2.Verify signature")

    p, q, curve, P = signature_params()
    d, Q = generate_keys(q, P, curve[0], p)
    file_name = "plain_text.txt"
    sign_file_name = "sign.asn1"
    while True:
        choice = input("Select an option:")
        if choice == "1":
            with open(file_name, 'rb') as f:
                M = f.read()
            r, s = signature.create(d, p, q, curve, P, M)
            asn_data = asn_encode(Q, p, curve[0], curve[1], P, q, r, s)
            with open(sign_file_name, 'wb') as f:
                f.write(asn_data)
            print("Done")
        elif choice == "2":
            with open(file_name, 'rb') as f:
                M = f.read()
            with open(sign_file_name, 'rb') as f:
                asn_data = f.read()
            Q, p, P, q, curve, r, s = asn_decode(asn_data)
            result = signature.verify(Q, p, P, q, curve, r, s, M)
            if result:
                print("Signature verified")
            else:
                print("Signature corrupted")
            print("Done")
        else:
            print("Wrong option")


if __name__ == '__main__':
    main()

