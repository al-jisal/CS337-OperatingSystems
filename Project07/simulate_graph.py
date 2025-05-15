import networkx as nx
import matplotlib.pyplot as plt

def create_wait_for_graph(num_philosophers):
    G = nx.DiGraph()

    # Add nodes for each philosopher
    for i in range(num_philosophers):
        G.add_node(i)

    # Add edges to represent the wait-for relationship
    for i in range(num_philosophers):
        left = i
        right = (i + 1) % num_philosophers
        G.add_edge(left, right)

    return G

def find_cycles_in_graph(G):
    cycles = list(nx.simple_cycles(G))
    return cycles

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", arrows=True)
    plt.title("Wait-for Graph")
    plt.show()


def main():
    # Testing for n philosophers
    num_philosophers = 5  
    G = create_wait_for_graph(num_philosophers)

    cycles = find_cycles_in_graph(G)

    # Print the cycles (deadlocks)
    if cycles:
        print("Deadlock detected! Cycles in the graph:")
        for cycle in cycles:
            result = cycles[0]
            result.append(cycles[0][0])
            print(result)
    else:
        print("No deadlocks detected!")

    # Visualize
    visualize_graph(G)


if __name__ == "__main__":
    main()