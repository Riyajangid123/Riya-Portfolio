import PyPDF2

with open('Riya_Jangid_Resume.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    links = []
    for page in reader.pages:
        text += page.extract_text()
        if '/Annots' in page:
            for annot in page['/Annots']:
                annot_obj = annot.get_object()
                if annot_obj.get('/Subtype') == '/Link':
                    link = annot_obj.get('/A', {}).get('/URI')
                    if link:
                        links.append(link)

print("Text:")
print(text)
print("\nLinks:")
for link in links:
    print(link)