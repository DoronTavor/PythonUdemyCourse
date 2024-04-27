# Better way to open files
import datetime
with open("my_file.txt",mode='a') as my_file:
    text= my_file.write(f"\n The date is {datetime.date.today()}")