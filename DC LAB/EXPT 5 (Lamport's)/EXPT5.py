def max1(a, b):
    """Returns the maximum of two values."""
    return max(a, b)

def display(p1, p2):
    """Prints the logical timestamps of events in P1 and P2."""
    print("\nThe timestamps of events in P1:")
    print(*p1)
    print("\nThe timestamps of events in P2:")
    print(*p2)

def lamport_logical_clock(e1, e2, m):
    """Calculates the logical timestamps of events."""
    p1 = [i + 1 for i in range(e1)]  # Initialize p1
    p2 = [i + 1 for i in range(e2)]  # Initialize p2
    
    for i in range(e1):
        for j in range(e2):
            if m[i][j] == 1:  # Message sent
                p2[j] = max1(p2[j], p1[i] + 1)
                p2[j + 1:] = [p2[k - 1] + 1 for k in range(j + 1, e2)]
            elif m[i][j] == -1:  # Message received
                p1[i] = max1(p1[i], p2[j] + 1)
                p1[i + 1:] = [p1[k - 1] + 1 for k in range(i + 1, e1)]
                
    display(p1, p2)

if __name__ == "__main__":
    e1 = int(input("Enter the number of events in process 1 (e1): "))
    e2 = int(input("Enter the number of events in process 2 (e2): "))
    m = []
    for i in range(e1):
        row = []
        for j in range(e2):
            value = int(input(f"Enter 1 if message is sent from e{i+1} to e{j+1}, -1 if received, 0 otherwise: "))
            row.append(value)
        m.append(row)
    lamport_logical_clock(e1, e2, m)
