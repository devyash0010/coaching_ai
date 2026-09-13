from retriever import Retriever

class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()

    def ask(self, question):

        results = self.retriever.search(question)

        return results