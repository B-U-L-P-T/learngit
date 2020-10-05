import RPi.GPIO as G
import time
class motor():
    def __init__():
        self.stp_2 = 11
        self.dir_2 = 12
        self.stp_1 = 13
        self.dir_1 = 15
        G.setmode(G.BOARD)
        G.setup(self, stp_2, G.OUT)
        G.setup(self, dir_2, G.OUT)
        G.setup(self, stp_1, G.OUT)
        G.setup(self, dir_1, G.OUT)
