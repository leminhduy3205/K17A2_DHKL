ten_tap_tin=input("Nhập tên tập tin:")
with open("HumptyDumpty.txt",'w',encoding='utf-8') as f:
    print("Nội dung tập tin:")
    f.write("Humpty Dumpty sat on a wall,\n")
    f.write("Humpty Dumpty had a great fall.\n")
    f.write("All the king's horses and all the king's men\n")
    f.write("Couldn't put Humpty together again.\n")
f=open("HumptyDumpty.txt",'r')
content=f.read()
print(content) 
f.close