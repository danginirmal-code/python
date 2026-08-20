with open("example.txt","r") as file:
    content=file.read()
    print(content)
##Read a file line by line

with open("example.txt","r") as file:
    print()
    for line in file:
        print(line.strip())#remives tge new line character

##Writing a file 
with open("example.txt","w") as file:
    file.write("Hello World\n")
    file.write("this is a new line")
##write a file without overwritting
with open("example.txt","a") as file:
    file.write("Append operation is taking place\n")

##writting  a list of lines to a file
lines=["FIrst line\n","second line \n","third line \n"]
with open("example.txt",'a') as file:
    file.writelines(lines)

#read the content from source text file and write tpa destination.txt
with open("example.txt","r") as source_file:
    content=source_file.read()
with open("destination.txt","w") as destination_file:
    destination_file.write(content)

def count_text_file(file_path):
    with open(file_path,'r') as file:
        lines=file.readlines()
        line_count=len(lines)
        word_count=sum(len(line.split()) for line in lines)
        char_count=sum(len(line) for line in lines) 
        return line_count,word_count,char_count
file_path='example.txt'
lines,words,characters=count_text_file(file_path)
print(f'lines:{lines},words:{words},character:{characters}')

#writing and then reading a file
with open('example.txt','w+') as file:
    file.write("Hello world\n")
    file.write("This is a new line")
    file.seek(0)
    content=file.read()
    print(content)
