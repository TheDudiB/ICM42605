from serial import Serial, SerialException
from multiprocessing import Value, Process, Pipe
from ctypes import c_bool
from time import sleep


class GetValue():
    def __init__(self, com, dic=False, m_processing=True):
        """GetValue(com, dic=False, m_processing=True)
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
            sleep(0.01)
            self.p_con.close()
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
            if self.p_con.poll(0):
                data = self.p_con.recv()
            else:
                data = None
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

    def data_ready(self):
        if self.p_con.poll(0):
            return True
        else:
            return False

    def read_line(self):
        return self.__next__()

    next = __next__


def m_serial(com, flag, pipe):
    with Serial(com, baudrate=921600, timeout=1) as ser:
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        print('clear buffer')
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
                if len(data) == 9:
                    pipe.send(data)
    pipe.close()


def test_con(com):
    try:
        with Serial(com, baudrate=921600, timeout=1) as ser:
            ser.reset_input_buffer()
            _ = ser.readline()
            read = ser.readline()
            if read:
                return True
            else:
                return False
    except SerialException:
        return False

if __name__ == '__main__':
    with GetValue('/dev/ttyUSB0') as val, open('out.csv', 'w') as f:
        f.write('time, accx, accy, accz, temp, gyorx, gyroy, gyroz\n')
        print(next(val))
        for i in range(10000):
            a = next(val)
            if a:
                f.write(','.join([str(x) for x in a])+'\n')
