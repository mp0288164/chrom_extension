# import PyPDF2
# from django.core.files.uploadedfile import UploadedFile

# def parse_document(file: UploadedFile):
#     # Assuming it's a PDF file for this example
#     parsed_data = {}
#     with file.open('rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#         num_pages = pdf_reader.numPages
#         for page_num in range(num_pages):
#             page = pdf_reader.getPage(page_num)
#             parsed_data[f'page_{page_num+1}'] = page.extractText()
#     return parsed_data
