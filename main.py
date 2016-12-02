import sys
from bs4 import BeautifulSoup
from core.analyzer import Analyzer
from core.baseanalyzer import BaseAnalyzer
from pluginbase import PluginBase
import sys, inspect



class App:
    plugin_base = None
    plugin_source = None
    plugins_list = None
    base_analyzer = None
    lines = None
    analyzers = []

    def get_entry_class(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                print(obj)
        pass

    def __init__(self):
        self.plugin_base = PluginBase(package='plugins')
        self.plugin_source = self.plugin_base.make_plugin_source(searchpath=['./plugins'])
        self.plugins_list = self.plugin_source.list_plugins()
        self.base_analyzer = BaseAnalyzer()

        filename = "./plugins/plugins.cfg"
        self.lines = [line.rstrip('\n') for line in open(filename)]

        self.analyzers = []
        for analyzer_name in self.lines:
            for plugin_name in self.plugins_list:
                plugin_module = self.plugin_source.load_plugin(plugin_name)
                plugin = plugin_module.Analyzer()
                if (not isinstance(plugin, Analyzer)):
                    continue
                if (plugin.get_name() == analyzer_name):
                    self.analyzers.append(plugin_name)
                    break
        pass

    def processSources(self, sources):
        print "Using this analyzers:"
        print self.analyzers
        results = []
        for param in sources:
            self.processSource(param)
        print BaseAnalyzer.occurences
        pass

    def processSource(self, param):
        processed = False
        results = []
        for plugin_name in self.analyzers:
            plugin_module = self.plugin_source.load_plugin(plugin_name)
            plugin = plugin_module.Analyzer()
            if (plugin.support(param)):
                results = plugin.process(param)
                processed = True
                break
        # Fallback analyzers
        if (not processed):
            results = self.base_analyzer.process(param)
        return results


def main(argv):
    app = App()
    params = [
        "https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python",
        # "https://it.wikipedia.org/wiki/Codice_fiscale",
        "https://en.wikipedia.org/wiki/The_Doors"
    ]
    app.processSources(params)
    pass

if __name__ == "__main__":
    main(sys.argv)
