from benchmark import Benchmark
from problems.n_puzzle.n_puzzle_problem import NPuzzleProblem
from problems.n_puzzle.n_puzzle_state import NPuzzleState

from problems.route_finding.location import Location
from problems.route_finding.route_finding import RouteFinding

from problems.rush_hour.vehicle import RushHourVehicle
from problems.rush_hour.rush_hour import RushHourProblem
from problems.rush_hour.board import RushHourBoard
from problems.rush_hour.heuristic import RushHourHeuristic

from solvers import BFS, DFS, BestFirstSearch, AStar, IDAStar
import numpy as np


def main_routefinding():
    a = Location("A", (0, 0))
    b = Location("B", (1, 1))
    c = Location("C", (2, 0))
    d = Location("D", (1, -1))
    
    pr = RouteFinding([a, b, c, d], [(a, b, 10), (b, c, 1), (a, d, 1), (d, c, 9)], a, c)

    bfs = BFS(pr, pr.initial)
    target_bfs = bfs.run()
    print(f"BFS: {target_bfs.path()}")
    
    dfs = DFS(pr, pr.initial)
    target_dfs = dfs.run()
    print(f"DFS: {target_dfs.path()}")

    bestfs= BestFirstSearch(pr, pr.initial)
    target_bestfs = bestfs.run()
    print(f"bestfirst: {target_bestfs.path()}")

    dist = lambda s: np.linalg.norm(np.array(s.coord) - np.array(pr.goal.coord), ord=np.inf)
    astar= AStar(pr, pr.initial, dist)
    target_astar = astar.run()
    print(f"astar: {target_astar.path()}")

    idastar= IDAStar(pr, pr.initial)
    target_idastar = idastar.run(dist)
    print(f"idastar: {target_idastar.path()}")


def main_n_puzzle():
    start_matrix = [[2, 8, 3],
                    [1, 6, 4],
                    [0, 7, 5]]

    final_matrix = [[1, 2, 3],
                    [8, 0, 4],
                    [7, 6, 5]]

    start_state = NPuzzleState(start_matrix, 2, 0)
    final_state = NPuzzleState(final_matrix, 1, 1)

    p = NPuzzleProblem(start_state, final_state)

    dist = lambda current: ((current.x + current.y)**2 + p.goal.y + p.goal.x)

    solver = BFS(p, start_state)
    target_solver = solver.run()
    print(f"Solver: {target_solver.path()}")


def main_benchmark():
    start_matrix = [[2, 8, 3],
                    [1, 6, 4],
                    [0, 7, 5]]

    final_matrix = [[1, 2, 3],
                    [8, 0, 4],
                    [7, 6, 5]]

    start_state = NPuzzleState(start_matrix, 2, 0)
    final_state = NPuzzleState(final_matrix, 1, 1)

    p = NPuzzleProblem(start_state, final_state)
    dist = lambda current: (current.x + current.y)**2

    b = Benchmark(p)
    b.compare((["BFS", "BestFirstSearch", "AStar", "DFS"], dist))
    b.print_grades()


def main_rush_hour():
    x = RushHourVehicle('X', 3, 2, 'H')
    a = RushHourVehicle('A', 0, 0, 'H')
    b = RushHourVehicle('B', 2, 0, 'H')
    c = RushHourVehicle('C', 4, 0, 'V')
    d = RushHourVehicle('D', 0, 1, 'V')  
    e = RushHourVehicle('E', 2, 1, 'H')
    f = RushHourVehicle('F', 1, 2, 'V')
    g = RushHourVehicle('G', 0, 5, 'H')
    o = RushHourVehicle('O', 5, 0, 'V') 
    p = RushHourVehicle('P', 2, 2, 'V')
    q = RushHourVehicle('Q', 3, 3, 'H')  

    vehicles = {x, a, b, c, d, e, f, g, o, p, q}
    board = RushHourBoard(vehicles) 
    problem = RushHourProblem(vehicles, board)
    blocking_cars_heuristic = RushHourHeuristic().blocking_cars
    distance_to_exit_heuristic = RushHourHeuristic().distance_to_exit

    solver = BFS(problem, board)
    target_bfs = solver.run()
    print(f"Solver: {target_bfs.path()}") 

    dfs = DFS(problem, board)
    target_dfs = dfs.run()
    print(f"DFS: {target_dfs.path()}")

    bestfs= BestFirstSearch(problem, board)
    target_bestfs = bestfs.run()
    print(f"bestfirst: {target_bestfs.path()}")

    astar= AStar(problem, board, blocking_cars_heuristic)
    target_astar = astar.run()
    print(f"astar: {target_astar.path()}")

    # idastar= IDAStar(problem, board)
    # target_idastar = idastar.run(distance_to_exit_heuristic)
    # print(f"idastar: {target_idastar.path()}")

if __name__ == '__main__':
    #main_n_puzzle()
    # main_routefinding()
    #main_benchmark()
    main_rush_hour()