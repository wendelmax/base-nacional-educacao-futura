## Especificação de Histórico Acadêmico (JSON assinado)

Campos essenciais
- estudante: id, nome, nascimento, escola.
- periodos: lista de anos e semestres.
- creditos: itens com componente, area, horas, creditos, gpa_item, avaliador.
- microcertificacoes: id_catalogo, titulo, carga_horaria, data.
- gpa: geral e por area.
- portfolio: evidencias com url, hash, avaliacao.
- assinatura: algoritmo, chave_emissora, assinatura.

Exemplo mínimo
```json
{
  "estudante": {"id": "123", "nome": "Ana Souza"},
  "creditos": [
    {"componente": "Matemática aplicada", "area": "Matemática", "horas": 120, "creditos": 2, "gpa_item": 8.2}
  ],
  "gpa": {"geral": 8.1, "areas": {"Matemática": 8.2}},
  "portfolio": [{"url": "https://exemplo/artefato.pdf", "hash": "sha256:..."}],
  "assinatura": {"algoritmo": "ed25519", "chave_emissora": "...", "assinatura": "..."}
}
```

Diagrama de dados (classes e relações)

<div class="mermaid">
classDiagram
  class Historico {
    +Estudante estudante
    +Creditos[] creditos
    +GPA gpa
    +Evidencia[] portfolio
    +Assinatura assinatura
  }
  class Estudante {
    +string id
    +string nome
    +date nascimento (opcional)
    +string escola (opcional)
  }
  class Creditos {
    +string componente
    +string area
    +int horas
    +int creditos
    +float gpa_item (opcional)
    +string avaliador (opcional)
    +date data (opcional)
  }
  class GPA {
    +float geral
    +map areas
  }
  class Evidencia {
    +string url
    +string hash
    +string avaliacao (opcional)
  }
  class Assinatura {
    +string algoritmo
    +string chave_emissora
    +string assinatura
  }
  Historico --> Estudante
  Historico --> Creditos
  Historico --> GPA
  Historico --> Evidencia
  Historico --> Assinatura
</div>


