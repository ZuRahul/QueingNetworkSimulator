class Node:
    '''
        id:
        link:
    '''

    def __init__(self, id):
        self.id = id

    def add_link(self, link):
        self.link = link


class System(Node):
    pass 


class Link:
    '''
        Length:
        Speed: 
    '''

    def __init__(self, speed, length):
        self.speed = speed
        self.length = length


class Packet:
    '''
        size:
        src:
        dest:
    '''

    def __init__(self, size, src, dst):
        self.size = size 
        self.src = src 
        self.dst = dst 

    def run(self):
        pass 


class Queue:
    queue = []

    def __init__(self, size):
        self.size = size

    def push(self, pck):
        if len(self.queue) == self.size:
            return False
        self.queue.append(pck)
        return True

    def pop(self):
        return self.queue.pop(0)


class Switch:

    def __init__(self):
        pass


class Router:

    def __init__(self):
        pass

