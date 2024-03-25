"""
Program : dircreator.py
Author: Nicky Enriquez
Function: program that create directories from file txt
"""
import os
import sys
import shutil
#file   : list of directory names
#file2  : list of subdirectory inside of each directory
def dircreator(file,file2=None):
    
    with open(file, "r") as file:
        dirs = file.read().splitlines()
    
    filepath = os.path.abspath(__file__)
    basedirname = os.path.dirname(filepath)
    
    for index, dirname in enumerate(dirs, start=1):
        
        prefix = str(index).zfill(2)
        newdirname = f"{prefix}_{dirname}"
        newdirpath = os.path.join(basedirname,newdirname)
        try:
            print(f"creating folder : {newdirname}")
            if os.path.exists(newdirpath):
                shutil.rmtree(newdirpath)
            os.mkdir(newdirpath)   
            
            if(file2!=None):                
                with open(file2, "r") as file:
                    subdirs = file.read().splitlines()                   
                    
                for index2, subdir in enumerate(subdirs, start=1):
                    prefix2 = str(index2).zfill(2)
                    newsubdir = f"{prefix2}_{subdir}"
                    newsubdirpath = os.path.join(newdirpath,newsubdir)
                    try:
                        print(f"Creating subfolder : {newsubdir}")
                        if os.path.exists(newsubdirpath):
                            shutil.rmtree(newsubdirpath)
                        os.mkdir(newsubdirpath)   
                    except FileExistsError:
                        print(f"folder {newsubdir} already exist.")
        except FileExistsError:
            print(f"Folder {newdirname} already exist.")            

def main():
    if(len(sys.argv)<3):
        print("Use : python direcreator.py <file> <file2>")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    dircreator(file1,file2)
    
if __name__ == "__main__":
    main()