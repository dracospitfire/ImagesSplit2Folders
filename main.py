from pathlib import Path

### Choose how many images you want per folder ###
MAX_IMAGES_PER_FOLDER = 1000

jpgFolderDirectory = Path('YOUR_FOLDER_DIRECTORY_WITH_ALL_YOUR_IMAGES')
### Find all .jpg files in directory ###
jpgFolder = jpgFolderDirectory.glob('*.jpg')

def check_directory(folder_num, count, jpgImage):
    ### Naming convention for your subfolders ###
    NewFolderName = str(folder_num-1) + "K - " + str(folder_num) + "K"
    
    ### Creating new folder directory name ###
    NewFolderDirectory = jpgFolderDirectory/NewFolderName
    FolderAlreadyExisit = NewFolderDirectory
    
    ### Create directory if it doesn't already exist ###
    if not NewFolderDirectory.exists():
        NewFolderDirectory.mkdir()
        count = 0
        
    ### If directory wasn't created, count items in existing directory ###
    if count == -1:
        i = 0
        for jpgImages in FolderAlreadyExisit.glob('*.jpg'):
            i += 1
        count = i
        
    ### If directory is not full add image ###
    if count < MAX_IMAGES_PER_FOLDER:
        jpgImage.rename(NewFolderDirectory/jpgImage.name)
        count += 1
    
        ### Once directory is full reset count ###
        if count == MAX_IMAGES_PER_FOLDER:
            count = -1
            folder_num += 1
            
    ### If exisiting directory is full call function recursively with new direcatory index ###
    elif count >= MAX_IMAGES_PER_FOLDER:
        count = -1
        folder_num += 1
        check_directory(folder_num, count, jpgImage)


### Main ###
count = -1
folder_num = 1
for jpgImage in jpgFolder:
    check_directory(folder_num, count, jpgImage)

