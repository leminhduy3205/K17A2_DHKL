ten_tap_tin=input("Nhập tên tập tin:")
with open("Rain.txt",'w',encoding='utf-8') as f:
    f.write("Rain rain, go away; Come again another day...\n")
f=open("Rain.txt",'r')
content=f.read()
print(content) 
print("Đã ghi nội dung vào tập tin Rain.txt!!!")
print("Rain rain, go away; Come again another day...")
f.close