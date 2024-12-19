import random as rd
import math
import statistics as st
import matplotlib.pyplot as plt
nb_test=1000
nb_inmates=100
criteria_range=range(10,101,5)
def inmates_scape_probability(criteria):
    inmates = range(1,nb_inmates+1,1)
    boxes = rd.sample(range(1,nb_inmates+1,1),nb_inmates)
    boxes_required = [(inmates[i],boxes[i-1]) for i in range(nb_inmates)]
    l = 0
    for i in inmates:
        x = 0
        inmates = boxes_required[i - 1][1]
        
        while x < (criteria+1):
            if i == inmates:
                x = (criteria+1)
                l = l + 1
                break
            inmates = boxes_required[inmates - 1][1] 
            x = x + 1
            if x > criteria:
                break    

    if l == nb_inmates:
        win_or_loose = 1
    else:
        win_or_loose = 0
        
    return win_or_loose
winning_percentage=[]
for j,criteria2 in enumerate(criteria_range):
    prob_lst = []
    for i in range(nb_test): 
        result = inmates_scape_probability(criteria2)
        prob_lst.append(result)
        print(i)
    
    a = sum(prob_lst)
    winning_percentage.append(st.mean(prob_lst))

plt.plot(criteria_range,winning_percentage)
plt.show()
# print(criteria_range)
# print(winning_percentage)
