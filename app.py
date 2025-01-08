import tweepy

# Autenticación con la API de X
consumer_key = 'w8ukKuTY9b3to0MhnVNduUtsi'
consumer_secret = '9Z0xa40IaSzW1yh9EqsXz34luGlzEsHZUiHrrifcrE2EBnfKEq'
access_token = '1864752692347764737-qXD0JnySg2hDdEpR5me2Ged1DD4dA0'
access_token_secret = 'bgHGjBRuH9bb7KmLGeqh0SN4hzLFuvlGanlFr4gTMt3qD'

# Configurando la autenticación
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creando una instancia de API
api = tweepy.API(auth)

try:
    # Publicar un tweet
    api.update_status("Hola, este es mi primer tweet usando Tweepy en Python!")
    print("Tweet publicado exitosamente!")
except Exception as e:
    print(f"Ocurrió un error: {e}")

