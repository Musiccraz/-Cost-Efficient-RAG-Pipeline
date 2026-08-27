from app.retriever import Retriever
from app.llm import GroqLLM
import time


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.llm = GroqLLM()

    def ask(self, question, k=3):
        total_start = time.perf_counter()

        retrieval_start = time.perf_counter()

        results = self.retriever.retrieve(question, k)

        retrieval_time = time.perf_counter() - retrieval_start

        context = ""

        sources = []

        for result in results:

            context += result["text"] + "\n\n"

            sources.append(
                f'{result["source"]} (Page {result["page"]})'
            )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:

"I couldn't find that information in the provided documents."

Context:

{context}

Question:

{question}
"""

        llm_start = time.perf_counter()

        answer = self.llm.generate(prompt)

        generation_time = time.perf_counter() - llm_start

        total_time = time.perf_counter() - total_start

        return {
            "question": question,
             "answer": answer,
             "sources": sources,
             "retrieved_chunks": len(results),
             "retrieval_time": round(retrieval_time, 3),
             "generation_time": round(generation_time, 3),
             "total_time": round(total_time, 3)
}