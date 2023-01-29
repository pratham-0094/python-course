import os

print(os.getcwd())  # get current working directory

os.chdir("C://")  # change working directory
print(os.getcwd())

print(os.listdir("C://program files"))
# list all the file / folder in the directory, return a list

print(os.listdir())
# if no path s specified then list all the file / folder of current working directory
for i in os.listdir():
    print(i)

os.mkdir("newfolder")  # make folder
os.rmdir("newfolder")  # remove folder

os.makedirs("newfolder/secondfolder")  # make subfolders

os.remove("hello.txt")  # remove file
os.rename("hello.txt", "sample.txt")  # rename file

print(os.environ.get("PATH"))  # get enviroment variable value

print(os.path.join("C://", "/hello.txt"))  # join two path
for i in os.listdir():
    print(os.path.join(os.getcwd(), i))

print(os.path.exists("C://program files"))  # check path is exist or not
print(os.path.isfile("sample.txt"))  # check file in the path is exist or not
print(os.path.isdir("C://program files"))
# check folder in the path is exist or not
