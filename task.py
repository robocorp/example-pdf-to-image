from pdf2image import convert_from_path


def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    for index, image in enumerate(images):
        image.save(f'output/{pdf_path}-{index}.png')


def task():
    convert_pdf_to_images('example-invoice.pdf')
    convert_pdf_to_images('example-multipage.pdf')


if __name__ == "__main__":
    task()
