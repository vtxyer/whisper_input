import multiprocessing

class MultiprocessingHandler:
    def __init__(self):
        self.processes = []

    def start_process(self, target):
        # Create a new process and start it
        process = multiprocessing.Process(target=target)
        process.start()
        self.processes.append(process)

    def stop_all_processes(self):
        # Stop all running processes
        for process in self.processes:
            process.terminate()
            process.join()
