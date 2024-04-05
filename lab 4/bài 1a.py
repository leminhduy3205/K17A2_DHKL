sum_numbers = 0
odd_numbers = []

while sum_numbers <= 1000:
    num = int(input("Nhập một số nguyên dương: "))
    sum_numbers += num
    if num % 2 != 0:
        odd_numbers.append(num)

print("Các số lẻ đã nhập:", odd_numbers)