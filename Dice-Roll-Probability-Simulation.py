import random 
import matplotlib.pyplot as plt

random.seed(50)
dace = [0, 0, 0, 0, 0, 0]

for i in range(1, 10000):
    x = random.randint(1, 6)
    # print(x , end= "")
    dace[x-1] += 1
    
x = sum(dace)

for i in range(len(dace)):
    dace[i] = (dace[i]/x)*100
    
print(dace)
dace.sort(reverse = True)

sides_of_die = [1, 2, 3, 4, 5, 6]


plt.bar(sides_of_die, dace)


plt.show()