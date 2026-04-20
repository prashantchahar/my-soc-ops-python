<!-- l10n-sync: source-file="README.md" -->
🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# 🎯 Soc Ops — Bingo Social

> **Quebre o gelo, faça conexões, vença no networking!**

Soc Ops é um jogo de bingo social interativo projetado para encontros presenciais, eventos de equipe e conferências. Encontre pessoas que correspondam às perguntas, marque seu cartão e corra para conseguir 5 em linha!

## ✨ Funcionalidades

- 🎲 **Cartelas aleatórias** — Cada jogador recebe um arranjo único
- 💾 **Salvar progresso automaticamente** — Continue de onde parou
- 🏆 **Detecção de bingo** — Detecção automática para linhas, colunas e diagonais
- 🎉 **Modal de celebração** — Tela de vitória digna de confete
- 📱 **Mobile-first** — Funciona muito bem em celulares em eventos

## 🚀 Início Rápido

### Pré-requisitos
- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes Python)

### Executar Localmente
```bash
uv sync
uv run uvicorn app.main:app --reload --port 8000
# Abra http://localhost:8000
```

### Testes
```bash
uv run pytest
```

### Lint
```bash
uv run ruff check .
```

## 🎨 Personalize Seu Jogo

### Alterar Perguntas
Edite `app/data.py` para adicionar suas próprias perguntas de apresentação:
```python
questions_list: list[str] = [
    "tem um animal de estimação",
    "fala mais de 2 idiomas",
    "sua pergunta personalizada aqui",
    # ... 24+ perguntas para uma cartela completa
]
```

### Guia do Workshop
👉 Siga o [Guia do Lab](workshop/GUIDE.md) para uma experiência de workshop prática com os agentes do GitHub Copilot.

## 🛠️ Stack Tecnológica

- **Framework**: FastAPI + Jinja2 + HTMX
- **Estilização**: Utilitários CSS personalizados (inspirados no Tailwind)
- **Estado**: Sessões no lado do servidor com persistência por cookie
- **Implantação**: GitHub Pages via Actions

## 📁 Estrutura do Projeto

```
app/
├── templates/       # Templates Jinja2
│   ├── base.html
│   ├── home.html
│   └── components/  # bingo_board, bingo_modal, game_screen, start_screen
├── static/          # Assets CSS & JS
├── models.py        # Estado do jogo & modelos de dados
├── game_logic.py    # Detecção de bingo & geração de cartela
├── game_service.py  # Gerenciamento de sessão
├── data.py          # Banco de perguntas
└── main.py          # Rotas FastAPI
tests/
├── test_api.py      # Testes de endpoints da API
└── test_game_logic.py  # Testes unitários da lógica do jogo
```

## 🚢 Implantação

Implantação automática no GitHub Pages ao fazer push para `main`:
- Seu jogo: `https://{usuario}.github.io/{repo-name}`

---

## 📚 Guia do Lab

| Parte | Título |
|-------|--------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Visão Geral & Lista de Verificação |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Configuração & Engenharia de Contexto |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Frontend Design-First |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Quiz Master Personalizado |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Desenvolvimento Multi-Agente |

> 📝 Os guias do lab também estão disponíveis na pasta [`workshop/`](workshop/) para leitura offline.

## 📝 Licença

MIT — use para o seu próximo evento!
