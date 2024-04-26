num_servers = int(input('Enter number of servers: '))
num_loads = int(input('Enter number of loads: '))

servers = []
for i in range(num_servers):
    name = input(f'Enter the name for server {i+1}: ')
    weight = int(input(f'Enter the weight for server {i+1}: '))
    servers.append([name, weight, 0])

i=0
index = i % num_servers
while i<num_loads:
    if servers[index][2] < servers[index][1]:
        print(f'Load {i+1} is assigned to server {servers[index][0]}')
        servers[index][2] += 1
        i+=1
        index = i % num_servers
    else: 
        index += 1
