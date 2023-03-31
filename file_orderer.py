#To make this code work, you should create folders for each file type in the path that you want to work on to move the files.
import os, shutil
path = #enter the path between '' that you want to order your files. For example: C:/users/yourusername/Downloads'
os.chdir(path) #you can delete this line if you run your code directly in the path that you want to work on. 
direction = os.listdir(path)
for file in direction:
    fileToMove = os.path.splitext(file)
    if(fileToMove[1] == '.jpg' or fileToMove[1] == '.png' or fileToMove[1] == '.jpeg'):
        shutil.move(file, #path of the folder that you want to move your file. for example: ("C:/users/yourusername/Downloads/images"))
    elif(fileToMove[1] == '.pdf'):
        shutil.move(file, #path of the folder that you want to move your file.)
    elif(fileToMove[1] == '.docx' or fileToMove[1] == '.doc'):
        shutil.move(file, #path of the folder that you want to move your file.)
    elif(fileToMove[1] == '.ppt' or fileToMove[1] == '.pptx'):
        shutil.move(file, #path of the folder that you want to move your file.)
    elif(fileToMove[1] == '.mp3' or fileToMove[1] == '.wav'):
        shutil.move(file, #path of the folder that you want to move your file.)
    elif(fileToMove[1] == '.exe'):
        shutil.move(file, #path of the folder that you want to move your file.)
    elif(fileToMove[1] == '.zip' or fileToMove[1] == '.rar' or fileToMove[1] == '.7z'):
        shutil.move(file, #path of the folder that you want to move your file.)
    #you can add more file types if you want.  
