import unittest
from models import sources

Source = sources.Source




class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('bbc-news','BBC News',"The oil giant distances itself from the President's \"hypothetical\" funds-for-contracts claim.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()