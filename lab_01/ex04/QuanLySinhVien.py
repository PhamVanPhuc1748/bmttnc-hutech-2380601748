from Sinhvien import SinhVien

class QuanLySinhVien:
    listSinhVien = [] 

    def tao_mssv(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0].mssv
            for sv in self.listSinhVien:
                if (maxId < sv.mssv):
                    maxId = sv.mssv
            maxId += 1
        return maxId

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        mssv = self.tao_mssv()
        mssv = int(input("Nhập MSSV: "))
        ten = input("Nhập tên sinh viên: ")
        gioi_tinh = input("Nhập giới tính (Nam/Nữ): ")
        chuyen_nganh = input("Nhập chuyên ngành: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(mssv, ten, gioi_tinh, chuyen_nganh, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def capNhatDanhSachSinhVien(self, mssv): 
        sv = self.timMssv(mssv) 
        if (sv != None):
            ten = input("Nhập tên sinh viên: ")
            gioi_tinh = input("Nhập giới tính (Nam/Nữ): ")
            chuyen_nganh = input("Nhập chuyên ngành: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv.ten = ten
            sv.gioi_tinh = gioi_tinh
            sv.chuyen_nganh = chuyen_nganh
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có MSSV:", mssv)

    def sapxepMssv(self):
        self.listSinhVien.sort(key=lambda sv: sv.mssv, reverse=False)

    def sapXepTenSV(self):
        self.listSinhVien.sort(key=lambda sv: sv.ten, reverse=False)

    def sapXepDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv.diemTB, reverse=True)

    def timMssv(self, mssv):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv.mssv == mssv):
                    searchResult = sv
        return searchResult

    def timTen(self, ten):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
               
                if (ten.upper() in sv.ten.upper()): 
                    listSV.append(sv)
        return listSV
    
    def xoaTheoMssv(self, mssv):
        isDelete = False
        sv = self.timMssv(mssv)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete

    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv.diemTB >= 8):
            sv.hocLuc = "Giỏi"
        elif(sv.diemTB >= 6.5):
            sv.hocLuc = "Khá"    
        elif(sv.diemTB >= 5):
            sv.hocLuc = "Trung Bình"
        else:
            sv.hocLuc = "Yếu" 

    def showSinhVien(self, listSV):
        
        print("{:<8} {:<20} {:<12} {:<15} {:<10} {:<10}"
              .format("MSSV", "Tên", "Giới Tính", "Chuyên Ngành", "Điểm TB", "Học Lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                
                print("{:<8} {:<20} {:<12} {:<15} {:<10} {:<10}" 
                      .format(sv.mssv, sv.ten, sv.gioi_tinh, sv.chuyen_nganh, sv.diemTB, sv.hocLuc))
        print("\n")             

    def getListSinhVien(self):
        return self.listSinhVien