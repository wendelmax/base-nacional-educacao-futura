import argparse
import json
import sys
from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder


def cmd_keygen(args):
    sk = SigningKey.generate()
    vk = sk.verify_key
    print(json.dumps({
        "private_key_hex": sk.encode(encoder=HexEncoder).decode(),
        "public_key_hex": vk.encode(encoder=HexEncoder).decode()
    }))


def cmd_sign(args):
    with open(args.input, "r", encoding="utf-8") as f:
        data = f.read()
    sk = SigningKey(args.private_key_hex, encoder=HexEncoder)
    sig = sk.sign(data.encode("utf-8")).signature
    print(json.dumps({
        "signature_hex": sig.hex()
    }))


def cmd_verify(args):
    with open(args.input, "r", encoding="utf-8") as f:
        data = f.read()
    vk = VerifyKey(args.public_key_hex, encoder=HexEncoder)
    try:
        vk.verify(data.encode("utf-8"), bytes.fromhex(args.signature_hex))
        print("VALIDA")
        sys.exit(0)
    except Exception:
        print("INVALIDA")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_keygen = sub.add_parser("keygen")
    p_keygen.set_defaults(func=cmd_keygen)

    p_sign = sub.add_parser("sign")
    p_sign.add_argument("--input", required=True)
    p_sign.add_argument("--private-key-hex", required=True)
    p_sign.set_defaults(func=cmd_sign)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("--input", required=True)
    p_verify.add_argument("--public-key-hex", required=True)
    p_verify.add_argument("--signature-hex", required=True)
    p_verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()


