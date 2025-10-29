## Assinatura e Verificação do Histórico (ed25519)

Dependência: ver `requirements.txt`.

???+ tip "Checklist — Geração de chaves"
    - [ ] Instalar dependências (`pip install -r requirements.txt`)
    - [ ] Gerar par de chaves: `python tools/crypto/sign_verify.py keygen`
    - [ ] Guardar a chave privada em cofre (HSM/secret)

???+ tip "Checklist — Assinatura"
    - [ ] Validar JSON (schema básico)
    - [ ] Assinar: `python tools/crypto/sign_verify.py sign --input data/historico_exemplo.json --private-key-hex <HEX>`
    - [ ] Inserir `assinatura.assinatura` e `assinatura.chave_emissora` no JSON

???+ tip "Checklist — Verificação"
    - [ ] Verificar: `python tools/crypto/sign_verify.py verify --input data/historico_exemplo.json --public-key-hex <HEX> --signature-hex <HEX>`
    - [ ] Registrar resultado (OK/erros) no protocolo de submissão

??? info "Boas práticas"
    - Armazenar chave privada em HSM/cofre; rotacionar semestralmente
    - Registrar assinatura e hash do arquivo no protocolo de submissão


