import unittest
from app.models import Review,User
from app import db

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Mugera = User(username = 'Mugera',password = 'chicken', email = 'Mugera@ms.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_Mugera )
   
        # self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
        
    def tearDown(self):
        Review.query.delete()
        User.query.delete()
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_Mugera)
        
    # We then create a test for our save review method. We also query the database to confirm that we actually have data saved.
    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)
        
    #We then test the get_reviews class method that we pass in the id of a movie and get a response which is a review for that movie.
    def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)

 
