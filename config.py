import os

class Config:
    """
    General configuration parent class
    """
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/watchlist'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI ="postgresql://iwweauxgkbdujj:9a2016aade37089bb62e3eca3428f22c45306041d10515ebd6651fef95745599@ec2-18-206-20-102.compute-1.amazonaws.com:5432/dd3e8ev6v5t6qr?sslmode=require"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/watchlist_test'

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config :The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/watchlist'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}


# aec9bb89058643fa9ce5d16218cb0c8b


# # https://newsapi.org/v2/everything?q=tesla&from=2021-03-18&sortBy=publishedAt&apiKey=aec9bb89058643fa9ce5d16218cb0c8b
# https://newsapi.org/v2/everything&apiKey=aec9bb89058643fa9ce5d16218cb0c8b
