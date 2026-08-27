from app.retriever import Retriever

retriever = Retriever()

results= retriever.retrieve("what are the course outcome?", k=3)

print("=" * 60)

for i, result in enumerate(results,start=1):
    print(f"Result {i}")

    print(f"=" * 40)
    print(result['text'][:300])
    print()
    print(result["source"])
    print(result["page"])
    print("=" * 60)

    
