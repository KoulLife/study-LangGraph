from app.graph import build_graph


def main():
    app = build_graph()

    result = app.invoke({"count": 0})
    print(f"최종 결과: {result}")

if __name__ == "__main__":
    main()