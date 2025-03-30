from abc import abstractmethod

from plugin import Plugin


class EvidenceCollectionPlugin(Plugin):
    @abstractmethod
    def connectivity_test(self):
        pass

    @abstractmethod
    def collect_evidence(self):
        pass

    @abstractmethod
    def log_error(self, error):
        pass

    def run(self):
        if self.connectivity_test():
            self.collect_evidence()
        else:
            self.log_error("Connectivity test failed.")
