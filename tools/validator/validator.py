import json
import sys
import argparse
try:
    from nacl.encoding import HexEncoder
    from nacl.signing import VerifyKey
    _HAS_NACL = True
except Exception:
    _HAS_NACL = False


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def index_gpa(creditos):
    gpa_areas = {}
    for item in creditos:
        area = item.get("area")
        gpa_item = item.get("gpa_item")
        if area is None or gpa_item is None:
            continue
        acc = gpa_areas.setdefault(area, {"soma": 0.0, "n": 0})
        acc["soma"] += float(gpa_item)
        acc["n"] += 1
    medias = {k: (v["soma"] / v["n"]) for k, v in gpa_areas.items() if v["n"] > 0}
    return medias


def contar_creditos(creditos):
    total = 0
    por_area = {}
    for item in creditos:
        c = int(item.get("creditos", 0))
        total += c
        area = item.get("area")
        if area:
            por_area[area] = por_area.get(area, 0) + c
    return total, por_area


def validar_minimos(hist):
    creditos = hist.get("creditos", [])
    gpa = hist.get("gpa", {})
    gpa_geral = float(gpa.get("geral", 0))
    total, por_area = contar_creditos(creditos)
    gpa_area_calc = index_gpa(creditos)

    erros = []
    if total < 72:
        erros.append(f"creditos_total < 72: {total}")
    if gpa_geral < 6.5:
        erros.append(f"gpa_geral < 6.5: {gpa_geral}")
    minimos = {
        "Linguagens": (12, 6.5),
        "Matemática": (12, 6.5),
        "Ciências": (10, 6.0),
        "Tecnologia": (8, 6.0),
    }
    for area, (min_cred, min_gpa) in minimos.items():
        if por_area.get(area, 0) < min_cred:
            erros.append(f"{area}: creditos < {min_cred}")
        if gpa_area_calc.get(area, 0) < min_gpa:
            erros.append(f"{area}: gpa < {min_gpa}")
    return erros


def verificar_assinatura(hist, public_key_hex=None, signature_hex=None):
    if not _HAS_NACL:
        return ["libsodium/PyNaCl nao disponivel para verificacao"] if (public_key_hex or signature_hex or hist.get("assinatura")) else []
    assinatura = hist.get("assinatura", {})
    pk_hex = public_key_hex or assinatura.get("chave_emissora") or assinatura.get("public_key_hex")
    sig_hex = signature_hex or assinatura.get("assinatura") or assinatura.get("signature_hex")
    if not pk_hex or not sig_hex:
        return ["assinatura ausente"]
    vk = VerifyKey(pk_hex, encoder=HexEncoder)
    data_bytes = json.dumps({k: hist[k] for k in hist if k != "assinatura"}, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    try:
        vk.verify(data_bytes, bytes.fromhex(sig_hex))
        return []
    except Exception:
        return ["assinatura invalida"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("historico", help="caminho do historico JSON")
    parser.add_argument("--public-key-hex")
    parser.add_argument("--signature-hex")
    parser.add_argument("--skip-signature", action="store_true")
    args = parser.parse_args()

    hist = load_json(args.historico)
    erros = validar_minimos(hist)
    if not args.skip-signature:
        erros += verificar_assinatura(hist, args.public_key_hex, args.signature_hex)
    if erros:
        print("INVALIDO")
        for e in erros:
            print(f"- {e}")
        sys.exit(1)
    else:
        print("VALIDO")
        sys.exit(0)


if __name__ == "__main__":
    main()


