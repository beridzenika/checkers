class Moves():
    def __init__(self, from_pos, to_pos, captured=None):
        self.from_pos=from_pos
        self.to_pos=to_pos
        self.captured=captured