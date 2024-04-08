from unittest import TestCase, main
from project.social_media import SocialMedia

class TestsocialMedia(TestCase):
    allowed_platforms = ['Instagram', 'YouTube', 'Twitter']

    def setUp(self):
        self.sm = SocialMedia("test", "YouTube", 3, "asd" )

    def test_correct_constructor(self):

        self.assertEqual("test", self.sm._username)
        self.assertEqual("YouTube", self.sm._platform)
        self.assertEqual(3, self.sm._followers)
        self.assertEqual("asd", self.sm._content_type)
        self.assertEqual([], self.sm._posts)


    def test_wrong_platform(self):



        with self.assertRaises(ValueError) as ve:
            self.sm.platform = "asd"
            self.assertEqual(f"Platform should be one of {self.allowed_platforms}", str(ve.exception))


    def test_wrong_value_follower(self):

        with self.assertRaises(ValueError) as ve:
            self.sm.followers = -1
            self.assertEqual("Followers cannot be negative.", str(ve.exception))


    def test_create_post(self):


        self.sm.posts = [{'content': "test", 'likes': 0, 'comments': []}]
        self.assertEqual([{'content': "test", 'likes': 0, 'comments': []}], self.sm.posts)