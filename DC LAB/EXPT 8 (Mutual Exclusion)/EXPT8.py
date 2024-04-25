import threading
import time

# Shared variables
token = True  # Assume initially one site has the token
sequence_number = 0
critical_section_busy = False

# Function to simulate entering the critical section
def enter_critical_section(site_id):
    global token, sequence_number, critical_section_busy
    print(f"Site {site_id} is requesting access to the critical section...")
    
    # Acquire the lock for updating shared variables
    with threading.Lock():
        if token and not critical_section_busy:
            # Grant access to the critical section
            print(f"Site {site_id} has entered the critical section")
            critical_section_busy = True
            time.sleep(1)  # Simulate some work in the critical section
            critical_section_busy = False
            
            # Release the token
            token = False
            sequence_number += 1
            print(f"Site {site_id} released the token with sequence number {sequence_number}")
            token = True
        else:
            print(f"Site {site_id} cannot enter the critical section now")

def main():
    # Create two threads to represent two sites
    site1_thread = threading.Thread(target=enter_critical_section, args=(1,))
    site2_thread = threading.Thread(target=enter_critical_section, args=(2,))
    
    # Start the threads
    site1_thread.start()
    site2_thread.start()
    
    # Wait for the threads to finish
    site1_thread.join()
    site2_thread.join()

    print("All threads finished execution")

if __name__ == "__main__":
    main()















# import threading
# import time

# # Shared resource
# shared_resource = 0

# # Create a lock
# lock = threading.Lock()

# # Function to simulate accessing the shared resource
# def update_shared_resource():
#     global shared_resource
#     # Acquire the lock
#     with lock:
#         print(f"Thread {threading.current_thread().name} acquired the lock")
#         # Simulate some work on the shared resource
#         time.sleep(1)
#         shared_resource += 1
#         print(f"Thread {threading.current_thread().name} updated the shared resource to {shared_resource}")
#     # Release the lock
#     print(f"Thread {threading.current_thread().name} released the lock")

# def main():
#     # Create two threads to update the shared resource
#     thread1 = threading.Thread(target=update_shared_resource, name="Thread1")
#     thread2 = threading.Thread(target=update_shared_resource, name="Thread2")

#     # Start the threads
#     thread1.start()
#     thread2.start()

#     # Wait for the threads to finish
#     thread1.join()
#     thread2.join()

#     print("All threads finished execution")

# if __name__ == "__main__":
#     main()
