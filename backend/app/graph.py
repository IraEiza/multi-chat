from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str

def passthrough(state: State) -> State:
    print('Passthrough state:', state)
    return state

builder = StateGraph(State)

builder.add_node("passthrough", passthrough)
builder.add_edge(START, "passthrough")
builder.add_edge("passthrough", END)

graph = builder.compile()
