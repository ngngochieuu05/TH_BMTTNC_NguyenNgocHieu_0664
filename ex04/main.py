from QuanLySinhVien import QuanLySinhVien
qlsv= QuanLySinhVien()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("=================================")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("=================================")

    key =int(input("Nhap vao lua chon cua ban: "))
    if(key ==1):
        print("\n1. Them sinh vien")
        qlsv.themSinhVien()
        print("Them sinh vien thanh cong!")
    elif(key ==2):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n2. Cap nhat thong tin sinh vien")
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlsv.updateSinhVien(ID)
    elif(key ==3):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n3. Xoa sinh vien boi ID")
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if(qlsv.deleteByID(ID) != None):
                print("Xoa sinh vien thanh cong!")
            else:
                print("Khong tim thay sinh vien co ID: ", ID)
    elif(key ==4):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n4. Tim kiem sinh vien theo ten")
            name = input("Nhap ten sinh vien can tim: ")
            listSV = qlsv.findByName(name)
            qlsv.showSinhVien(listSV)
    elif(key ==5):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n5. Sap xep sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
    elif(key ==6):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n6. Sap xep sinh vien theo ten chuyen nganh")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
    elif(key ==7):
        if(qlsv.soLuongSinhVien() == 0):
            print("Danh sach sinh vien trong!")
        else:
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
    elif(key ==0):
        print("Thoat chuong trinh. Hen gap lai!")
        break
    else:
        print("Lua chon khong hop le. Vui long thu lai!")