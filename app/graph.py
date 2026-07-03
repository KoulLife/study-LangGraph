from langgraph.graph import StateGraph, START, END

from app.state import CounterState
from app.nodes import first_increment, second_increment


def build_graph():
    graph = StateGraph(CounterState)

    graph.add_node("first", first_increment)
    graph.add_node("second", second_increment)

    graph.add_edge(START, "first")
    graph.add_edge("first", "second")
    graph.add_edge("second", END)

    return graph.compile()