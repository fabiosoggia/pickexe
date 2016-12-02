from analyzer import Analyzer

class BaseAnalyzer(Analyzer):

    def get_name(self):
        return "baseanalyzer"

    def support(self, param):
        return True

    def process(self, param):
        print "Can't process param: " + param

    occurences = {}

    def set_occurence(self, term):
        name = self.get_name()
        self.occurences.setdefault(term, {})
        self.occurences[term].setdefault("occurences", {})
        occurences = self.occurences[term]["occurences"].setdefault(name, 0)
        self.occurences[term]["occurences"][name] = occurences + 1
