from htmlanalyzer import Analyzer as HtmlAnalyzer
import re

class Analyzer(HtmlAnalyzer):

    def get_name(self):
        return "stackoverflow"

    def support(self, url):
        if (url.startswith("http://stackoverflow.com")):
            return True
        if (url.startswith("https://stackoverflow.com")):
            return True
        return False

    def processDocument(self, url, document):
        print "Processing as stackoverflow"
        results = []
        posts = document.find_all("", "post-text")
        text = ""
        for post in posts:
            text = text + " " + post.get_text()
            pass
        text = re.sub(r"\s+", " ", text)
        tokens = text.split(" ")
        for token in tokens:
            token.strip()
            self.set_occurence(token)
        return results
