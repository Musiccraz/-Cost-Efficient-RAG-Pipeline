from app.rag import RAGPipeline

rag = RAGPipeline()

response = rag.ask(
    "What are the course outcomes?"
)

print("=" * 60)

print(response["answer"])

print()

print("Sources:")

for source in response["sources"]:

    print("-", source)