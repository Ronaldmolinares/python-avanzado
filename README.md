# Platzi News 📰🤖

## Descripción General

Este proyecto es parte del curso "Python Avanzado" en Platzi, impartido por [@lcmartinezdev](https://github.com/lcmartinezdev).

**Platzi News** es una aplicación de línea de comandos (CLI) desarrollada en Python que permite buscar noticias de diferentes fuentes y hacer preguntas inteligentes sobre ellas utilizando inteligencia artificial. El usuario puede elegir específicamente de qué fuente obtener las noticias.

La aplicación integra tres APIs principales:
- **The Guardian API** - Para noticias internacionales de calidad
- **News API** - Para acceder a múltiples fuentes de noticias globales
- **Google AI Studio (Gemini) API** - Para análisis inteligente y respuestas contextuales

## Características Principales

✅ **Búsqueda de Noticias**: Consulta noticias en tiempo real desde The Guardian y News API con un solo comando

✅ **Análisis con IA**: Utiliza Gemini de Google AI Studio para analizar artículos y responder preguntas específicas sobre las noticias encontradas

✅ **Interfaz Simple**: Comandos intuitivos y fáciles de usar desde la terminal

✅ **Selección de Fuente**: Elige específicamente de qué fuente obtener las noticias (Guardian o NewsAPI)

✅ **Configuración Flexible**: Gestión de API keys mediante variables de entorno


**Requisitos:**
- Python 3.13 o superior
- Claves de API válidas para The Guardian, News API y Google AI Studio

## Uso

### 1. Buscar Noticias
```bash
platzi-news search "query" --source [guardian|newsapi]
```
**Ejemplos:**
```bash
platzi-news search "tecnología" --source newsapi
platzi-news search "inteligencia artificial" --source guardian
platzi-news --log-level DEBUG search "tecnología" --source newsapi
```
Este comando busca noticias relacionadas con el query en la fuente especificada y muestra una lista con títulos, descripciones y enlaces.

**Parámetros:**
- `query`: El término o tema a buscar
- `--source`: La fuente de noticias (`guardian` o `newsapi`)

**Opciones globales:**
- `--log-level [DEBUG|INFO|WARNING|ERROR|CRITICAL]`: Nivel de logging (opcional, por defecto no se muestran logs)

### 2. Preguntar sobre Noticias
```bash
platzi-news ask "query" "pregunta sobre el tema" --source [guardian|newsapi]
```
**Ejemplos:**
```bash
platzi-news ask "cambio climático" "¿Cuáles son las principales causas mencionadas?" --source guardian
platzi-news --log-level INFO ask "economía global" "¿Qué países se mencionan más?" --source newsapi
```
Este comando:
1. Busca noticias relacionadas con el query en la fuente especificada
2. Envía los artículos a Google AI (Gemini)
3. Obtiene una respuesta inteligente basada en el contenido de las noticias

**Parámetros:**
- `query`: El término o tema a buscar
- `pregunta`: La pregunta específica sobre el tema
- `--source`: La fuente de noticias (`guardian` o `newsapi`)

## Tecnologías Utilizadas

- **Python 3.13+** - Lenguaje principal
- **requests** - Para consumir las APIs REST
- **python-dotenv** - Gestión de variables de entorno
- **google-generativeai** - Cliente oficial de Google AI Studio (Gemini)
- **rich** - Para una interfaz CLI atractiva y con colores
- **pydantic** - Validación de datos y configuración
- **pydantic-settings** - Gestión de configuración con Pydantic


## Instalación

```bash
uv venv
uv pip install -e .
```

## Configuración

Para usar **Platzi News** necesitas configurar las claves de API. Crea un archivo `.env` en la raíz del proyecto con tus claves:

```env
# Claves de API para Platzi News
GUARDIAN_API_KEY=tu_clave_de_guardian_aqui
NEWSAPI_API_KEY=tu_clave_de_newsapi_aqui
GOOGLE_API_KEY=tu_clave_de_google_ai_aqui

# Configuraciones opcionales
MAX_ARTICLES=10
REQUEST_TIMEOUT=10
GEMINI_MODEL=gemini-1.5-flash-latest
GEMINI_MAX_TOKENS=500
```

### Claves de API Requeridas
- **The Guardian**: Regístrate en https://open-platform.theguardian.com/
- **News API**: Regístrate en https://newsapi.org/
- **Google AI Studio**: Obtén tu API key en https://aistudio.google.com/app/apikey

### Configuraciones Opcionales
- `MAX_ARTICLES`: Número máximo de artículos a obtener (por defecto: 10)
- `REQUEST_TIMEOUT`: Tiempo de espera para las solicitudes API en segundos (por defecto: 10)
- `GEMINI_MODEL`: Modelo de Google Gemini a usar para el análisis (por defecto: gemini-1.5-flash-latest)
- `GEMINI_MAX_TOKENS`: Número máximo de tokens en la respuesta de Gemini (por defecto: 500)

## Logging y Depuración

La aplicación incluye un sistema de logging configurable para monitorear operaciones y depurar problemas. Por defecto, no se muestran logs a menos que se especifique el nivel.

```bash
# Nivel INFO - operaciones principales
platzi-news --log-level INFO search "tecnología" --source guardian

# Nivel DEBUG - información detallada incluyendo requests HTTP
platzi-news --log-level DEBUG search "tecnología" --source guardian

# Nivel ERROR - solo errores
platzi-news --log-level ERROR ask "IA" "¿Qué avances hay?" --source newsapi
```

**Niveles disponibles:**
- `DEBUG`: Información detallada para desarrolladores
- `INFO`: Operaciones principales
- `WARNING`: Advertencias
- `ERROR`: Errores
- `CRITICAL`: Errores críticos

## Casos de Uso

- 📊 Investigar temas de actualidad desde fuentes confiables
- 🎓 Recopilar información para tareas académicas eligiendo la fuente más apropiada
- 💼 Monitorear noticias sobre temas específicos de negocio
- 🔍 Obtener análisis resumidos de artículos de una fuente específica
- 📝 Generar insights a partir de noticias actuales
- 🌍 Comparar la cobertura del mismo tema entre diferentes fuentes

## Ejemplo de Flujo de Trabajo

```bash
# 1. Buscar noticias sobre un tema en The Guardian
platzi-news search "tecnología blockchain" --source guardian

# 2. Hacer una pregunta específica sobre el tema
platzi-news ask "tecnología blockchain" "¿Cuáles son las aplicaciones más prometedoras?" --source guardian

# 3. Buscar el mismo tema en News API
platzi-news search "tecnología blockchain" --source newsapi

# 4. Obtener análisis de una fuente específica
platzi-news ask "energías renovables" "¿Cuáles son las tendencias principales?" --source newsapi
```

## Ventajas

- ⚡ **Rápido**: Obtén información en segundos
- 🎯 **Preciso**: Respuestas basadas en fuentes periodísticas reales
- 🔄 **Actualizado**: Acceso a noticias en tiempo real
- 🎚️ **Flexible**: Elige la fuente que prefieras según tus necesidades
- 🛠️ **Extensible**: Fácil de agregar nuevas fuentes de noticias
- 💡 **Inteligente**: Análisis contextual gracias a Google Gemini

## Desarrollo

### Estructura del Proyecto

```
src/platzi_news/
├── __init__.py
├── config.py              # Configuración y validación de API keys
├── main.py                # Punto de entrada
├── analysis/              # Módulo de análisis con IA
│   ├── __init__.py
│   └── analyzer.py        # Integración con Google AI (Gemini)
├── core/                  # Lógica central de la aplicación
│   ├── __init__.py
│   ├── exceptions.py      # Excepciones personalizadas
│   ├── models.py          # Modelos de datos (Article)
│   └── services.py        # Servicios principales
├── io/                    # Interfaz de entrada/salida
│   ├── __init__.py
│   ├── cli.py             # Lógica de línea de comandos
│   └── display.py         # Funciones de salida con Rich
└── sources/               # Fuentes de noticias
    ├── __init__.py
    ├── guardian.py        # API de The Guardian
    └── newsapi.py         # API de NewsAPI
```

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.