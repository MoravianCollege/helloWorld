
import unittest
import json
import beerapi


class TestBeerAPI(unittest.TestCase):

    def setUp(self):
        beerapi.app.testing = True
        self.app = beerapi.app.test_client()

    def testRoot(self):
        self.assertEqual({}, json.loads(self.app.get('/').data.decode()))