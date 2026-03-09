import pdfplumber

with pdfplumber.open("data/raw_docs/HR_Policy.pdf") as pdf:
    text = ""
    for page in pdf.pages[:2]:
        text += page.extract_text()

print(text[:500])
