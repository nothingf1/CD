def distribute_tasks(num_servers, num_processes):
    tasks_per_server = [0] * num_servers
    current_server = 0

    for process in range(1, num_processes + 1):
        tasks_per_server[current_server] += 1
        current_server = (current_server + 1) % num_servers

    return tasks_per_server

if __name__ == "__main__":
    num_servers = int(input("Enter the number of servers: "))
    num_processes = int(input("Enter the number of processes: "))

    tasks_assigned = distribute_tasks(num_servers, num_processes)

    print("\nTasks distribution:")
    for i, tasks in enumerate(tasks_assigned, start=1):
        print(f"Server {i}: {tasks} tasks")
