'''
Semaphore Visualizer

Copyright Sabrina Button - 2024

Description: This visualizer demonstrates the Semaphore Algorithm. I made this to help myself
understand process synchronization for ELEC 377 (Operating Systems).
'''

import threading
import time
import matplotlib.pyplot as plt

# Change these values to see how the algorithm behaves
# with different time constraints
CRITICAL_SECTION_TIME = 1
REMAINDER_SECTION_TIME = 1
    
class SemaphoreVisualizer:
    def __init__(self):
        self.semaphore = threading.Semaphore()
        self.threads = []
        self.transitions = []
        self.stop = False
        self.threads.append(threading.Thread(target=self.thread0))
        self.threads.append(threading.Thread(target=self.thread1))
        self.threads[0].start()
        self.threads[1].start()
        
    def thread0(self):
        while True:
            self.semaphore.acquire()
            self.critical_section(0)
            self.semaphore.release()
            self.remainder_section(0)
            
    def thread1(self):
        while True:
            self.semaphore.acquire()
            self.critical_section(1)
            self.semaphore.release()
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
        
    def visualize(self):
        fig, ax = plt.subplots()
        for i, transition in enumerate(self.transitions):
            if transition[1] == 'critical':
                ax.plot([i, i+1], [transition[0], transition[0]], 'r-')
            else:
                ax.plot([i, i+1], [transition[0], transition[0]], 'b-')
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['Thread 0', 'Thread 1'])
        ax.set_xlabel('Time')
        ax.set_title('Semaphore Algorithm')
        plt.show()

visualizer = SemaphoreVisualizer()
time.sleep(10)
visualizer.visualize()
    