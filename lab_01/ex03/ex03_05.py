def count_elements(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


print(
    "So lan xuat hien cua tung tu trong danh sach la:",
    count_elements(input("Nhap vao danh sach cac tu: ").split()),
)
