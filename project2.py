def prototype_f(liste):


    
    if len(liste)%2 == 0:
        
        for i in range(0,int(len(liste)/2)):
            l1 = liste[i]
            l2 = liste[len(liste)-1-i]

            liste[i] = l2
            liste[len(liste)-1-i] = l1
        
    else:

        for i in range(0,int((len(liste)-1)/2)):
            l1 = liste[i]
            l2 = liste[len(liste)-1-i]

            liste[i] = l2
            liste[len(liste)-1-i] = l1


    
    return liste




def actual_f(listem):

    prototype_f(listem)

    for item in listem:
        if type(item) == list:
            actual_f(item)
    
    return(listem)
    




ex = [[1, 2], [3, 4], [5, 6, 7,[1,2,[1,2,"a"]]]]

print(actual_f(ex))
#output: [[[['a', 2, 1], 2, 1], 7, 6, 5], [4, 3], [2, 1]]



            




