#1
def merge_dict(dict1, dict2):
    merged_dict={}
    for key in dict1:
        merged_dict[key]=dict1[key]
    for key in dict2:
        merged_dict[key]=dict2[key]
    return merged_dict
d1={'A': 20, 'B':10}
d2={'C':5, 'D':15, 'E':20}
print(merge_dict(d1,d2))
        
#2
def common_dict(list1,list2):
    my_dict={}
    for element in list1:
        if element in list2:
            if element not in my_dict:
                my_dict[element]=1
            else:
                my_dict[element]+=1
    return my_dict
l1=list(map(int,input("Enter elements for list1:").split(',')))
l2=list(map(int,input("Enter elements for list2:").split(',')))
print(common_dict(l1,l2))

#3
def tuple_to_dict(list_of_tuple):
    my_dict=dict(list_of_tuple)
    return my_dict
list_tuple=[('A', 20), ('B',10), ('C',5), ('D',15), ('E',20)]
print(tuple_to_dict(list_tuple))
            
