from pdf2docx import Converter

pdf_file = "Введите файл с конвертацией - .pdf"
docx_file = "Введите путь для файла где хотите сохранить переконвертацию - .docx"

# convert pdf to docx.
cv = Converter(pdf_file)

# all pages by default.
cv.convert(docx_file)
cv.close