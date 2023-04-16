from network import Node, Link, Packet, Queue


class DirectLink(Link):
    '''
        nodeA: 
        nodeB: 
    '''

    def __init__(self, speed, length, nodeA, nodeB):
        Link.__init__(speed, length)
        
        self.nodeA = nodeA 
        self.nodeB = nodeB 

        nodeA.add_link(self)
        nodeB.add_link(self)

