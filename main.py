# Importing required libraries: pyttsx3 for text-to-speech conversion and PyPDF2 for reading PDF files
import pyttsx3 
import PyPDF2 

# Open the 'oop.pdf' file in read-binary mode
book = open('oop.pdf', 'rb')

# Create a PdfFileReader object to read the PDF file
pdfReader = PyPDF2.PdfFileReader(book)

# Get the number of pages in the PDF file
pages = pdfReader.numPages

# Print the number of pages in the PDF file
print(pages)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Loop through the pages of the PDF file from page 7 to the last page
for num in range(7, pages):
   
   # Get the page object for the current page number
   page = pdfReader.getPage(num)

   # Extract the text from the current page object
   text = page.extractText()

   # Use the text-to-speech engine to narrate the extracted text
   speaker.say(text)

   # Run the text-to-speech engine and wait for it to complete before moving on to the next page
   speaker.runAndWait() 

# Close the PDF file
book.close()
