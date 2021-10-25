""" 
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""

"""input_array=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_function(arr):
    output=[]
    for sublist in arr:
        for element in sublist:
             output.append(element)
    return output 

print("output: ",flatten_function(input_array))""" 

def flatten_without_rec(non_flat):
    
    flat = []
    
    while non_flat: #runs until the given list is empty.
        
            e = non_flat.pop()
            
            if type(e) == list: #checks the type of the poped item.
                
                    non_flat.extend(e) #if list extend the item to given list.
            else:
                
                    flat.append(e) #if not list then add it to the flat list.
            
    flat.reverse()
    
    return flat
l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_without_rec(l))