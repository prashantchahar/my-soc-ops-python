<!-- l10n-sync: source-file="README.md" -->
🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# 🎯 Soc Ops — Social Bingo

> **¡Rompe el hielo, haz conexiones, gana en el networking!**

Soc Ops es un juego interactivo de bingo social diseñado para encuentros presenciales, eventos de equipo y conferencias. ¡Encuentra personas que coincidan con las pistas, marca tu cartón y compite por conseguir 5 en fila!

## ✨ Características

- 🎲 **Tableros aleatorios** — Cada jugador recibe un arreglo único
- 💾 **Progreso guardado automáticamente** — Continúa donde lo dejaste
- 🏆 **Detección de bingo** — Detección automática de victoria en filas, columnas y diagonales
- 🎉 **Modal de celebración** — Pantalla de victoria digna de confeti
- 📱 **Mobile-first** — Funciona genial en teléfonos en eventos

## 🚀 Inicio Rápido

### Prerrequisitos
- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes Python)

### Ejecutar Localmente
```bash
uv sync
uv run uvicorn app.main:app --reload --port 8000
# Abre http://localhost:8000
```

### Pruebas
```bash
uv run pytest
```

### Lint
```bash
uv run ruff check .
```

## 🎨 Personaliza Tu Juego

### Cambiar Preguntas
Edita `app/data.py` para añadir tus propios prompts de introducción:
```python
questions_list: list[str] = [
    "tiene una mascota",
    "habla más de 2 idiomas",
    "tu pregunta personalizada aquí",
    # ... 24+ preguntas para un tablero completo
]
```

### Guía del Workshop
👉 Sigue la [Guía del Laboratorio](workshop/GUIDE.md) para una experiencia práctica de taller con agentes de GitHub Copilot.

## 🛠️ Stack Tecnológico

- **Framework**: FastAPI + Jinja2 + HTMX
- **Estilos**: Utilidades CSS personalizadas (inspiradas en Tailwind)
- **Estado**: Sesiones en el servidor con persistencia en cookie
- **Despliegue**: GitHub Pages mediante Actions

## 📁 Estructura del Proyecto

```
app/
├── templates/       # Plantillas Jinja2
│   ├── base.html
│   ├── home.html
│   └── components/  # bingo_board, bingo_modal, game_screen, start_screen
├── static/          # Assets CSS & JS
├── models.py        # Estado del juego & modelos de datos
├── game_logic.py    # Detección de bingo & generación de tablero
├── game_service.py  # Gestión de sesiones
├── data.py          # Banco de preguntas
└── main.py          # Rutas FastAPI
tests/
├── test_api.py      # Tests de endpoints de la API
└── test_game_logic.py  # Tests unitarios de la lógica del juego
```

## 🚢 Despliegue

Se despliega automáticamente en GitHub Pages al hacer push a `main`:
- Tu juego: `https://{usuario}.github.io/{nombre-del-repo}`

## 📚 Guía del Laboratorio

| Parte | Título |
|-------|--------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Visión General y Lista de Verificación |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Configuración y Context Engineering |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Desarrollo Frontend Orientado al Diseño |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Quiz Master Personalizado |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Desarrollo Multi-Agente |

> 📝 Las guías del laboratorio también están disponibles en la carpeta [`workshop/`](workshop/) para lectura sin conexión.

## 📝 Licencia

MIT — ¡úsalo en tu próximo evento!
