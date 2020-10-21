class Source:
    '''
    News class to define News Objects
    '''
    def __init__(self, id, name,description):
        self.id=id
        self.name=name
        self.description=description



class Articles:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,published_at,url,url_to_image,source):

        self.title=title
        self.author=author       
        self.description=description
        self.published_at=published_at
        self.url=url
        self.url_to_image=url_to_image
        self.source=source