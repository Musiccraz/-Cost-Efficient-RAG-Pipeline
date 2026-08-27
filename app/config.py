from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("LLM_MODEL")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE",500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP",100))

TOP_K = int(os.getenv("TOP_K",5))

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
TABLE_NAME = os.getenv("TABLE_NAME")

print("VECTOR_DB_PATH =", VECTOR_DB_PATH)