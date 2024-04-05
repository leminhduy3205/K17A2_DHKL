num = int(input("Nhập số nguyên: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print("Số chữ số của số nguyên:", count)