import os
import shutil

def list_files(directory):
    """Found file: horse1.jpeg
    Found file: human 1.jpeg
    Found file: human2.jpeg
    Found file: LT E-Bill.pdf
    Found file: vedant.txt
    Found file: zebra.jpeg"""   
    
               
    
    def get_folder_for_file(filename):
        """
        Found folder: Images
        Found folder: Documents
        """
    
        extension = os.path.splitext(filename)[1].lower()
    
        FILE_TYPE_MAP= {
            "Images": [".jpg",".jpeg",".png",".gif"],
            "Documents": [".pdf",".docx",".txt",".xlsx"],
            "Videos": [".mp4",".mov",".avi",".mkv"],
            "Music": [".mp3",".wav",".aac"],
            "Archives": [".zip",".rar",".tar"],
            "Scripts": [".py",".js",".cpp",".html"],
        } 
        ext = os.path.splitext(filename)[1].lower() 
        for folder_name, extension in FILE_TYPE_MAP.items():
            if ext in extension:
                return folder_name
        
        return "others"
    
    for filename in os.listdir(directory):
        file_path = os.path .join(directory, filename)
        
        if os.path.isfile(file_path):
            target_folder= get_folder_for_file(filename)
            target_folder_path= os.path.join(directory, target_folder)
            
            #Creat folder if it does not exist
            
            os.makedirs(target_folder_path, exist_ok=True)
            
            #Builds full destination path
            destination_path= os.path.join(target_folder_path, filename)
            
            #Moves the file in
            shutil.move(file_path, destination_path) 
            print(f"Moved {filename}--> {target_folder}")  
    
    
    
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            target = get_folder_for_file(filename)
            print(f"{filename} --> {target}")
            
            
if __name__ == "__main__":
    folder_to_scan = "test_folder"
    list_files(folder_to_scan)    

            
            
            
