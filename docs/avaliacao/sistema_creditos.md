## Sistema de Créditos por Competências — Modelo para Admissão Pública

Objetivo: substituir ou complementar o ENEM por um histórico de créditos por competências, moderado externamente, para ingresso em universidades públicas.

Unidades e cargas
- Crédito de Ensino Médio (CEM): 1 CEM = 60 horas de aprendizagem valida (aula, PBL, prática, estágio).
- Módulo técnico curto: 2–3 CEM por módulo de 120–180h com microcertificação.
- Projeto Integrador e Estágio: até 4 CEM válidos para admissão.

Estrutura mínima para conclusão
- Núcleo Comum: 40 CEM distribuídos entre linguagens, matemática, ciências, tecnologia, cidadania.
- Itinerários Formativos: 24 CEM em uma ou mais trilhas.
- Vida Independente e PBL: 8 CEM.
- Estágio/Projeto: 8 CEM.
- Total de referência ao final do 4º ano: 80 CEM.

Avaliação e validação
- Avaliação por competências com rubricas padronizadas estaduais e banca externa por amostragem.
- Portfólio digital com evidências-chave auditáveis.
- Moderadores regionais validam 10–20% das evidências por escola por semestre.

GPA por competências
- Escala 0–10, com pesos por área e rigor (AP/Honras = +0,5; Técnico Avançado = +0,5, limitado por área).
- GPA Geral; GPAs de área: Linguagens, Matemática, Ciências, Tecnologia, Cidadania, Técnico.

Requisitos de admissão (modelo geral)
- Padrão Base: ≥72 CEM totais, com mínimos por área e GPAs mínimos definidos pela universidade.
- Cursos seletivos podem exigir trilhas e microcertificações específicas.
- Projeto Integrador com banca obrigatória e parecer externo.

Transparência e interoperabilidade
- Histórico acadêmico em JSON assinado digitalmente, com trilha de auditoria.
- Vocabulário comum de competências e microcertificações.
- Integração com ENEM/SiSU: ver [Equivalência e integração](conversao_enem_equivalencia.md) e [Pesos por curso](pesos_por_curso.yaml).

Diagrama (visão de alto nível)

<div class="mermaid">
flowchart LR
  A[Ensino Médio: Módulos & PBL] --> B{Avaliação por Competências}
  B --> C[Créditos (CEM) & GPA por área]
  C --> D[Histórico JSON assinado]
  D -->|Validação| E[Validador CLI]
  E --> F{IES Públicas / SiSU}
  F --> G[Admissão]
</div>


