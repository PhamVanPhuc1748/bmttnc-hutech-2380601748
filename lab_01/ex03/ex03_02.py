def dao_nguoc(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))

list_dao_nguoc = dao_nguoc(numbers)
print("Danh sách sau khi đảo ngược:", list_dao_nguoc)