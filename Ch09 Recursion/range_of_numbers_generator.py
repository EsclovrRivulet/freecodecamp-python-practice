def range_of_numbers(start_num, end_num):
    if end_num < start_num:
        return []
        
    range_list = range_of_numbers(start_num, end_num - 1)
    range_list.append(end_num)
    return range_list
    
print(range_of_numbers(1, 5))
print(range_of_numbers(1, 3))
print(range_of_numbers(6, 9))
print(range_of_numbers(4, 4))
print(range_of_numbers(10, 15))