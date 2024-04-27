# Better way to open files
with open("./files/new_txt_file.txt",mode='a') as my_file:
    text= my_file.write("write to the new text file\n")

with open("./files/new_txt_file.txt",mode='r') as my_file:
    print(my_file.read())