# -*- coding: utf-8 -*-
import os

run = 'running'

while run != 'finish':
    try:
        number = int(input('Digite um número para saber se ele é primo ou não: '))
    except ValueError:
        print('Value Error')
        
    total = 0
    
    for count in range(1, number + 1):
        if number % count == 0:
            total += 1
    
    if total == 2:
        print(f'O número {number} é primo.')
    else:
        print(f'O número {number} não é primo.')
    
    try:
        choice = str(input('Deseja continuar testando? [s/n]: '))
    except ValueError:
        print('Value Error')
    
    if choice == 'S' or choice == 's':
        os.system("clear || cls")
    elif choice == 'N' or choice == 'n':
        run = 'finish'
    else:
        print('Incorret digit.')
        run = 'finish'