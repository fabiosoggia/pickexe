from htmlanalyzer import Analyzer as HtmlAnalyzer
import re

class Analyzer(HtmlAnalyzer):

    wiki_patter = None

    def __init__(self):
        self.wiki_patter = re.compile("https?://(.*)wikipedia\.org/wiki/(.+)")
        pass

    def get_name(self):
        return "wikipedia"

    def get_source(self, url):
        params = self.get_wiki_params(url)
        lang = params[0]
        term = params[1]
        url = "https://" + lang + "wikipedia.org/w/index.php?printable=yes&title=" + term
        return url

    def get_wiki_params(self, url):
        result = self.wiki_patter.findall(url)
        if (len(result) == 1):
            return list(result[0])
        return []

    def support(self, url):
        params = self.get_wiki_params(url)
        if (len(params) == 2):
            return True
        return False

    def processDocument(self, url, document):
        print "Processing as wikipedia"
        title = document.title.get_text()
        ptext = ""
        atext = ""
        for p in document.find_all("p"):
            for a in p.find_all("a"):
                atext = atext + " " + a.get_text()
            ptext = ptext + " " + p.get_text()
        text = title + ptext + atext
        tokens = text.split(" ")
        for token in tokens:
            token.strip()
            self.set_occurence(token)
