def groups_of_3(values:list[int])->list[list[int]]:
    triple_list = []
    for value in range(0,len(values),3):
        triple_list.append(values[value:value+3])
    return triple_list
