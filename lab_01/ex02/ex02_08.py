def divi_5(so_nhi_phan):
    decimal = int(so_nhi_phan, 2)
    return decimal % 5 == 0
list_bina = [
    x for x in map(str, input("Nhap so nhi phan: ").split(",")) if divi_5(x)
]
print("Cac so nhi phan chia het cho 5 la:", ",".join(list_bina))
