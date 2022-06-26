nested_list = [-20.43, 309.3, 80, 11.32, [-44.90, 609, [29.23, [-50.11, 440, 87.43, 90.32]]]]

def summa(nested_list):
    total_sum = 0
    for element in nested_list:
        if (type(element) == type([])):
            total_sum = total_sum + summa(element)
        else:
            total_sum = total_sum + element
    return total_sum

print("Сумма элементов:", summa(nested_list), '\n')