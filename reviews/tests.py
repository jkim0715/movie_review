from django.test import TestCase
import json
import requests,pprint
# Create your tests here.
url = f'https://api.themoviedb.org/3/search/movie?api_key=4aa6196c39a63ef5473aa8c1e096c329&language=ko-K&query=%EB%BA%91%EB%B0%98&page=1'
res = requests.get(url).json()
pprint.pprint(res.get("results")[0])