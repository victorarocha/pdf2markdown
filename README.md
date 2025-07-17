<p align="center">
  <img src="assets/logo.png" alt="PDF to Markdown Logo" width="150">
</p>

# 📝 PDF to Markdown Converter

🔄 A handy Python script to convert all your 📄 PDF files into 🧠 LLM-friendly Markdown files using the powerful `pymupdf4llm` library.

## ✨ Features

- 📂 Batch conversion of PDFs in a folder
- 🔧 Simple command-line usage
- ⚡ Fast and lightweight
- 🧠 LLM-ready Markdown formatting

## 🚀 Usage

Run the script from the command line:

```bash
python pdf2md.py <input_folder> <output_folder>
```

📁 `<input_folder>`: Path to the folder containing PDF files to convert  
📁 `<output_folder>`: Path where converted `.md` files will be saved

### Example

```bash
python pdf2md.py ./pdfs ./markdowns
```

## 🧩 Functions

### `pdf_to_markdown(pdf_path)`
Converts a single PDF file to Markdown using `pymupdf4llm`.

### `main()`
- Parses CLI arguments
- Scans input folder for `.pdf` files
- Converts each PDF to Markdown
- Saves the output in the specified folder

## 📦 Dependencies

- [`pymupdf4llm`](https://pypi.org/project/pymupdf4llm/)
- Python Standard Libraries:
  - `sys`
  - `os`
  - `pathlib`

Install the main dependency with:

```bash
pip install pymupdf4llm
```

## 🪪 License

This project is licensed under the MIT License.

---

🤝 Feel free to contribute, report bugs, or suggest improvements!
