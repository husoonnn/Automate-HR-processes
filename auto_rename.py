from distutils import text_file
import re
import csv
import os
from os import walk
from pathlib import *
import glob
from PyPDF3 import PdfFileReader


pdf_files = glob.glob("*.pdf")
print(pdf_files)

for pdffile in pdf_files:
    with open(pdffile, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        pageObj = pdf.getPage(0)
        txt = pageObj.extractText()
        pos1 = re.search("Dear", txt)
        pos2 = re.search("Advance", txt)
        pos1 = pos1.end()
        pos2 = pos2.start()
        text = txt[pos1:pos2]
        print(text)
        new = []
        for i in text:
            if i.isalpha() or i == " ":
                new.append(i)
        new.pop()
        new.remove(new[0])
        for i in new:
            if new[-1] == ' ':
                new.pop()
        print(new)
        new.append(".pdf")
        new = ''.join(new)
        print(new)
        f.close()
    os.rename(pdffile, new)
        
        
    
        
