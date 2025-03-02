import os
import pypdf

files = os.listdir("files/")
files = [f for f in files if f.endswith(".pdf")]
files.sort()

folder = "files/"

search = "KAROLINA"

print(f"Buscando por: {search}")
results = []

for file in files:
    filepath = os.path.join(folder, file)

    with open(filepath, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)

        found = False
        results = []

        for page_num in range(len(reader.pages)):
            page = reader.get_page(page_num)
            text = page.extract_text()

            if search in text:
                found = True
                print(f"Found '{search}' on page {page_num} of {file}")
                results.append(file)
                break

if found:
    print(f"We found {search} in:")
    for result in results:
                print(result)
