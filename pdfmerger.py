from PyPDF2 import PdfFileMerger
from natsort import natsorted
import os

path = input("Enter path: ") 
file_name = input("Enter file name: ")

os.chdir(r'{}'.format(path)) # change current directory to inserted directory
pdflist = [a for a in os.listdir() if a.endswith(".pdf")] # check all files with pdf extension
pdflist.sort(key=lambda x: '{0:0>8}'.format(x).lower()) # sort all files name
merger = PdfFileMerger()
pdflist = natsorted(pdflist)
print(pdflist)

# merge all pdf files
for pdf in pdflist: 
    merger.append(open(pdf, 'rb'))

# name the merged pdf files according to inserted name
with open(f"{file_name}.pdf", "wb") as merge_pdf:
    merger.write(merge_pdf)
    print("done")
