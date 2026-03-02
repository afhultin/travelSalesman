# Travelling Salesman Problem — Hill Climbing

Solves the Travelling Salesman Problem (TSP) using stochastic hill climbing with random restarts.

## Problem

Given a 4-city distance matrix, find the tour that visits every city exactly once and returns to the start with minimal total distance.

## Approach

- **Hill climbing** — iteratively swaps two random cities in the tour, keeping improvements and rejecting worse solutions
- **Random restarts** — runs 20 independent trials from random permutations and keeps the shortest tour
- **Termination** — stops after 100 consecutive non-improving neighbor evaluations

## Usage

```bash
python tsp_template.py
```

Outputs the best tour (city ordering) and its total distance.

Built for an Artificial Intelligence course.
