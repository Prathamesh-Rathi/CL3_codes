import xmlrpc.client

num_servers = int(input('Enter number of servers: '))
num_loads = int(input('Enter number of loads: ')) 
loads = []
for i in range(num_loads):
    loads.append(int(input(f'Enter  load {i+1} to calculate factorial: ')))

for i in range(num_loads):
    index = i % num_servers
    proxy = xmlrpc.client.ServerProxy(f'http://localhost:{8000+index}/')
    result = proxy.factorial(loads[i])
    print(f"The factorial of {loads[i]} is {result} (server #{index})")






















    

# def create_server(name, weight):
#     return {"name": name, "weight": weight}

# def create_load_balancer(servers):
#     return {"servers": servers, "current_index": 0}

# def add_server(load_balancer, server):
#     load_balancer["servers"].append(server)

# def get_next_server(load_balancer):
#     next_server = load_balancer["servers"][load_balancer["current_index"]]
#     load_balancer["current_index"] = (load_balancer["current_index"] + 1) % len(load_balancer["servers"])
#     return next_server

# def prompt_server_info(index):
#     name = input("Enter the name of server " + str(index) + ": ")
#     weight = int(input("Enter the weight of server " + str(index) + ": "))
#     return create_server(name, weight)

# def assign_load(load_balancer, i):
#     next_server = get_next_server(load_balancer)
#     print("Load", i, "assigned to server:", next_server["name"])

# if __name__ == "__main__":
#     servers = []
#     num_servers = int(input("Enter the number of servers: "))
#     for i in range(1, num_servers + 1):
#         servers.append(prompt_server_info(i))

#     lb = create_load_balancer(servers)

#     num_loads = int(input("Enter the number of loads: "))

#     print("\nLoad balancing result:")
#     for i in range(1, num_loads + 1):
#         assign_load(lb, i)


