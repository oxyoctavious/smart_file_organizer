import os

def list_files(directory):
    """Found file: horse1.jpeg
    Found file: human 1.jpeg
    Found file: human2.jpeg
    Found file: LT E-Bill.pdf
    Found file: vedant.txt
    Found file: zebra.jpeg"""     
    
    def get_folder_for_file(filename):
        """Images
        Documents"""
    
        extension= os.path.splitext(filename)[1].lower()
    
        FILE_TYPE_MAP= {
            "Images": [".jpg",".jepg",".png",".gif"],
            "Documents": [".pdf",".docx",".txt",".xlsx"],
            "Videos": [".mp4",".mov",".avi",".mkv"],
            "Music": [".mp3",".wav",".aac"],
            "Archives": [".zip",".rar",".tar"],
            "Scripts": [".py",".js",".cpp",".html"],
        
    }
    
    
    for folder_name, extension in FILE_TYPE_MAP.items():
        if ext in extensions:
            return folder_name
        
        return "others"
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            target =get_folder_for_file(filename)
            print(f"{filename}-> {filename}")
            
            
if __name__ == "__main__":
    folder_to_scan = "test_folder"
    list_files(folder_to_scan)    

            
            
            
