'''Creates Fish class
made Fall 2017
Final Project
@author Annika Johnson (agj4)'''

import math

class Fish:
    def __init__ (self, canv, x, y, Xvel, Yvel, size, color = 'red', direction = 'right'):
        ''' Sets fish to given parameters'''
        self._canv = canv
        self._y = y
        self._x = x
        self._Xvel = Xvel
        self._Yvel = Yvel
        self._size = size
        self._color = color
        self._direction = direction
        
    def draw_fish (self):
        ''' draws fish based on size, color, and direction'''
        if self._direction == 'right':
            self._canv.create_oval(self._x + self._size/2, self._y + self._size/4, 
                                   self._x - self._size/4, self._y - self._size/4,
                                   width = 2, fill = self._color)
            self._canv.create_polygon(self._x - self._size/4, self._y, 
                                      self._x - self._size/2, self._y - self._size/4, 
                                      self._x - self._size/2, self._y + self._size/4,
                                      width = 2, outline = 'black', fill = self._color)
        else:
            self._canv.create_oval(self._x - self._size/2, self._y - self._size/4, 
                                   self._x + self._size/4, self._y + self._size/4,
                                   width = 2, fill = self._color)
            self._canv.create_polygon(self._x + self._size/4, self._y, 
                                      self._x + self._size/2, self._y - self._size/4, 
                                      self._x + self._size/2, self._y + self._size/4,
                                      width = 2, outline = 'black', fill = self._color)
   
    def get_x (self):
        ''' Returns X coordinate'''
        return self._x
    
    def get_y (self):
        ''' Returns Y coordinate'''
        return self._y
    
    def get_size (self):
        ''' Returns size of fish'''
        return self._size
    
    def get_direction (self):
        ''' Returns direction of fish'''
        return self._direction
    
    def set_x (self, new_x):
        ''' Sets new X coordinate'''
        self._x = new_x
        
    def set_y (self, new_y):
        ''' Sets new Y coordinate'''
        self._y = new_y
        
    def set_Xvel (self, new_Xvel):
        ''' Changes X velocity'''
        self._Xvel = new_Xvel
        
    def set_Yvel (self, new_Yvel):
        ''' Changes Y velocity'''
        self._Yvel = new_Yvel
        
    def set_direction (self, new_direction):
        self._direction = new_direction
        
    def set_size (self, new_size):
        self._size = new_size
        
    def move (self):
        ''' Moves based on the X and Y velocities'''
        self._x += self._Xvel
        self._y += self._Yvel
            
    
    def hit(self, other):
        '''Checks for collisions between fish'''
        if (self == other):
            return False
        if self._direction == 'right':
            if other.get_direction() == 'right': #self right, other right
                return (((self._size * 3/8 + other.get_size()* 3/8) #large box
                         >= math.fabs((self._x - self._size/8) - (other.get_x() - other.get_size()/8))
                        and (self._size/4 + other.get_size()/4)
                         >= math.fabs(self._y - other.get_y()))
                        or
                        ((self._size/8 + other.get_size()/8) #small box
                         >= math.fabs((self._x + self._size* 3/8) - (other.get_x() + other.get_size()* 3/8))
                        and (self._size/8 + other.get_size()/8)
                         >= math.fabs(self._y - other.get_y())))
            else: #self right, other left
                return (((self._size * 3/8 + other.get_size()* 3/8) #large box
                         >= math.fabs((self._x - self._size/8) - (other.get_x() + other.get_size()/8))
                        and (self._size/4 + other.get_size()/4)
                         >= math.fabs(self._y - other.get_y()))
                        or
                        ((self._size/8 + other.get_size()/8) #small box
                         >= math.fabs((self._x + self._size* 3/8) - (other.get_x() - other.get_size()* 3/8))
                        and (self._size/8 + other.get_size()/8)
                         >= math.fabs(self._y - other.get_y())))
        else:
            if other.get_direction() == 'right': #self left, other right
                return (((self._size * 3/8 + other.get_size()* 3/8) #large box
                         >= math.fabs((self._x + self._size/8) - (other.get_x() - other.get_size()/8))
                        and (self._size/4 + other.get_size()/4)
                         >= math.fabs(self._y - other.get_y()))
                        or
                        ((self._size/8 + other.get_size()/8) #small box
                         >= math.fabs((self._x - self._size* 3/8) - (other.get_x() + other.get_size()* 3/8))
                        and (self._size/8 + other.get_size()/8)
                         >= math.fabs(self._y - other.get_y())))
            else: #self left, other right
                return (((self._size * 3/8 + other.get_size()* 3/8) #large box
                         >= math.fabs((self._x + self._size/8) - (other.get_x() + other.get_size()/8))
                        and (self._size/4 + other.get_size()/4)
                         >= math.fabs(self._y - other.get_y()))
                        or
                        ((self._size/8 + other.get_size()/8) #small box
                         >= math.fabs((self._x - self._size* 3/8) - (other.get_x() - other.get_size()* 3/8))
                        and (self._size/8 + other.get_size()/8)
                         >= math.fabs(self._y - other.get_y())))
    
    def __gt__ (self, other):
        ''' Compares the sizes of 2 fish
        if fish compared is larger, fish size grows based on opponent size
        returns boolean statement'''
        return self._size > other.get_size()
        
