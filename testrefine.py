from refinedoc.refined_document import RefinedDocument
from pypdf import PdfReader

# Build the document from a PDF file
reader = PdfReader("Semanario_Judicial_Abril_2011_part_16.pdf")
document = []
for page in reader.pages:
    document.append(page.extract_text().split("\n"))
    
rd = RefinedDocument(content=document)
headers = rd.headers
# [["header 1", "subheader 1"], ["header 2", "subheader 2"], ["header 3", "subheader 3"], ["header 4", "subheader 4"]]
footers = rd.footers
# [["footer 1"], ["footer 2"], ["footer 3"], ["footer 4"]]
body = rd.body
# [["lorem ipsum dolor sit amet", "consectetur adipiscing elit"], ["sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"], ["ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"], ["duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur"]]

body_text = "\n".join(["\n".join(section) for section in body])

print("Headers:", headers)
print("Footers:", footers)
print("Body:", body_text)

