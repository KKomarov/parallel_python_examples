import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print('Called run method in process:', self.name)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        process = MyProcess()
        jobs.append(process)
        process.start()
        process.join()
