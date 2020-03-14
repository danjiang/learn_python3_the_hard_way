class Room(object):
    """docstring for Room"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        """docstring for go"""
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """docstring for add_paths"""
        self.paths.update(paths)
