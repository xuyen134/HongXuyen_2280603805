def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
# Kiểm tra số nguyên tố và in kết quả
number = int(input("Nhập vào số đã kiểm tra:"))
if kiem_tra_so_nguyen_to(number):
    print(number,"là số nguyên tố.")
else:
    print(number, "không phải số nguyên tố.")