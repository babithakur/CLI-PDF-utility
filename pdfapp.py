import pyfiglet
from pypdf import PdfReader, PdfWriter

class PdfApp:
    def merge_pdf(self):
        merger = PdfWriter()
        no_of_pdfs = int(input("Enter the number of pdfs to merge: "))
        if no_of_pdfs <= 1:
            print(f"Can\'t merge {no_of_pdfs} pdf!")
            exit()
        pdfs = []
        out_file = input("Enter the output filename: ")
        for i in range(no_of_pdfs):
            pdfs.append(input(f"Enter pdf path {i+1}: "))
        for pdf in pdfs:
            try:
                merger.append(pdf)
            except FileNotFoundError:
                print("File not found!")
                exit()
        merger.write(out_file)
        merger.close()
        print("Pdf merged successfully!")

    def extract_Text(self):
        pdf_file = input("Enter the pdf filename to extract text: ")
        output_txtfile = input("Enter the output text filename: ")
        try:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                with open(output_txtfile, 'a') as f:
                    f.write(page.extract_text())
            print("Extracted text successfully!")
        except FileNotFoundError:
            print("File not found!")
            exit()

    def extract_images(self):
        pdf_file = input("Enter the pdf filename to extract images: ")
        try:
            reader = PdfReader(pdf_file)
            count = 1
            page = reader.pages[0]
            for image in page.images:
                with open(str(count)+image.name, "wb") as f:
                    f.write(image.data)
                    count += 1
            print("Images extracted successfully")
        except FileNotFoundError:
            print("File not found!")
            exit()

    def encrypt_pdf(self):
        pdf_file = input("Enter th pdf filename to encrypt: ")
        password = input("Enter the password to encrypt: ")
        try:
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            with open(f"encrypted-{pdf_file.split('/')[-1]}", "wb") as f:
                writer.write(f)
            print("Pdf file encrypted successfully!")
        except FileNotFoundError:
            print("File not found!")
            exit()


if __name__ == '__main__':
    banner = pyfiglet.figlet_format("CLI Pdf Utility", font="slant")
    print(banner)
    print("[1]. Merge pdf\n[2]. Extract text\n[3]. Extract images\n[4]. Encrypt pdf\n[5]. Exit")
    pdfapp = PdfApp()
    try:
        choice = int(input("[+]. Enter your choice: "))
    except ValueError:
        print("Invalid Choice: Value Error!")
        exit()
    if choice == 1:
        pdfapp.merge_pdf()
    elif choice == 2:
        pdfapp.extract_Text()
    elif choice == 3:
        pdfapp.extract_images()
    elif choice == 4:
        pdfapp.encrypt_pdf()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice!")
