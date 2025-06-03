import time as ti


class MyQueue(object):
    """
    My Queue class

    Attributes:
        queue: queue
        head
        tail
    """

    def __init__(self):
        """Constructor
        """
        self.length = 50010
        self.queue = [0] * self.length
        # counter = 0
        # while counter < self.length:
        #     self.queue.append(Process())
        #     counter += 1
        self.head = 0
        self.tail = 0

    # def enqueue(self, name, time):
    def enqueue(self, process):
        """enqueue method

        Args:
            name: enqueued process name
            time: enqueued process time

        Returns:
            None
        """
        self.queue[self.tail] = process
        # self.queue[self.tail].name = name
        # self.queue[self.tail].time = time
        self.tail = (self.tail + 1) % self.length

    def dequeue(self):
        """dequeue method

        Returns:
            None
        """
        # self.queue[self.head].name = ""
        # self.queue[self.head].time = 0
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.length

    def is_empty(self):
        """check queue is empty or not

        Returns:
            Bool
        """
        if self.head == self.tail:
            return True
        else:
            return False

    def is_full(self):
        """chech whether queue is full or not"""
        if self.tail - self.head >= len(self.queue):
            return True
        else:
            return False


class Process(object):
    """process class
    """

    def __init__(self, name="", time=0):
        """constructor
        Args:
            name: name
            time: time
        """
        self.name = name
        self.time = time

    def forward_time(self, time):
        """time forward method

        Args:
            time: forward time interval

        Returns:
            remain time

        """
        self.time -= time
        return self.time


def time_forward(my_queue, interval, current_time,):
    """

    Args:
        my_queue: queue
        interval: time step interval
        current_time: current time
    """

    value = my_queue.queue[my_queue.head].forward_time(interval)
    if value <= 0:
        current_time += (interval + value)
        print my_queue.queue[my_queue.head].name, current_time
        my_queue.dequeue()

    elif value > 0:
        current_time += interval
        # name, time = my_queue.queue[my_queue.head].name, \
        #              my_queue.queue[my_queue.head].time
        my_queue.enqueue(my_queue.queue[my_queue.head])
        my_queue.dequeue()

    return current_time


my_queue = MyQueue()
n, q = [int(x) for x in raw_input().split()]
counter = 0
while counter < n:
    name, time = raw_input().split()

    my_queue.enqueue(Process(name, int(time)))
    counter += 1

# end_time_list = []
current_time = 0
while not my_queue.is_empty():
    current_time = time_forward(my_queue, q, current_time)