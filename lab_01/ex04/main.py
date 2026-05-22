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
        print("\nDanh sách sinh viên trống!")
    elif (key == 3):
       if(qlsv.soLuongSinhVien() > 0):
          print("\n3. Xoá sinh viên")
          print("\nNhập MSSV: ")
          mssv = int(input())
          if(qlsv.xoaTheoMssv(mssv)):
             print("\nSinh viên có mssv = ", mssv, " đã bị xoá")
          else:
             print("\nSinh viên có mssv ", mssv, " không tồn tại!")
       else:
          print("\nDanh sách sinh viên trống!")
    elif (key == 4):
       if(qlsv.soLuongSinhVien() > 0):
          print("\n4. Tìm kiếm sinh viên theo tên. ")
          print("\nNhập tên sinh viên cần tìm: ")
          name = input()
          searchResult = qlsv.timTen(name)
          qlsv.showSinhVien(searchResult)
       else:
          print("\nDanh sách sinh viên trống!")
    elif (key == 5):
        if(qlsv.soLuongSinhVien() > 0):
           print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA). ")
           qlsv.sapXepDiemTB()
           qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
           print("\nDanh sách sinh viên trống!")
    elif (key == 6):
       if(qlsv.soLuongSinhVien() > 0):
          print("\n6. Sắp xếp sinh viên theo tên.")
          qlsv.sapXepTenSV()
          qlsv.showSinhVien(qlsv.getListSinhVien())
       else:
         print("\nDanh sách sinh viên trống!")
    elif (key == 7):
       if(qlsv.soLuongSinhVien() > 0):
          print("\n7. Hiển thị danh sách sinh viên.")
          qlsv.showSinhVien(qlsv.getListSinhVien())
       else:
          print("\nDanh sách sinh viên trống!")
    elif (key == 0):
        print("\n0. Thoát chương trình.")
        break
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn lại!") 

       
