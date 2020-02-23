# Text_Reader
Simple python script for reading text from images using pytessaract.

## Installation and Requirements
pytessaract should be installed. Follow the below steps if not. 

#### On Linux

sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev

#### On Mac

brew install tesseract

#### On Windows

download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.
