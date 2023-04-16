from network import Node, Link, Packet, Queue


class BackBone(Link):
    '''
        links: map<coordinate, DropLine>
    '''

    links = {}

    def __init__(self, speed, length):
        Link.__init__(speed, length)

    def add_dropline(self, dropline):
        self.links[dropline.coordinate] = dropline


class DropLine(Link):
    '''
        Coordinate:
        BackBone:
        Node:
    '''

    def __init__(self, speed, length, backbone, coordinate, node):
        Link.__init__(speed, length)
        
        self.coordinate = coordinate
        self.backbone = backbone 
        self.node = node 

        node.add_link(self)
        backbone.add_dropline(self)


