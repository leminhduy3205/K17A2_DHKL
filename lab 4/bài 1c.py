sum_of_numbers = 0
count = 0
print("Nhập các số nguyên dương từ bàn phím cho đến khi tổng vượt quá 1000:")
while sum_of_numbers <= 1000:
    num = int(input("Nhập số nguyên dương: "))
    if num <= 0:
        print("Vui lòng nhập số nguyên dương.")
        continue
    sum_of_numbers += num
    count += 1
print("Số lượng số nguyên đã nhập:", count)
