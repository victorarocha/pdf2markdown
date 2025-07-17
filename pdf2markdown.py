"""
pdf2markdown.py

Author: Victor Arocha
Description: 
    This script converts all PDF files in a specified input folder to Markdown (.md) files 
    using the pymupdf4llm library. The converted Markdown files are saved in a specified 
    output folder. The script can be run from the command line with the following usage:

        python pdf2md.py <input_folder> <output_folder>

Functions:
    pdf_to_markdown(pdf_path):
        Converts a PDF file at the given path to Markdown text using pymupdf4llm.

    main():
        Parses command-line arguments for input and output folders, processes all PDF files 
        in the input folder, converts them to Markdown, and saves the results in the output folder.

Usage:
    python pdf2md.py <input_folder> <output_folder>

Dependencies:
    - pymupdf4llm
    - Python standard libraries: sys, os, pathlib
"""
import sys
import os
import pymupdf4llm
import pathlib


def pdf_to_markdown(pdf_path):
    md_text = pymupdf4llm.to_markdown(pdf_path)
    return md_text

def main():
    if len(sys.argv) < 3:
        print("Usage: python pdf2md.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            md_text = pdf_to_markdown(pdf_path)
            md_filename = os.path.splitext(filename)[0] + ".md"
            md_path = os.path.join(output_folder, md_filename)
            pathlib.Path(md_path).write_bytes(md_text.encode())
            print(f"Converted {filename} to {md_filename}")

if __name__ == "__main__":
    main()



