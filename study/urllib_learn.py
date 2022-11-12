# fundamental http request implement
import urllib.request
# exception
import urllib.error
# url parse
import urllib.parse
# parse robots.text file, Determining whether a website can crawl information
import urllib.robotparser

'''
* urlopen
* @description:  Used to implement basic http requests and receive return data from the server
* @params:
    url: web url
    data:  request method, default is GET
    timeout: /s
    cafile/capath CA certification file and path
    cadefault: CA certification default value
    context: SSL options
* @return:
    response
'''
url = "https://www.python.org/"
response = urllib.request.urlopen(url)
print(type(response))
print('status: ', response.status)
print('headers: ', response.getheaders())
print('\n\n')
print('html:', response.read().decode('utf-8'))


# post
url = "https://www.httpbin.org/post"
data = bytes(urllib.parse.urlencode({'hello':'python'}), encoding = 'utf-8')
response = urllib.request.urlopen(url, data)
print(response.read().decode('utf-8'))