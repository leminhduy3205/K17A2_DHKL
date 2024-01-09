def check_so_nguyen_duong(a):
    if a<0:
        raise Exception("LỖI SỐ ÂM!!!")
def check_so_nguyen(b):
    try:
        return int(b)
    except ValueError:
        raise Exception("LỖI NHẬP SỐ!!!")
def check_4_so_nguyen_duong_lien_tiep(numbers):
    if len(numbers)>=4 and all(num==numbers[-1] for num in numbers[-4:]):
        raise Exception("LỖI NHẬP LẶP LẠI!!!")
def check_5_so_chan_lien_tiep(numbers):
    if len(numbers)>=5 and all(num % 2 == 0 for num in numbers[-5]):
        raise Exception("LỖI NHẬP CHẴN!!!")
def main():
    numbers=[]
    while True:
        try:
            input_str=input("Nhập một số:")
            num=check_so_nguyen(input_str)
            check_so_nguyen_duong(num)
            check_4_so_nguyen_duong_lien_tiep(numbers)
            check_5_so_chan_lien_tiep(numbers)
            if num == 0:
                break
            numbers.append(num)
        except Exception as error:
            print("LỖI!!!",error)
    print("CÁC SỐ NGUYÊN DƯƠNG ĐÃ NHẬP:",numbers)        
main()