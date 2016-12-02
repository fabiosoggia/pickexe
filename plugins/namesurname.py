from core.baseanalyzer import BaseAnalyzer

class Analyzer(BaseAnalyzer):

    def get_name(self):
        return "namesurname"

    def support(self, url):
        if (url.startswith("namesurname:")):
            return True
        return False

    def process(self, param):
        print "Processing as namesurname"
