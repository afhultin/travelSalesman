# Travelling Salesman Problem - Hill Climbing

Solves TSP on a 4-city distance matrix using hill climbing with random restarts.

Randomly swaps cities in the tour and keeps the swap if it shortens the route. Stops after 100 swaps with no improvement, then restarts from a new random tour. Runs 20 restarts total and keeps the shortest.
