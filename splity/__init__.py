#!/usr/bin/env python3
"""
Tools to split/join pdf files
"""

__author__ = "Jason Rebuck"
__copyright__ = "2011-2023"
__version__ = "0.38"

import os
import PyPDF2
import uuid
import re

def make_dir(path, extra=""):
    """Make a unique folder"""
    root, ext =  os.path.splitext(re.sub('[^0-9a-zA-Z\.]+', '_', os.path.basename(path)))                    
    folder = os.path.join(os.path.dirname(path), extra, root)
    folder = f'{folder}_{str(uuid.uuid4())[:6]}' if os.path.isdir(folder) else folder
    os.makedirs(folder)
    return folder

def split_pdf(paths, fill=3):
    """Splits pdf files into separate files."""
    for path in paths:
        if path.endswith(".pdf"):
            try:
                with open(path, 'rb') as file_p:
                    folder = make_dir(path, "split")
                    pdf_read = PyPDF2.PdfFileReader(file_p, False)
                    for page in range(pdf_read.getNumPages()):                        
                        file_name = os.path.join(folder, f"{page+1:0{fill}}.pdf")
                        pdf_write = PyPDF2.PdfFileWriter()
                        pdf_write.addPage(pdf_read.getPage(page))
                        with open(file_name, 'wb') as file_write:
                            pdf_write.write(file_write)
            except (OSError, PyPDF2.utils.PdfReadError) as e:
                print(f"• {e}")

def join_pdf(paths):
    """Joins pdf file list to a single file."""
    pdf_merger = PyPDF2.PdfFileMerger(False)
    try:
        file_name = os.path.join(make_dir(paths[0], "join"), f"combined.pdf")
        for path in paths:
            path = os.path.abspath(path)
            try:
                pdf_merger.append(path)
            except (OSError, PyPDF2.utils.PdfReadError) as e:
                print(f"• {e}")
        pdf_merger.write(file_name)
    except (OSError, PyPDF2.utils.PdfReadError) as e:
        print(f"• {e}")
    finally:
        pdf_merger.close()

if __name__ == "__main__":
    pass
