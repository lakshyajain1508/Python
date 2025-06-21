data = {}

n = int(input('Enter the number of items: '))

for i in range(n):
    key = input('Enter the key: ')
    value = input('Enter the value: ')
    data[key] = value
    
    
for key, value in data.items():
    print(f'{key}: {value}')