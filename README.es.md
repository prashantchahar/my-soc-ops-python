<!-- l10n-sync: source-file="README.md" -->
🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# 🎯 Soc Ops — Bingo Social

> **¡Rompe el hielo, haz conexiones, gana en el networking!**

Soc Ops es un juego de bingo social interactivo diseñado para encuentros presenciales, eventos de equipo y conferencias. ¡Encuentra personas que coincidan con las preguntas, marca tu cartón y corre a conseguir 5 en fila!

## ✨ Características

- 🎲 **Tableros aleatorios** — Cada jugador obtiene una disposición única
- 💾 **Guardado automático** — Retoma donde lo dejaste
- 🏆 **Detección de bingo** — Detección automática de filas, columnas y diagonales
- 🎉 **Modal de celebración** — Pantalla de victoria digna de confeti
- 📱 **Mobile-first** — Funciona genial en teléfonos durante eventos

## 🚀 Inicio Rápido

### Requisitos Previos
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

### Linting
```bash
uv run ruff check .
```

## 🎨 Personaliza Tu Juego

### Cambiar Preguntas
Edita `app/data.py` para agregar tus propias preguntas rompe-hielo:
```python
questions_list: list[str] = [
    "tiene una mascota",
    "habla más de 2 idiomas",
    "tu pregunta personalizada aquí",
    # ... 24+ preguntas para un tablero completo
]
```

### Guía del Taller
👉 Sigue la [Guía del Lab](workshop/GUIDE.md) para una experiencia práctica con los agentes de GitHub Copilot.

## 🛠️ Stack Tecnológico

- **Framework**: FastAPI + Jinja2 + HTMX
- **Estilos**: Utilidades CSS personalizadas (inspiradas en Tailwind)
- **Estado**: Sesiones del lado del servidor con persistencia de cookies
- **Despliegue**: GitHub Pages mediante Actions

## 📁 Estructura del Proyecto

```
app/
├── templates/       # Plantillas Jinja2
│   ├── base.html
│   ├── home.html
│   └── components/  # bingo_board, bingo_modal, game_screen, start_screen
├── static/          # Recursos CSS y JS
├── models.py        # Estado del juego y modelos de datos
├── game_logic.py    # Detección de bingo y generación de tablero
├── game_service.py  # Gestión de sesiones
├── data.py          # Banco de preguntas
└── main.py          # Rutas FastAPI
tests/
├── test_api.py      # Pruebas de endpoints de la API
└── test_game_logic.py  # Pruebas unitarias de lógica del juego
```

## 📚 Guía del Laboratorio

| Parte | Título |
|-------|--------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Visión General y Lista de Verificación |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Configuración y Context Engineering |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Desarrollo Frontend Orientado al Diseño |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Quiz Master Personalizado |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Desarrollo Multi-Agente |

> 📝 Las guías del laboratorio también están disponibles en la carpeta [`workshop/`](workshop/) para lectura sin conexión.

## 🚢 Despliegue

Se despliega automáticamente en GitHub Pages al hacer push a `main`:
- Tu juego: `https://{usuario}.github.io/{nombre-repo}`

## 📝 Licencia

MIT — ¡úsalo en tu próximo evento!
