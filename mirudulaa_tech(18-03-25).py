def flatten_list(nested_list):
    flat_list = []
    def flatten(element):
        if isinstance(element, list):
            for item in element:
                flatten(item)
        else:
            flat_list.append(element)
    flatten(nested_list)
    return flat_list

arr = [1, [2, [3, [4, 5]], 6], 7]
result = flatten_list(arr)
print(result)  
