from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=1144cdf8e1a2dab59dbca2112342e131&targetDt=20120101'
    print(requests)
    response = requests.get(url).json()
    return ''

