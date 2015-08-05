import requests
from bs4 import BeautifulSoup

class Combien:
	def __init__(self, url):
		r = requests.get(url)
		self.soup = BeautifulSoup(r.text, 'html.parser')

	def get_og_tag(self, og_tag):
		return [meta.attrs['content'] for meta in self.soup.find_all("meta") if 'property' in meta.attrs and meta['property']==og_tag][0]	
	def price(self):
		return self.get_og_tag('product:price:amount')
	def currency(self):
		return self.get_og_tag('product:price:currency')
