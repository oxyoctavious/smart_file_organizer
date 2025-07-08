📁 **Smart File Organizer**

A simple Python script that automatically organizes files in a folder based on their file type.
Great for cleaning up messy directories like Downloads, Desktop, or Documents.

📌 **Features**

Automatically detects file types by extension

Organizes files into categories like Images, Documents, Videos, etc.

Creates folders if they don't exist

Works with any folder path

Beginner-friendly, clean code

🧠 **Technologies Used**

Python 3.x

os module

shutil module

🗂️ **Supported File Categories**

Category	Extensions

Images	.jpg, .jpeg, .png, .gif

Documents	.pdf, .docx, .txt, .xlsx

Videos	.mp4, .mov, .avi, .mkv

Music	.mp3, .wav, .aac

Archives	.zip, .rar, .tar

Scripts	.py, .js, .cpp, .html

Others	Anything not matched above

▶️ **How to Use**

Clone the repo or download smart.py

Make sure you have a folder with random files (like test_folder)

Open terminal and run:

bash


python smart.py

Your files will be neatly sorted into subfolders inside test_folder.

📝 **Example Output**

mathematica


Moved horse1.jpeg → Images/
Moved vedant.txt → Documents/
Moved LT E-Bill.pdf → Documents/

🔧 Customization

Want to organize a different folder?

Open smart.py and change this line:


folder_to_scan = "test_folder"

to


folder_to_scan = "C:/Users/CSH/Downloads"  # or any path you want


🧑‍💻**Author**

Vedant Vidhate
Beginner Python & AI/ML enthusiast 

Reference - Google

