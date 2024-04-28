import numpy as np

def calculate_distance(coords, order):
    dist = 0
    for i in range(len(order)):
        dist += np.linalg.norm(coords[order[i]] - coords[order[(i + 1) % len(order)]])
    return dist

def ant_colony_optimization(coords, num_ants=10, num_iterations=100, evaporation_rate=0.5, alpha=1, beta=2):
    num_cities = len(coords)
    pheromone = np.ones((num_cities, num_cities))

    best_order = None
    best_distance = float('inf')

    for _ in range(num_iterations):
        for _ in range(num_ants):
            order = np.random.permutation(num_cities)
            distance = calculate_distance(coords, order)

            if distance < best_distance:
                best_distance = distance
                best_order = order

            for i in range(num_cities):
                pheromone[order[i], order[(i + 1) % num_cities]] += 1 / distance

        pheromone *= (1 - evaporation_rate)

    return best_order, best_distance

# Example usage:
if __name__ == "__main__":
    np.random.seed(0)
    cities_coords = np.array([
        [0, 0],
        [1, 1],
        [1, 2],
        [2, 2],
        [2, 1]
    ])

    best_order, best_distance = ant_colony_optimization(cities_coords)
    print("Best order:", best_order)
    print("Best distance:", best_distance)
