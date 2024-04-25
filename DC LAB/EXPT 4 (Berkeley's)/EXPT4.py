import time
from datetime import datetime

def synchronize(nodes_time):
    local_time = time.time()
    nodes_timestamps = [to_seconds(h, m, s) for h, m, s in nodes_time]
    
    average_offset = sum(nodes_timestamps) / len(nodes_timestamps) - local_time
    return local_time + average_offset

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return int(h), int(m), int(s)

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))

    nodes_time = []
    for i in range(num_nodes):
        h = int(input(f"Enter the hour for Node {i+1}: "))
        m = int(input(f"Enter the minute for Node {i+1}: "))
        s = int(input(f"Enter the second for Node {i+1}: "))
        nodes_time.append((h, m, s))

    synchronized_time = synchronize(nodes_time)

    print("\nSynchronized Time:")
    for i, (h, m, s) in enumerate(nodes_time, start=1):
        h_sync, m_sync, s_sync = to_hms(synchronized_time)
        print(f"Node {i}: {h_sync:02d}:{m_sync:02d}:{s_sync:02d}")

    added_minutes = int((synchronized_time - time.time()) / 60)
    print(f"\nAdded minutes to balance time: {added_minutes}")
