class Config:
    '''
    General configuration parent class
    '''
    new_api_base_url='http://newsapi.org/v2/top-headlines?api_key={}'

         



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True