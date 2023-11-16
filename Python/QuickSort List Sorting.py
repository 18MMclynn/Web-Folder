mainlist = [88, 46, 25, 11, 18, 12, 22]
pivot = int(mainlist[-1])
print(pivot)

def sortedlist(templist):
    if len(templist) <= 1:
        return templist
    else:
        pivot = int(templist[-1])
    
        left_list = []
        middle_list = []
        right_list = []

        for elements in templist:
    
            if pivot > elements:
                left_list.append(elements)
                print(left_list)
            elif pivot == elements:
                middle_list.append(elements)
                print(middle_list)
            elif pivot < elements:
                right_list.append(elements)
                print(right_list)
        return sortedlist(left_list) + middle_list + sortedlist(right_list)

#sortedlist(mainlist)
print(sortedlist(mainlist))