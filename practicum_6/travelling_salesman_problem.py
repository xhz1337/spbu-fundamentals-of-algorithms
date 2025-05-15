from pathlib import Path
from typing import Any

import networkx as nx
import numpy as np

from src.plotting.graphs import plot_graph
from src.common import AnyNxGraph


class DpAlgorithmForTravellingSalesmanProblem:
    """
    This algorithm finds the optimal path of a salesman
    visiting all nodes of a graph exactly once and 
    returning to the starting node.
    """ 
    def __init__(self, G: nx.DiGraph) -> None:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass

    def run(self, node: Any) -> tuple[int, set[tuple[Any, Any]]]:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass


if __name__ == "__main__":
    G = nx.read_edgelist(
        Path("practicum_6") / "simple_weighted_graph_5_nodes.edgelist",
        create_using=nx.Graph
    )
    plot_graph(G)

    dp = DpAlgorithmForTravellingSalesmanProblem(G)
    min_dist, optimal_path = dp.run(node="A")
    plot_graph(G, highlighted_edges=list(optimal_path))

