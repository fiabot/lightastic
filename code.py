from adafruit_circuitplayground.express import cpx
import time
import random

class NeopixelPattern:
     def __init__(self):
         #basic colors
         self.red = (255,0,0)
         self.orange = (255,127,0)
         self.yellow = (255,255,0)
         self.yellow_green = (127,255,0)
         self.green = (0,255,0)
         self.green_blue = (0,127,127)
         self.blue = (0,0,255)
         self.blue_purple = (127,0,255)
         self.purple = (225,0,255)
         self.red_purple = (255,0,127)

         #pattern color range
         self.colors = [self.red,self.orange,self.yellow,self.yellow_green,
         self.green,self.green_blue,self.blue,self.blue_purple,self.purple,self.red_purple]
         #current frame number
         self.frame = 0

         #wait times for animation
         self.smooth_time = 0.01
         #self.pulse_time_start = 0.4
         #self.pulse_time_end = 0.4
         self.transition_time = 1

         #pixel brightness
         self.brightness = 0.3
         cpx.pixels.brightness = self.brightness

         #automatic pattern type
         self.auto_patt = "fism" #spin smooth

         #solid pattern
         self.color_count = 0
         self.num_colors = 10
         self.num_steps = self.transition_time/ self.smooth_time
         self.cur_step = 0
         self.cur_brightness = self.brightness

         self.fade_in = False


     """def show_base_frame(self):
         for i in range(10):
             cpx.pixels[i] = self.colors[i]"""

     """def update_frame_spin(self):
         add_value = self.frame
         for i in range(10):
             if i + add_value >= 10:
                 add_value = -i
             cpx.pixels[i+add_value] = self.colors[i]
             #print(add_value)

         self.frame += 1
         if self.frame >= 10:
             self.frame = 0"""

     def update_frame_random(self):
         for i in range(10):
             cpx.pixels[i] = self.colors[random.randint(0,9)]

     """def display_spin_smooth(self):
         self.update_frame_spin()
         time.sleep(self.smooth_time)"""

     def display_spin_pulse(self):
         self.update_frame_spin()
         time.sleep(self.pulse_time)
         cpx.pixels.fill((0,0,0))
         time.sleep(self.pulse_time)

     def display_rand_smooth(self):
         self.update_frame_random()
         time.sleep(self.smooth_time)

     def display_rand_pulse(self):
         self.update_frame_random()
         time.sleep(self.pulse_time_start)
         cpx.pixels.fill((0,0,0))
         time.sleep(self.pulse_time_end)

     def display_fill_smooth(self, random = False):
         if self.color_count == (self.num_colors-1):
             r_dif = (self.colors[self.color_count][0] - self.colors[0][0])\
              / self.num_steps * self.cur_step
             g_dif = (self.colors[self.color_count][1] - self.colors[0][1])\
                  / self.num_steps * self.cur_step
             b_dif = (self.colors[self.color_count][2] - self.colors[0][2])\
                  / self.num_steps * self.cur_step
         else:
             r_dif = (self.colors[self.color_count][0] - self.colors[self.color_count+1][0])\
                  / self.num_steps * self.cur_step
             g_dif = (self.colors[self.color_count][1] - self.colors[self.color_count+1][1])\
                  / self.num_steps * self.cur_step
             b_dif = (self.colors[self.color_count][2] - self.colors[self.color_count+1][2])\
                  / self.num_steps * self.cur_step

         r = int(self.colors[self.color_count][0] - r_dif)
         g = int(self.colors[self.color_count][1] - g_dif)
         b = int(self.colors[self.color_count][2] - b_dif)
         color = (r,g,b)

         #color = self.colors[self.color_count]

         cpx.pixels.fill(color)
         self.cur_step += 1
         if self.cur_step > self.num_steps:
             self.cur_step = 0
             self.color_count += 1

             if self.color_count >= (self.num_colors):
                 self.color_count = 0
         time.sleep(self.smooth_time)

     def display_fill_pulse(self, random = False):
         color = self.colors[self.color_count]
         cpx.pixels.brightness = self.cur_brightness
         """ r = int(color[0]/(1-self.cur_brightness))
         g= int(color[1]/(1-self.cur_brightness))
         b = int(color[2]/(1-self.cur_brightness))
         color =(r,g,b)"""
         cpx.pixels.fill(color)

         step = (self.brightness)/ self.num_steps

         if self.fade_in:
             self.cur_brightness += step
         else:
             self.cur_brightness -= step


         self.cur_step += 1
         if self.cur_step > self.num_steps:
             print(self.cur_brightness)
             self.cur_step = 0

             self.fade_in = not self.fade_in
             if self.fade_in:
                self.color_count += 1

             if self.color_count >= (self.num_colors):
                 self.color_count = 0

         time.sleep(self.smooth_time)

     def display_auto(self):
         if self.auto_patt == "spsm":
             self.display_spin_smooth()
         elif self.auto_patt == "sppu":
             self.display_spin_pulse()
         elif self.auto_patt == "rasm":
             self.display_rand_smooth()
         elif self.auto_patt == "rapu":
             self.display_rand_pulse()
         elif self.auto_patt == "fism":
             self.display_fill_smooth()
         else:
             self.display_fill_pulse()


fire = NeopixelPattern()
fire.colors= (fire.red, fire.red, fire.red,fire.orange,fire.orange,
fire.orange,fire.yellow,fire.yellow,fire.yellow,fire.yellow)
fire.smooth_time = 0.3
fire.auto_patt = "rasm"

rainbow = NeopixelPattern()

siren = NeopixelPattern()
siren.colors = (siren.blue,siren.red)
siren.num_colors = 2
siren.smooth_time = 0.0001
siren.num_steps = 0.0005 / siren.smooth_time
siren.auto_patt = "fipu"

cool = NeopixelPattern()
cool.colors = (cool.green_blue,cool.blue,cool.blue_purple, cool.purple,
    cool.red_purple)
cool.num_colors = 5


party = NeopixelPattern()
party.auto_patt = "fipu"
party.smooth_time = 0.0001
party.num_steps = 0.0005 / party.smooth_time

pattern_list = [rainbow,fire,siren, cool,party]

pattern = 3
while True:
     pattern_list[pattern].display_auto()
     if cpx.tapped:
        pattern += 1
        if pattern >= 5:
            cpx.pixels.brightness = 0.3
            pattern = 0