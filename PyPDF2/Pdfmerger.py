import PyPDF2


def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)


if __name__ == "__main__":
    # List of PDF files to merge
    pdfs_to_merge = ['cv.pdf', 'cl.pdf']
    output_file_path = 'MuhammadTaha.pdf'  # Output file path

    merge_pdfs(pdfs_to_merge, output_file_path)
    print(f'Merged PDF saved as {output_file_path}')
