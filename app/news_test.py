import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("the-hill","The Hill","Tal Axelrod","Moore: Trump has to be on 'best behavior' for final presidential debate | TheHill - The Hill","Stephen MooreStephen MooreIf the election depends on the economy, the results favor TrumpTrump economic adviser calls president's debate performance 'crappy'Sunday shows - Coronavirus stimulus, Barre… [+2733 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()