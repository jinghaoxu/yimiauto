from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

readfile = 'C:\\Users\\suMs\\Desktop\\2018中国影视童星大赛手册.pdf'
readfile2 = 'C:\\Users\\suMs\\Desktop\\1.pdf'

pdffilereader = PdfFileReader(open(readfile, 'rb'))
pdf2 = PdfFileReader(open(readfile2, 'rb'))

print(pdffilereader.getDocumentInfo())
print(pdffilereader.getNumPages())

pdfout = PdfFileWriter()

pc = pdffilereader.getNumPages()

for i in range(0, pc - 1):
    pdfout.addPage(pdffilereader.getPage(i))
pdfout.addPage(pdf2.getPage(0))
pdfout.write(open('C:\\Users\\suMs\\Desktop\\2018中国影视童星大赛手册2.pdf', 'wb'))
