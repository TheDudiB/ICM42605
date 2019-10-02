from multiprocess import Process, Pipe, Value
from ctypes import c_bool


class parllelFile():
    def __init__(self, file_name):
        self.file_name = file_name
        self.pipe_out, self.pipe_in = None, None
        self.run_flag = Value(c_bool, 1)

    def start(self):
        self.run_flag.value = 1
        self.pipe_out, self.pipe_in = Pipe()
        self.pro = Process(writeToFile, (self.file_name,
                                         self.pipe_in,
                                         self.run_flag,))
        self.pro.start()

    def stop(self):
        self.run_flag.value = 0

    def send(self, line):
        if self.run_flag.value and self.pipe_out:
            self.pipe_out.send(line)
        else:
            print('did not start')


def writeToFile(file_name, pipe_in, run_flag):
    with open(file_name, 'w') as f:
        f.write('time, accx, accy, accz, temp, gyorx, gyroy, gyroz\n')
        while run_flag.value:
            line = pipe_in.recv()
            line = [str(x) for x in line]
            f.write(','.join(line))
