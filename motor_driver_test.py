import RPi.GPIO as G
import time
class moto():
   def __init__(self):
      self.in1 = 11   # 对应stp2
      self.in2 = 12   # 对应dir2
      self.in3 = 13   # 对应stp1
      self.in4 = 15   # 对应dir1
      G.setmode(G.BOARD)
      G.setup(self.in1,G.OUT)
      G.setup(self.in4,G.OUT)
      G.setup(self.in3,G.OUT)
      G.setup(self.in2,G.OUT)
   def set_up(self,w1,w2,w3,w4):
      G.output(self.in1,w1)
      G.output(self.in2,w2)
      G.output(self.in3,w3)
      G.output(self.in4,w4)
   def stop(self):
      self.set_up(0,0,0,0)
   def run(self):
      self.set_up(0,0,0,1)
      time.sleep(0.001)
      self.set_up(1,0,1,1)
      time.sleep(0.001)
   def back(self):
      self.set_up(0,1,0,0)
      time.sleep(0.001)
      self.set_up(1,1,1,0)
      time.sleep(0.001)
   def left(self):
      self.set_up(0,0,0,0)
      time.sleep(0.001)
      self.set_up(1,0,1,0)
      time.sleep(0.001)
   def right(self):
      self.set_up(0,1,0,1)
      time.sleep(0.001)
      self.set_up(1,1,1,1)
      time.sleep(0.001)
      
   def move_forward(self, time_s):
      time_start = time.time()
      time_end = time_start
      while ((time_s/100) > float(time_end-time_start)):
         self.run()
         time_end = time.time()

   def move_back(self, time_s):
      time_start = time.time()
      time_end = time_start
      while ((time_s/100) > float(time_end-time_start)):
         self.back()
         time_end = time.time()

   def turn_left(self, time_s):
      time_start = time.time()
      time_end = time_start
      while ((time_s/100) > float(time_end-time_start)):
         self.left()
         time_end = time.time()

   def turn_right(self, time_s):
      time_start = time.time()
      time_end = time_start
      while ((time_s/100) > float(time_end-time_start)):
         self.right()
         time_end = time.time()


if __name__=='__main__':
   time.sleep(5)
   a = moto()
   a.move_forward(300)
   time.sleep(1)
   a.move_back(300)
   time.sleep(1)
   a.turn_left(300)
   time.sleep(1)
   a.turn_right(300)
   time.sleep(1)
   a.turn_right(300)
