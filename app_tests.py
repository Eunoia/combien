import os
import app
import unittest
import tempfile
import urllib.parse

class FlaskrTestCase(unittest.TestCase):

  def setUp(self):
    self.app = app.app.test_client()

  def test_hello(self):
    rv = self.app.get('/')
    assert b'Hello World' in rv.data

  def test_price(self):
    url = 'http://www.patagonia.com/us/product/womens-better-sweater-fleece-jacket?p=25542-0'
    encoded_url = urllib.parse.quote(url, safe='~()*!.\'')
    rv = self.app.get('/price/'+encoded_url)
    assert b'139.00' in rv.data

  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()