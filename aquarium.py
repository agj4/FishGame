'''Creates an Aquarium
made Fall 2017
Final Project
@author Annika Johnson (agj4)'''

from tkinter import *
from random import randint
from fish import *

class Aquarium:
    ''' Creates aquarium'''
    def __init__ (self, window):
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self._width = 1500
        self._hight = self._width // 2
        self._canv = Canvas(self.window, bg='sky blue',
                        width=self._width, height=self._hight)
        self._canv.pack()
        
        self._fish_list = []
        self._max_fish = self._hight // 10
        self._smallest = 5
        self._largest = self._hight // 5
        self._slowest = 2
        self._fastest = 7

        self.animate()
        
    
    def animate (self):
        ''' Animates fish'''
        self.add_fish()
        self._canv.delete(ALL)
        for fish in self._fish_list:
            fish.move()
            fish.draw_fish()
        self.check_off_screen()
        self._canv.after(40, self.animate)
            
    def add_fish (self):
        ''' Adds fish along the y access on either side of the screen
        staggers fish creation'''
        if len(self._fish_list) < self._max_fish:
            if randint(0, 100) > 80:
                sz = randint(self._smallest, self._largest)
                if randint(0, 1) == 0: #left side of screen
                    self._fish_list.append(Fish(self._canv, -1/2 * sz, randint(5, self._hight - 5), 
                                                randint(self._slowest, self._fastest), 0, sz, 
                                                self.get_random_color(), 'right'))
                else: #right side of screen
                    self._fish_list.append(Fish(self._canv, self._width + 1/2 * sz, randint(5, self._hight - 5), 
                                                -(randint(self._slowest, self._fastest)), 0, sz, 
                                                self.get_random_color(), 'left'))
    
    def check_off_screen (self):
        ''' Checks if any fish is off screen
        if any fish is then it is deleted'''
        for fish in self._fish_list[:]:
            if fish.get_x() < -(fish.get_size()/2) or fish.get_x() > self._width + fish.get_size()/2:
                self._fish_list.remove(fish)
                
    def get_random_color(self):
        ''' Generate random color intensities for red, green & blue and convert them to hex. '''
        return '#{:02X}{:02X}{:02X}'.format(randint(0,255), randint(0,255), randint(0,255))
    
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Aquarium')    
    app = Aquarium(root)
    root.mainloop()
    