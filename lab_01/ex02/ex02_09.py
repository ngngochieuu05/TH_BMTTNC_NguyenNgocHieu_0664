def prime_number(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 2


print(
    f"{n} la so nguyen to"
    if prime_number(n := int(input("nhap mot so nguyen: ")))
    else f"{n} khong phai la so nguyen to"
)
