import os
import requests
import openai
import tweepy
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from langdetect import detect

# Cargar variables desde .env
load_dotenv()

# Obtener claves desde el .env
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def obtener_trending_topic():
    """Scrapea los trending topics de X desde Trends24 y filtra el primero en español."""
    url = "https://trends24.in/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("❌ Error al obtener trending topics")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar la lista de trending topics en Trends24
        trending_section = soup.find("ol", class_="trend-card__list")
        if not trending_section:
            print("⚠️ No se encontraron trending topics.")
            return None

        trends = trending_section.find_all("li")  # Buscar los elementos <li> dentro de la lista

        # Filtrar el primer trending topic que esté en español
        for trend in trends:
            trending_topic = trend.text.strip()
            if trending_topic and detect(trending_topic) == "es":
                print(f"🔥 Trending Topic en español: {trending_topic}")
                return trending_topic

        print("⚠️ No se encontraron trending topics en español.")
        return None

    except Exception as e:
        print(f"❌ Error en scraping: {e}")
        return None

def buscar_noticias_google(tema):
    """Busca noticias en Google News usando SerpAPI."""
    url = "https://serpapi.com/search"
    params = {
        "q": tema,
        "tbm": "nws",  # Búsqueda en Google News
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("❌ Error en la solicitud a SerpAPI.")
        print("Código de estado HTTP:", response.status_code)
        print("Respuesta completa:", response.text)
        return None

    noticias = response.json().get("news_results", [])

    if not noticias:
        print("⚠️ No hay noticias en la búsqueda.")
        return None  # No hay resultados

    # Tomar la noticia más relevante
    noticia = noticias[0]
    titulo = noticia["title"]
    descripcion = noticia.get("snippet", "Sin descripción")
    url_noticia = noticia["link"]

    return f"Título: {titulo}\nDescripción: {descripcion}\nURL: {url_noticia}"

def generar_tweet(noticia):
    """Usa OpenAI para resumir la noticia en un tweet de 230 caracteres."""
    openai.api_key = OPENAI_API_KEY
    prompt = f"Redacta un tweet llamativo sobre la siguiente noticia en 230 caracteres:\n\n{noticia}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Eres un redactor de noticias en Twitter. No añadas URLs, solo hastags"},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"❌ Error en OpenAI: {e}")
        return None

def publicar_en_x(tweet):
    """Publica el tweet en X (Twitter) usando la API v2 de Tweepy."""
    try:
        client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        response = client.create_tweet(text=tweet)
        print(f"✅ Tweet publicado con éxito: https://twitter.com/user/status/{response.data['id']}")

    except Exception as e:
        print(f"❌ Error al publicar el tweet: {e}")

def main():
    """Ejecuta la búsqueda del trending topic, obtiene noticias y publica en X."""
    print("\n🔎 Obteniendo trending topic de X en español...")
    trending_topic = obtener_trending_topic()

    if trending_topic:
        print("\n⏳ Buscando noticias sobre:", trending_topic)
        noticia = buscar_noticias_google(trending_topic)

        if noticia:
            print("\n✍️ Generando tweet...")
            tweet = generar_tweet(noticia)

            if tweet:
                print("\n🚀 Publicando en X...")
                print(tweet)
                #publicar_en_x(tweet)
            else:
                print("❌ No se pudo generar el tweet.")
        else:
            print("❌ No se encontraron noticias sobre el trending topic.")
    else:
        print("❌ No se pudo obtener un trending topic en español.")

if __name__ == "__main__":
    main()
