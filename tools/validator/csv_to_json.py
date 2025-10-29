import csv
import json
import argparse
from typing import List, Dict


def read_credits_csv(path: str) -> List[Dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "componente": r.get("componente"),
                "area": r.get("area"),
                "ano": int(r.get("ano") or 0),
                "horas": int(r.get("horas") or 0),
                "creditos": int(r.get("creditos") or 0),
                "gpa_item": None if not r.get("gpa_item") or r.get("gpa_item") == "0-10" else float(r.get("gpa_item")),
                "avaliador": r.get("avaliador") or None,
                "data": r.get("data") or None,
            })
    return rows


def build_history(estudante_id: str, estudante_nome: str, creditos: List[Dict]) -> Dict:
    gpa_vals = [c["gpa_item"] for c in creditos if isinstance(c.get("gpa_item"), (int, float))]
    gpa_geral = round(sum(gpa_vals) / len(gpa_vals), 2) if gpa_vals else None
    return {
        "estudante": {"id": estudante_id, "nome": estudante_nome},
        "creditos": creditos,
        "gpa": {"geral": gpa_geral},
        "portfolio": [],
        "assinatura": {},
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True, help="arquivo CSV de creditos")
    p.add_argument("--out", required=True, help="arquivo JSON de saida")
    p.add_argument("--id", required=True, help="id do estudante")
    p.add_argument("--nome", required=True, help="nome do estudante")
    args = p.parse_args()

    creditos = read_credits_csv(args.csv)
    hist = build_history(args.id, args.nome, creditos)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(hist, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()


