# Combien

Get the price for the product at a specific URL. 

## GET /price/<url>

### Python 2
```
import urllib
import requests

url = u''
price = requests.get(urllib.quote(s.encode("utf-8"))).text
```

### Python 3
```
import urllib
import requests

url = u''
price = requests.get(urllib.quote(s.encode("utf-8"))).text
```
### Ruby
```ruby
require 'net/http'

url = ''
price = Net::HTTP.get(URI.parse(url)).body
```

### Javascript, with jQuery
$.ajax(

### Node.js with requests






