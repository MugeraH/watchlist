import os

class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/watchlist'


class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config :The parent configuration class with General configuration settings
    """
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}


# aec9bb89058643fa9ce5d16218cb0c8b


# # https://newsapi.org/v2/everything?q=tesla&from=2021-03-18&sortBy=publishedAt&apiKey=aec9bb89058643fa9ce5d16218cb0c8b
# https://newsapi.org/v2/everything&apiKey=aec9bb89058643fa9ce5d16218cb0c8b
