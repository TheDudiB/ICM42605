from serial import Serial
from multiprocessing import Value, Process, Pipe
from ctypes import c_bool


class getValue():
    def __init__(self, com, dic=False, m_processing=True):
        """getValue(com, dic=False, m_processing=True)
        Reads the ICM42605 raw regesters
        com: Com port to comunicate with the eval board
        dic: If true return values as dictenary
        m_processing: If true works with multiprosesing"""
        self.com = com
        self.i = 0
        self.ser = None
        self.dic = dic
        if m_processing:
            self.stop_flag = Value(c_bool, True)
        self.m_processing = m_processing

    def __enter__(self):
        if self.m_processing:
            self.stop_flag.value = 1
            self.p_con, self.c_con = Pipe()
            self.process = Process(target=m_serial,
                                   args=(self.com,
                                         self.stop_flag,
                                         self.c_con,))
            self.process.start()
        else:
            self.ser = Serial(self.com, baudrate=921600, timeout=1)
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if self.m_processing:
            self.stop_flag.value = 0  # Turn off process
        if exception_type is None:
            if self.ser:
                self.ser.close()
                if not self.ser.closed:
                    return False
                return True

    def __iter__(self):
        if not self.m_processing:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        return self

    def __next__(self):
        if self.m_processing:
            data = self.p_con.recv()
        else:
            read = self.ser.readline()
            while '[I]' != read[:3] or '\n' != read[-1]:
                read = self.ser.readline()
            data = read[3:].strip().replace(':', ',')
            data = [int(x) for x in data.split(',')]
            self.i += 1

        if self.dic:
            return {'time': data[0],
                    'accx': data[1],
                    'accy': data[2],
                    'accz': data[3],
                    'temp': data[4],
                    'gyrox': data[5],
                    'gyroy': data[6],
                    'gyroz': data[7]}
        else:
            return data

    def start(self):
        self.__enter__()

    def stop(self):
        self.__exit__(None, None, None)

    next = __next__


def m_serial(com, flag, pipe):
    ser = Serial(com, baudrate=921600, timeout=1)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    while flag.value:
        read = ser.readline()
        while '[I]' != read[:3] or '\n' != read[-1]:
            read = ser.readline()
        data = read[3:].strip().replace(':', ',')
        try:
            data = [int(x) for x in data.split(',')]
        except ValueError:
            pass
        else:
            pipe.send(data)
    pipe.close()


if __name__ == '__main__':
    with getValue('/dev/ttyUSB0') as val, open('out.csv', 'w') as f:
        f.write('time, accx, accy, accz, temp, gyorx, gyroy, gyroz\n')
        print(next(val))
        for i in range(10000):
            f.write(','.join([str(x) for x in next(val)])+'\n')
