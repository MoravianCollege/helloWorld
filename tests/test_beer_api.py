
import unittest
import json
import beer_api


class TestBeerAPI(unittest.TestCase):

    def setUp(self):
        beer_api.app.testing = True
        self.app = beer_api.app.test_client()

    def testRoot(self):
        self.assertEqual({}, json.loads(self.app.get('/').data))