import os
from flask import Flask
import urllib.parse
from combien import Combien

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/price/<path:url>")
def price(url):
	c = Combien(urllib.parse.unquote(url))
	return c.price()

if __name__ == "__main__":
	app.run(debug=True)
