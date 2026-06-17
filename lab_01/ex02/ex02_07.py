print("Nhap cac dong van ban(Nhap 'end' de ket thuc): ")
lines = []
while True:
    text = input()
    if text.lower() == "end":
        break
    lines.append(text)
print("Ban da nhap cac dong van ban sau khi chuyen thanh chu in hoa ")
for text in lines:
    print(text.upper())
