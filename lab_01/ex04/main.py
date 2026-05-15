from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("**********************************MENU*****************************")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo MSSV")
    print("3. Xoa sinh viên theo MSSV")
    print("4. Tìm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm Trung Bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    print("*******************************************************************")

    key = int(input("Nhập tuỳ chọn: "))
    if(key == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công")
    elif (key == 2):
     if(qlsv.soLuongSinhVien() > 0):
       print("\n2. Cập nhật thành công sinh viên. ")
       print("\nNhập MSSV")
       mssv = int(input())
       qlsv.capNhatDanhSachSinhVien(mssv)
     else:
        print()
