import fitz

# Open the PDF file in read-binary mode
with open('locked_file.pdf', 'rb') as file:
    # Create a PdfFileReader object
    reader = fitz.open(stream=file.read(), filetype="pdf")

    # Check if the file is encrypted
    if reader.isEncrypted:
        # Enter the password to unlock the file
        password = input('Enter the password: ')

        # Try to decrypt the file with the password
        if reader.authenticate(password):
            print('File successfully unlocked.')

            # Create a new PDF file with the unlocked content
            writer = fitz.open()

            # Copy the pages from the original PDF file to the new PDF file
            for page in reader:
                writer.insert_pdf(reader, from_page=page.number, to_page=page.number)

            # Write the new PDF file to disk
            writer.save('unlocked_file.pdf')

            print('New file saved as "unlocked_file.pdf".')
        else:
            print('Incorrect password.')
    else:
        print('File is not encrypted.')