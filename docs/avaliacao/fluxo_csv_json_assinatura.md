## Fluxo: CSV → JSON → Assinatura → Validação

???+ tip "1) Preparar créditos no Sheets/CSV"
    - [ ] Usar `sheets/creditos_modelo.csv` como base

???+ tip "2) Converter para JSON"
    - [ ] `python tools/validator/csv_to_json.py --csv sheets/creditos_modelo.csv --out data/historico_gerado.json --id 001 --nome "Aluno Teste"`

???+ tip "3) Assinar"
    - [ ] `python tools/crypto/sign_verify.py sign --input data/historico_gerado.json --private-key-hex <HEX>`
    - [ ] Adicionar `assinatura.assinatura` e `assinatura.chave_emissora` ao JSON

???+ tip "4) Validar créditos e assinatura"
    - [ ] `python tools/validator/validator.py data/historico_gerado.json --public-key-hex <HEX> --signature-hex <SIGHEX>`

Fluxo em diagrama

<div class="mermaid">
sequenceDiagram
  participant S as Sheets/CSV
  participant C as Conversor (csv_to_json)
  participant H as Histórico JSON
  participant K as Assinador (ed25519)
  participant V as Validador CLI
  S->>C: Exporta CSV
  C->>H: Gera JSON
  K->>H: Assina JSON (assinatura + chave)
  V->>H: Valida créditos e assinatura
  V-->>S: Relatório de validação
</div>


