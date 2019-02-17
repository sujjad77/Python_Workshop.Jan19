def frequency(str):
    dict = {}
    for each in str:
        key = dict.keys()
        if each in key:
            dict[each] += 1
        else:
            dict[each] = 1
    return dict


print(frequency(input("Enter a string: ")))
