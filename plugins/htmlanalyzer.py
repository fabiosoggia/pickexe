from core.baseanalyzer import BaseAnalyzer
from bs4 import BeautifulSoup
import re
import urllib2

class Analyzer(BaseAnalyzer):

    def get_name(self):
        return "htmlanalyzer"

    def is_valid(self, url, qualifying=None):
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return bool(regex.match(url))

    def get_source(self, url):
        return url

    def support(self, param):
        return self.is_valid(param)

    def process(self, url):
        url = self.get_source(url)
        html_doc = urllib2.urlopen(url).read()
        document = BeautifulSoup(html_doc, 'html.parser')
        self.processDocument(url, document)
        pass

    def processDocument(self, url, document):
        print "Processing as HTML page"
        pass
