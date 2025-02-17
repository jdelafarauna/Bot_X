![Language](https://img.shields.io/badge/language-Python-blue)  
![Status](https://img.shields.io/badge/status-Finished-green)  

# 🚀 Bot de Noticias Automático para X (Twitter)

Este proyecto es un bot automatizado que obtiene trending topics en español desde Trends24, busca noticias relacionadas en Google News mediante SerpAPI, genera un tweet llamativo usando OpenAI, y lo publica en X (Twitter) con Tweepy.

## 📌 Características
- Obtiene trending topics en español desde Trends24.
- Busca noticias relevantes usando SerpAPI.
- Genera un tweet atractivo con OpenAI (GPT-4 Turbo).
- Publica automáticamente en X (Twitter) con Tweepy.
- Manejo de errores y validaciones para mejorar la estabilidad.

## 🛠️ Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
   ```
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar variables de entorno en un archivo `.env`:
   ```env
   SERPAPI_KEY=tu_serpapi_key
   OPENAI_API_KEY=tu_openai_key
   BEARER_TOKEN=tu_bearer_token
   CONSUMER_KEY=tu_consumer_key
   CONSUMER_SECRET=tu_consumer_secret
   ACCESS_TOKEN=tu_access_token
   ACCESS_TOKEN_SECRET=tu_access_token_secret
   ```

## 🚀 Uso
Ejecuta el script principal:
```bash
python main.py
```
El bot buscará el primer trending topic en español, obtendrá noticias relacionadas, generará un tweet y lo publicará en X (Twitter).

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar el bot, abre un issue o envía un pull request.

## 📬 Contacto
Si tienes preguntas o sugerencias, contáctame en [tu correo o red social].

