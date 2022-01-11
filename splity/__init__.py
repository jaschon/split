#!/usr/bin/env python3
"""
Tools to split/join pdf files
"""

__author__ = "Jason Rebuck"
__copyright__ = "2011-2022"
__version__ = "0.30"

import os
import PyPDF2

def split_pdf(paths):
    """Splits pdf files into separate files."""
    for path in paths:
        if path.endswith(".pdf"):
            try:
                with open(path, 'rb') as file_p:
                    path_root, path_ext = os.path.splitext(os.path.basename(path).replace(" ", "_"))                    
                    new_dir_name = os.path.dirname(path)
                    pdf_read = PyPDF2.PdfFileReader(file_p, False)
                    for page in range(pdf_read.getNumPages()):                        
                        new_path_name = os.path.join(new_dir_name, f"{page+1}{path_ext}")
                        pdf_write = PyPDF2.PdfFileWriter()
                        pdf_write.addPage(pdf_read.getPage(page))
                        with open(new_path_name, 'wb') as file_write:
                            pdf_write.write(file_write)
            except (OSError, PyPDF2.utils.PdfReadError) as e:
                print(f"• {e}")

def join_pdf(paths):
    """Joins pdf file list to a single file."""
    pdf_merger = PyPDF2.PdfFileMerger(False)
    try:
        new_file_name = os.path.join(os.path.dirname(paths[0]), "combo.pdf")
        for path in paths:
            path = os.path.abspath(path)
            if path.endswith(".pdf") and path != new_file_name:
                pdf_merger.append(path)
        pdf_merger.write(new_file_name)
    except (OSError, PyPDF2.utils.PdfReadError) as e:
        print(f"• {e}")
    finally:
        pdf_merger.close()

if __name__ == "__main__":
    pass
