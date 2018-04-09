import urllib,json
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=&limit=5").read())
print json.dumps(data, sort_keys=True, indent=4)
