def unique_in_order(arr):
    new_list = []
    previous = None
    for item in arr:
        if item != previous:
            new_list.append(item)
        previous = item
    print(new_list)

unique_in_order('AAAABBBCCDAABBB')
