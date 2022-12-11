ex = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


wanted_list = []


def flatten_list(given_list):

    # visiting each item in a nested list structure and putting them in wanted list such that wanted list is not nested one.


    for item in given_list:


        if isinstance(item, list):

            visiting_each_item(item)
            
    
        else:

            wanted_list.append(item)


visiting_each_item(ex)

print(wanted_list)
#output : [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
