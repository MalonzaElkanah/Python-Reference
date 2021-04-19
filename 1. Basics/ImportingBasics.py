import random
import os, sys, math

for i in range(15):
    print(random.randint(1, 10))

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

