#Criando uma rede neural básica

import math

input = -3 
output_desire = 1

input_weight = 0.5
learning_rate = 0.0001

bias = 1
bias_weight = 0.5

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0    


print("entrada",input,"desejado",output_desire)

error = math.inf

interation = 0 

while not error == 0:
    interation += 1
    print("############## iteração", interation)
    print("peso",input_weight)
    # input_weight = input_weight + learning_rate * input * error
    sum = (input * input_weight) + (bias + bias_weight)
    
    output = activation(sum)
    print("saida",output)

    error = output_desire - output

    print("erro",error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)

print("Parabéns!!! A Rede aprendeu")