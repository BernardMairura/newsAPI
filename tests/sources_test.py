import unittest
from app.models import Source ,Article




class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.new_article = Article('dummy_article','john doe','https://s.image.com',"http://abc.com",'abc-news')

    def test_instance(self):
        print(self.new_source.__class__)
        self.assertTrue(isinstance(self.new_source,Source))
    
    def test_article_instance(self):
        print(self.new_article.__class__)
        self.assertTrue((isinstance(self.new_article,Article)))


