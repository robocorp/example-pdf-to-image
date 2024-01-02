# Convert PDF files to PNG images

This robot converts [PDF](https://en.wikipedia.org/wiki/PDF) files to [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) images using Python. This is useful when you want to use [OCR (Optical Character Recognition)](https://en.wikipedia.org/wiki/Optical_character_recognition) and image recognition services to extract data from your documents.

👉 Using the `robocorp` -library `@task` -decorator gives automatic log.html for the execution 

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
