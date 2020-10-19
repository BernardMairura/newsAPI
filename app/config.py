class Config:
    '''
    General configuration parent class
    '''
    new_api_base_url='https://newsapi.org/v2/sources?apiKey={}'
    
    

         



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True