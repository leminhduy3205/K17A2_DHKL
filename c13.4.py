n=input("Nhập tên tập tin:")
def doc_file():
    while True:
        nd=input('Nhập nội dung:')
        with open('JohnnyJohnny.txt','a') as file:
                file.write(nd+'\n')
        x=int(input('Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có,0: Không   '))
        if x == 1:
            continue
        elif x == 0:
            with open('JohnnyJohnny.txt','r') as file:
                doc=file.read()
                print("Đã ghi nội dung vào tập tin JohnnyJohnny.txt")
                print(doc)
            break
doc_file()