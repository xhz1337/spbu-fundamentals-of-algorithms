from typing import Any, Protocol
from itertools import combinations

import numpy as np
import networkx as nx
from heapq import heappop, heappush

from src.plotting.graphs import plot_graph, plot_network_via_plotly
from src.common import AnyNxGraph 


class CentralityMeasure(Protocol):
    def __call__(self, G: AnyNxGraph) -> dict[Any, float]:
        ...


def closeness_centrality(G: AnyNxGraph) -> dict[Any, float]:
    closeness_centralities = {} 
    g_range = range(len(G))
    for n in g_range:
        distances = nx.shortest_path_length(G, source=n)
        closeness_centralities[n] = 1 / sum(distances[i] for i in g_range)
    return closeness_centralities


def betweenness_centrality(G: AnyNxGraph) -> dict[Any, float]: 

    ##########################
    ### PUT YOUR CODE HERE ###
    #########################

    pass


def eigenvector_centrality(G: AnyNxGraph) -> dict[Any, float]: 

    ##########################
    ### PUT YOUR CODE HERE ###
    #########################

    pass


def plot_centrality_measure(G: AnyNxGraph, measure: CentralityMeasure) -> None:
    values = measure(G)
    if values is not None:
        plot_graph(G, node_weights=values, figsize=(14, 8), name=measure.__name__)
    else:
        print(f"Implement {measure.__name__}")


if __name__ == "__main__":
    G = nx.karate_club_graph()
    print(nx.closeness_centrality(G))
    print(closeness_centrality(G))
    #plot_centrality_measure(G, closeness_centrality)
    #plot_centrality_measure(G, betweenness_centrality)
    #plot_centrality_measure(G, eigenvector_centrality)

