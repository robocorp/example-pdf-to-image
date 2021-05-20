# Convert PDF files to PNG images

This robot converts [PDF](https://en.wikipedia.org/wiki/PDF) files to [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) images using Python. This is useful when you want to use [OCR (Optical Character Recognition)](https://en.wikipedia.org/wiki/Optical_character_recognition) and image recognition services to extract data from your documents.

There are two example PDF files:

- A single-page `example-invoice.pdf`
- A multipage `example-multipage.pdf`

The `pdf2image` library generates one image per PDF document page:

```bash
example-invoice.pdf-0.png
example-multipage.pdf-0.png
example-multipage.pdf-1.png
example-multipage.pdf-2.png
example-multipage.pdf-3.png
example-multipage.pdf-4.png
example-multipage.pdf-5.png
example-multipage.pdf-6.png
example-multipage.pdf-7.png
example-multipage.pdf-8.png
```

## Dependencies

`conda.yaml`:

```yaml
channels:
  - conda-forge

dependencies:
  - python=3.7.5
  - poppler=21.03.0
  - pdf2image=1.15.1
```

## The robot

`task.py`:

```py
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
```
