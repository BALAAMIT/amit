from pypdf import pdfwriter
import os
 

marger = pdfwriter()
file = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in file:
    marger.append(pdf)
marger.write("meerged-pdf.pdf")
marger.close()