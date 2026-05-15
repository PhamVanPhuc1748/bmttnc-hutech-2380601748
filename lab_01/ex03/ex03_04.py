def truy_cap_phan_tu(lst):
    first_element = tuple(lst)[0]
    last_element = tuple(lst)[-1]
    return first_element, last_element

input_tuple = eval(input("Nhập một tuple: "))
first, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)