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

    def __init__(self,author,title,article_url,image_url,date_published,source):

        self.title=title
        self.author=author       
        self.article_url=article_url
        self.image_url=image_url
        self.date_published=date_published
        self.source=source