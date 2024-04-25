def initialize_processes(total_processes):
    processes = [{'id': i, 'active': True} for i in range(total_processes)]
    return processes

def fetch_maximum_active_process(processes):
    max_id = -1
    max_index = -1
    for i, process in enumerate(processes):
        if process['active'] and process['id'] > max_id:
            max_id = process['id']
            max_index = i
    return max_index

def election(processes, initialized_process):
    print("Process no {} fails".format(processes[fetch_maximum_active_process(processes)]['id']))
    processes[fetch_maximum_active_process(processes)]['active'] = False
    print("Election Initiated by", initialized_process)

    old = initialized_process
    newer = (old + 1) % len(processes)

    while True:
        if processes[newer]['active']:
            print("Process {} pass Election({}) to process {}".format(processes[old]['id'], processes[old]['id'], processes[newer]['id']))
            old = newer
        newer = (newer + 1) % len(processes)
        if newer == initialized_process:
            break

    coordinator_index = fetch_maximum_active_process(processes)
    print("Process {} becomes coordinator".format(processes[coordinator_index]['id']))

    old = coordinator_index
    newer = (old + 1) % len(processes)
    while True:
        if processes[newer]['active']:
            print("Process {} pass Coordinator({}) message to process {}".format(processes[old]['id'], processes[processes[old]['id']]['id'], processes[newer]['id']))
            old = newer
        newer = (newer + 1) % len(processes)
        if newer == coordinator_index:
            print("End Of Election ")
            break

def main():
    total_processes = 5
    processes = initialize_processes(total_processes)
    initialized_process = 2
    election(processes, initialized_process)

if __name__ == "__main__":
    main()
