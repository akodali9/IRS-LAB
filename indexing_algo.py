#Task 3

class Index_algo:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, content, documents):
        words = content.split()
        documents.append(words)

    def search(self, query, documents):
        for sub_doc in documents:
            if query in sub_doc:
                doc_index, quer_index = documents.index(
                    sub_doc), sub_doc.index(query)
                print(
                    f"Document '{' '.join(documents[doc_index])}' contains '{query}' at position[{quer_index}]")

index = Index_algo()
documents = []
for i in range(int(input("Enter No of documents: "))):
    index.add_document(doc_id=i, documents=documents, content=input("Enter: "))

index.search(query=input("Enter tokens: "), documents=documents)
