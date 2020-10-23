class Source:
    '''
    News class to define News Objects
    '''
    def __init__(self, id, name,description):
        self.id=id
        self.name=name
        self.desc=description



class Article:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,image_url,article_url,source):

        self.title=title       
        self.author=author 
        self.image_url=image_url      
        self.article_url=article_url
        self.source=source