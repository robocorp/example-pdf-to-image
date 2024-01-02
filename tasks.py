from robocorp.tasks import task
from pdf2image import convert_from_path


def convert_pdf_to_images(pdf_path):
    """
    Handles single or multipaged PDFs to PNG images using 'pdf2image' -library
    The result images are placed in the output -folder
    """
    images = convert_from_path(pdf_path)
    for index, image in enumerate(images):
        image.save(f'output/{pdf_path}-{index}.png')


@task
def task():
    """
    Converting PDF files to image is usefull in OCR cases.
    """
    convert_pdf_to_images('example-invoice.pdf')
    convert_pdf_to_images('example-multipage.pdf')
