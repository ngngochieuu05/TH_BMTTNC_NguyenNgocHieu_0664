def sum_so_chan(lst):
    return sum([x for x in lst if x % 2 == 0])
number_list = map(int, input("nhap vao mot day so nguyen: ").split())
print("Tổng các số chẵn trong dãy là:", sum_so_chan(number_list))