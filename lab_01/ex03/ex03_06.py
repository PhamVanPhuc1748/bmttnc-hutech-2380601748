def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = input("Nhập một dictionary (ví dụ: {'a': 1, 'b': 2}): ")
key_to_delete = input("Nhập khóa cần xóa: ")
if xoa_phan_tu(my_dict, key_to_delete):
    print("Đã xóa phần tử có khóa '{key_to_delete}'.")
else:
    print("Không tìm thấy khóa '{key_to_delete}' trong dictionary.")  

print("Dictionary sau khi xóa:", my_dict)          