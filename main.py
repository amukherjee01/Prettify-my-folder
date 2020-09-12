#path, dictionary file, format
import os
def soldier(pathname,filename,imgformat):
    os.chdir(pathname)
    filelist = os.listdir(pathname)
    i = 1
    with open(filename) as f:
        data = f.read().split("\n")
    for file in filelist:
        if (file not in data) and not(file.endswith(imgformat)) and os.path.isfile(file):
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] == imgformat:
            os.rename(file,f"{i}{imgformat}")
            i+=1

if __name__ == "__main__":

    soldier(r"C:\Users\Lenovo\Desktop\myfolder",r"C:\Work\complete python\CodeWithHarryPython\Soldier Pretiffier\pretiffy.txt",".jpg")
