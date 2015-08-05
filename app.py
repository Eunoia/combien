import os
from flask import Flask
import urllib.parse
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/price/<path:url>")
def price(url):
	r = requests.get(urllib.parse.unquote(url))
	soup = BeautifulSoup(r.text, 'html.parser')
	return [meta.attrs['content'] for meta in soup.find_all("meta") if 'property' in meta.attrs and meta['property']=='product:price:amount'][0]

if __name__ == "__main__":
	app.run(debug=True)
