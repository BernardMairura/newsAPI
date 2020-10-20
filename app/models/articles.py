class Articles:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,published_at,url,url_to_image):
        self.author=author
        self.title=title
        self.description=description
        self.published_at=published_at
        self.url=url
        self.url_to_image=url_to_image
        