#Проверить подпоследовательность
#Учитывая два непустых массива целых чисел, напишите функцию, которая определяет, является ли второй массив подпоследовательностью первого.

#Пример ввода:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isSubSequence(str2, str1):
    len_str1 = len(str1)
    len_str2 = len(str2)
    index_str1 = 0  
    index_str2 = 0
    while index_str1 < len_str1 and index_str2 < len_str2:
        if str1[index_str1] == str2[index_str2]:
            index_str1 = index_str1 + 1
        index_str2 = index_str2 + 1
    return index_str1 == len_str1

print(isSubSequence(array, sequence))