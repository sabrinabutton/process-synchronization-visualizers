'''
Peterson's Algorithm Critical Section Visualizer

Copyright Sabrina Button - 2024

Description: This visualizer demonstrates the Peterson's Algorithm for mutual exclusion. I made this to help myself 
understand process synchronization for ELEC 377 (Operating Systems).

The algorithm is used to solve the critical section problem in concurrent programming. It holds the properties of 
mutual exclusion, progress, but struggles with bounded wait. Feel free to change the CRITICAL_SECTION_TIME and 
REMAINDER_SECTION_TIME to see how the algorithm behaves with different time constraints.
'''

import threading
import time
import matplotlib.pyplot as plt

# Change these values to see how the algorithm behaves
# with different time constraints
CRITICAL_SECTION_TIME = 1
REMAINDER_SECTION_TIME = 1

class PetersonsCriticalSectionVisualizer:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0
        self.threads = []
        self.transitions = []  # To store the transitions for visualization
        self.stop = False
        self.threads.append(threading.Thread(target=self.thread0))
        self.threads.append(threading.Thread(target=self.thread1))
        self.threads[0].start()
        self.threads[1].start()

    def thread0(self):
        while True:
            self.flag[0] = True # Flag indicates that the thread wants to enter the critical section
            self.turn = 1 # It's the other thread's turn
            while self.flag[1] and self.turn == 1: # If the other thread wants to enter the critical section and it's the other thread's turn
                pass
            self.critical_section(0) # Critical section
            self.flag[0] = False # Done with the critical section
            self.remainder_section(0)

    def thread1(self):
        while True: # Same as thread0, but flag is 1
            self.flag[1] = True 
            self.turn = 0
            while self.flag[0] and self.turn == 0: 
                pass
            self.critical_section(1)
            self.flag[1] = False
            self.remainder_section(1)

    # Sleep for CRITICAL_SECTION_TIME seconds to simulate the thread executing the critical section
    def critical_section(self, thread_id):
        t = len(self.transitions) + 1
        print("[ t = ", t, "]", "Thread", thread_id, "entering critical section")
        self.transitions.append((thread_id, 'critical'))
        time.sleep(CRITICAL_SECTION_TIME)
        print("[ t = ", t, "]","Thread", thread_id, "leaving critical section")

    # Sleep for REMAINDER_SECTION_TIME seconds to simulate the thread executing the remainder section
    def remainder_section(self, thread_id):
        t = len(self.transitions) + 1
        print("[ t = ", t, "]","Thread", thread_id, "entering remainder section")
        self.transitions.append((thread_id, 'remainder'))
        time.sleep(REMAINDER_SECTION_TIME)
        print("[ t = ", t, "]","Thread", thread_id, "leaving remainder section")

    # Plots the critical section transitions of the threads
    def visualize(self):
        times = list(range(len(self.transitions)))
        thread0_sections = [1 if t[0] == 0 and t[1] == 'critical' else 0 for t in self.transitions]
        thread1_sections = [1 if t[0] == 1 and t[1] == 'critical' else 0 for t in self.transitions]

        plt.plot(times, thread0_sections, label='Thread 0 Critical Section')
        plt.plot(times, thread1_sections, label='Thread 1 Critical Section')
        plt.xlabel('Time')
        plt.ylabel('Critical Section')
        plt.title('Peterson\'s Algorithm Section Transitions')
        plt.legend()
        plt.show()

visualizer = PetersonsCriticalSectionVisualizer()
time.sleep(10)  # Let the threads run for a while
visualizer.visualize()
