from abc import ABCMeta

class Analyzer:
    __metaclass__ = ABCMeta

    def get_name(self):
        return ""

    def support(self, param):
        return True

    def process(self, param):
        results = []
        print "Base extractor"
        return results
