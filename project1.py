ex = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


wanted_list = []


def visiting_each_item(given_list):

    # visiting each item in a nested list structure/list flatten...


    for item in given_list:


        if isinstance(item, list):

            visiting_each_item(item)
            
    
        else:

            wanted_list.append(item)


visiting_each_item(ex)

print(wanted_list)
#output : [1, 'a', 'cat', 2, 3, 'dog', 4, 5]