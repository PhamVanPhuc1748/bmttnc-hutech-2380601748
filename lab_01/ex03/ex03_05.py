def dem_so_lan_xuat_hien(lst):
    dem = {}
    for char in lst:
        if char in dem:
            dem[char] += 1
        else:
            dem[char] = 1
    return dem

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu ',': ")
word_list = input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi phần tử:", so_lan_xuat_hien)