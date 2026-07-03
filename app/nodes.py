from app.state import CounterState


def first_increment(state: CounterState) -> dict:
    print("first increment")
    return {"count": state["count"] + 1}

def second_increment(state: CounterState) -> dict:
    print("second increment")
    return {"count": state["count"] + 10}