import urllib
import requests


class MyCrawl():

    def getHtmlUrllib(self,url, params, headers):
        '''
        https
        :param url:
        :param params:
        :param headers:
        :return:
        '''
        data = urllib.parse.urlencode(params).encode(encoding='utf8')
        req = urllib.request.Request(url, data, headers)
        # req = request.Request(url+"?"+data)  # GET方法
        response = urllib.request.urlopen(req)

        the_page = response.read()
        #html = the_page.decode("utf8")
        return the_page

    def getHtmlReqWithWords(self, url, words, headers=None):
        data = urllib.parse.quote(words)
        the_page = self.getHtmlReq(url + '/' + data, words, headers)
        html = the_page.decode("utf8")
        return html

    def getHtmlReq(self, url, headers=None, params=None):
        response = requests.get(url=url, headers=headers, params=params)
        the_page = response.content
        #        html = the_page.decode("utf8")
        return the_page

    def getHtlPost(self, url, headers=None, params=None, isJson=True):
        if isJson:
            response = requests.post(url=url, json=params, headers=headers)
        else:
            response = requests.post(url=url, data=params, headers=headers)
        the_page = response.content
        # html = the_page.decode("utf8")
        return the_page

    def toJson(self, content):
        '''
        to json
        :param content:
        :return:
        '''
        import json
        json = json.loads(content)
        return json
    pass