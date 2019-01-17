import urllib.request
import urllib.parse

fusion_fall_url = urllib.request.urlopen('http://fusionfall.wikia.com/wiki/Missions')

print(fusion_fall_url.read())


url = 'http://fusionfall.wikia.com/wiki/Missions'
values = {'s':'Missions', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)


try:
	fusion_fall_url = urllib.request.urlopen('http://fusionfall.wikia.com/wiki/Missions')
	print (fusion_fall_url.read())

except Exception as e:
	print(str(e))



try:
	url = 'http://fusionfall.wikia.com/wiki/Missions'

	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
	req = urllib.request.Request(url, headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	saveFile = open('python_web_text_files/withHeaders.text', 'w')
	saveFile.write(str(respData))
	saveFile.close()

except Exception as e:
	print(str(e))
