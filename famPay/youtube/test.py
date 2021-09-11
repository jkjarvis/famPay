# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python




import requests
import json



url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=cricket&key=AIzaSyB5Kr212duSycZJWM-zXg5A_7tDV-CquIg'

response = requests.get(url)

response = response.json()['items'][0]['snippet']

print(response['thumbnails'])

for i in response['thumbnails'].values():
    print(i['url'])
