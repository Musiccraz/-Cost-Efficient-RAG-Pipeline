from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import(PyPDFLoader,BSHTMLLoader,TextLoader,)

class DocumentLoader:
    def __init__(self, data_path:str):
        self.data_path = Path(data_path)
        print("Searching in:", self.data_path.resolve())



    def load_pdf(self,file_path: Path):
        loader = PyPDFLoader(str(file_path))
        documents = loader.load()

        for doc in documents:
            doc.metadata["source"] = file_path.name
            doc.metadata["file_type"]="pdf"

        return documents


    def load_html(self,file_path:Path):
        loader = BSHTMLLoader(str(file_path))
        documents = loader.load()

        for doc in documents:
            doc.metadata["source"]=file_path.name
            doc.metadata["file_type"]="html"

        return documents


    def load_markdown(self,file_path:Path):
        loader = TextLoader(str(file_path),encoding="utf-8")
        documents =loader.load()


        for doc in documents:
            doc.metadata["source"]=file_path.name
            doc.metadata["file_type"]="markdown"

        return documents


    def  load_documents(self):
        all_documents=[]

        for file_path in self.data_path.rglob("*"):
            if not file_path.is_file():
                continue

            suffix = file_path.suffix.lower()

            if suffix ==".pdf":
                all_documents.extend(self.load_pdf(file_path))

            elif suffix in [".html",".htm"]:
                all_documents.extend(self.load_html(file_path))

            elif suffix in [".md",".markdown"]:
                all_documents.extend(self.load_markdown(file_path)) 


        return all_documents       
    


