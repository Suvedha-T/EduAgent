from tools.pdf_tool import extract_pdf_text

text = extract_pdf_text("sample.pdf")

print(text[:1000])