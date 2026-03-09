def check(lib_name, import_stmt):
    try:
        exec(import_stmt)
        print(f"[OK] {lib_name}")
    except Exception as e:
        print(f"[FAIL] {lib_name} -> {e}")


print("=== Environment Library Check ===\n")

check("fastapi", "import fastapi")
check("uvicorn", "import uvicorn")

check("sentence-transformers", "from sentence_transformers import SentenceTransformer")

check("faiss-cpu", "import faiss")

check("pydantic", "import pydantic")

check("python-multipart", "import multipart")

check("pdfplumber", "import pdfplumber")
check("pymupdf", "import fitz")

check("bcrypt", "import bcrypt")
check("python-jose", "from jose import jwt")

check("nltk", "import nltk")
check("spacy", "import spacy")

print("\n=== Test Complete ===")
