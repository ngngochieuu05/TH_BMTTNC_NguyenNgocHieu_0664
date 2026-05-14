def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element


print(
    f"Phan tu dau tien va cuoi cung cua tuple la:",
    " ".join(
        str(x)
        for x in truy_cap_phan_tu(eval(input("Nhap tuple vi du (1,2,545): ")))
    ),
)
