import time

lista = ["45565687998","123456","222222"]

for i in range(len(lista)):
    if i == len(lista):
        break
    else:
        print(lista[i])
        time.sleep(1)
        print(lista[i+1])
    
    