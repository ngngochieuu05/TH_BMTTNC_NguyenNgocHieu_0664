from SinhVien import SinhVien


class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soLuongSinhVien() > 0:
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if sv._id > maxID:
                    maxID = sv._id
            maxID += 1
        return maxID

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def themSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if sv != None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._diemTB = diemTB
            sv._major = major
            sv._sex = sex
            self.xepLoaiHocLuc(sv)
        else:
            print("Khong tim thay sinh vien co ID: ", ID)

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 9:
            sv._hocLuc = "Xuat sac"
        elif sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 7:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=True)

    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() == 0:
            return searchResult
        for sv in self.listSinhVien:
            if sv._id == ID:
                searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv != None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def showSinhVien(self, listSV):
        print(
            "{:<8} {:<20} {:<10} {:<20} {:<10} {:<10}".format(
                "ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"
            )
        )
        if listSV.__len__() > 0:
            for sv in listSV:
                print(
                    "{:<8} {:<20} {:<10} {:<20} {:<10} {:<10}".format(
                        sv._id,
                        sv._name,
                        sv._sex,
                        sv._major,
                        sv._diemTB,
                        sv._hocLuc,
                    )
                )
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
