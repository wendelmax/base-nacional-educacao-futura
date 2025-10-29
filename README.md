## Base Nacional Educação Futura — Ensino Médio (4 anos)

[![Pages Deploy](https://github.com/wendelmax/base-nacional-educacao-futura/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/wendelmax/base-nacional-educacao-futura/actions/workflows/gh-pages.yml)
[![Site](https://img.shields.io/website?url=https%3A%2F%2Fwendelmax.github.io%2Fbase-nacional-educacao-futura%2F)](https://wendelmax.github.io/base-nacional-educacao-futura/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Este repositório (base-nacional-educacao-futura) apresenta uma proposta integrada e operacional para um Ensino Médio de 4 anos, orientado por competências, com itinerários técnicos, avaliação por evidências e sistema de créditos compatível com admissão em universidades públicas.

Site público (GitHub Pages): [https://wendelmax.github.io/base-nacional-educacao-futura/](https://wendelmax.github.io/base-nacional-educacao-futura/)

### Motivação e Princípios
- Alinhar a formação à BNCC, práticas internacionais de alto desempenho e às competências do século XXI.
- Combinar núcleo comum robusto com flexibilidade local e itinerários técnicos modulares.
- Avaliação por competências e projetos, com portfólios e microcertificações auditáveis.
- **Sistema de créditos por competências** capaz de substituir ou complementar o ENEM.

### Visão Geral da Estrutura
- **Núcleo Comum**: competências essenciais nas áreas de Linguagens, Matemática, Ciências, Tecnologia e Cidadania.
- Itinerários Formativos: trilhas técnicas e ofícios em módulos de 120–160h, com certificações parciais.
- **Vida Independente e PBL**: aprendizagem baseada em projetos e competências para autonomia.
- **Estágio/Prática**: cumprimento mínimo de 160h, com supervisão e avaliação prática.

### Sistema de Créditos e Admissão ao Ensino Superior
- 1 crédito = 60 horas válidas; referência total ao final do 4º ano: 80 créditos.
- GPA geral e por área; pesos por curso e rigor acadêmico/técnico.
- Integração com SiSU e IES públicas via histórico JSON assinado e auditável.

### Conteúdo do Repositório
- Referências oficiais: ver `docs/Referencias.md`.

- docs/curriculo
  - matriz_curricular.md — estrutura por anos, competências e módulos.
  - matriz_competencias.csv — competências, descritores e evidências.
  - objetivos_por_ano_e_modulo.yaml — objetivos de aprendizagem.
- docs/planos
  - plano_gestao_financeira_40h.md; rubrica_gestao_financeira.md
  - plano_dev_web_mobile_120h.md; rubrica_dev_web_mobile.md
  - plano_eletricidade_residencial_120h.md; rubrica_eletricidade_residencial.md
  - plano_logistica_operacoes_120h.md; rubrica_logistica_operacoes.md
  - plano_culinaria_profissional_120h.md; rubrica_culinaria_profissional.md
  - plano_hvac_120h.md; rubrica_hvac.md
  - plano_autonomia_vida_independente_120h.md; rubrica_autonomia_vida_independente.md
- docs/implementacao
  - mapa_implementacao.md; cronograma.md; custos_estimados.csv
  - piloto_90_dias.md; dashboard_piloto.md
  - plano_comunicacao.md; checklists_oficinas.md
- docs/avaliacao
  - sistema_creditos.md; conversao_enem_equivalencia.md
  - edital_modelo_universidades.md; pesos_por_curso.yaml
  - assinatura_verificacao.md; fluxo_csv_json_assinatura.md
- tools/validator
  - validator.py — valida créditos/GPA e assinatura opcional
  - csv_to_json.py — conversor CSV → JSON do histórico
- tools/crypto
  - sign_verify.py — geração de chaves, assinatura e verificação ed25519
- data
  - creditos_componentes.csv; indicadores.csv; historico_exemplo.json
- sheets
  - creditos_modelo.csv; indicadores_modelo.csv

### Como Usar (Passo a Passo)
1. Ajuste o currículo local selecionando 3–6 itinerários técnicos.
2. Capacite docentes em competências, PBL e avaliação por evidências.
3. Registre créditos no modelo de planilha e gere o histórico JSON:
   - `python tools/validator/csv_to_json.py --csv sheets/creditos_modelo.csv --out data/historico_gerado.json --id 001 --nome "Aluno Teste"`
4. Assine e valide o histórico:
   - Assinar: ver `docs/avaliacao/assinatura_verificacao.md`
   - Validar créditos: `python tools/validator/validator.py data/historico_exemplo.json`
   - Validar com assinatura: `python tools/validator/validator.py data/historico_exemplo.json --public-key-hex <HEX> --signature-hex <HEX>`
5. Acompanhe indicadores do piloto conforme `docs/implementacao/dashboard_piloto.md`.

### Governança e Qualidade
- Moderação externa por amostragem das evidências e bancas.
- Rubricas padronizadas e catálogos de microcertificações por trilha.
- Ajustes de contexto socioeconômico segundo políticas vigentes.

### Licença
- Conteúdo sob CC BY 4.0. Cite a fonte ao reutilizar.

### Contato e Contribuição
- Sugestões e issues: abra uma issue neste repositório.
- Contribuições são bem-vindas via pull request com descrição clara do impacto educacional.

Licença: CC BY 4.0.


