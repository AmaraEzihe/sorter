import os
import shutil
from pathlib import Path
from datetime import datetime

print("Welcome to Sorter")
pathsource = input("Enter the Folder Name eg Downloads\n")
sourcefolder=f"C:/path/path/{pathsource}"
path = Path(sourcefolder)
listoftypes = []
try:
 countfile = 0       
 countdir =0
 print(f"Files and their types in '{sourcefolder}':")
 print(f"Started process at {datetime.now()}\n\n\n")
 for file in path.iterdir():
         if file.is_dir():
             countdir +=1
         elif file.is_file():
         
             file_extension = file.suffix.lower() # Get the extension and convert to lowercase
             
             if file_extension:
                                
                 if file_extension in listoftypes:
                      pass
                 else:
                     listoftypes.append(file_extension) 
                     for extension in listoftypes:
                        
                        withdot = extension
                        typeoffile = extension[1:].upper()
                        destinationfolder = f"{sourcefolder}/{typeoffile}"
                        if not os.path.exists(destinationfolder):
                             os.makedirs(destinationfolder)
                             print(f"Creating folder: {destinationfolder}")
                        for filename in os.listdir(sourcefolder):
                             #eg C:/path/path/Downloads/egg.extension for all files basically in the source folder, we move from source path to destination path
                             #file must be joined to a path
                             sourcepath= os.path.join(sourcefolder,filename)
                             if os.path.isfile(sourcepath) and filename.endswith(withdot):
                                  countfile+=1
                                  destinationpath = os.path.join(destinationfolder,filename)
                                  shutil.move(sourcepath,destinationpath)
                     print(f"Moving {countfile} {typeoffile}s files")
                     print(f"Movement Completed")
             else:
                 print(f"This file extension is unknown")
            
         
 print(f"You have {countdir} directories in this path\n\n\n")
 print(f"Ended Process at {datetime.now()}")
 
except FileNotFoundError:
     print(f"Error: '{sourcefolder}' is not a valid directory.")

except Exception as e:
     print(f"Something went wrong: {e}")
