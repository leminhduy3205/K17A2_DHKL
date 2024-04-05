sum_numbers = 0
even_numbers = []

while sum_numbers <= 1000:
    num = int(input("Nhập một số nguyên dương: "))
    sum_numbers += num
    if num % 2 == 0:
        even_numbers.append(num)

print("Các số chẵn đã nhập:", even_numbers)