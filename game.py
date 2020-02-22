'''Creates Fish Game
made Fall 2017
Final Project
@author Annika Johnson (agj4)'''

from tkinter import *
from random import randint
from fish import *


class Game:
    ''' Creates Fish Game'''
    
    def __init__ (self, window):
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self._width = 1000
        self._hight = self._width // 2
        self._canv = Canvas(self.window, bg='sky blue',
                        width=self._width, height=self._hight)
        self._canv.pack()
        button = Button(self.window, text='New Game', command=self.new_game)
        button.pack()
        
        self._game_over = False
        self._game_won = False
        self._fish_list = []
        self._player = Fish(self._canv, self._width/2, self._hight/2, 0, 0, 15, self.get_random_color(), 'right')
        self._canv.bind("<Key>", self.player_move)
        self._canv.bind("<KeyRelease>", self.player_stop)
        self._canv.bind("<space>", self.new_game)
        
        self._canv.focus_set()
        
        self.animate()
        
    
    def animate (self):
        ''' Animates fish'''
        if not self._game_over and not self._game_won:
            self.add_fish( )
            self._canv.delete(ALL)
            self._player.move()
            self._player.draw_fish()
            for fish in self._fish_list:
                fish.move()
                fish.draw_fish()
            self.check_off_screen()
            self.check_collision()
            self.check_win_condition()
            self._canv.after(40, self.animate)
        elif self._game_over:
            self._canv.create_text(self._width/2, self._hight * 3/8, text = "Game Over", font = ('Arial', 30))
            self._canv.create_text(self._width/2, self._hight/2, text = "you've been eaten", font = ('Arial', 20))
        elif self._game_won:
            self._canv.create_text(self._width/2, self._hight * 3/8, text = "Victory", font = ('Arial', 30))
            self._canv.create_text(self._width/2, self._hight/2, text = "you've become the largest fish in the pond", font = ('Arial', 20))
            
    def add_fish (self):
        ''' Adds fish along the y access on either side of the screen
        staggers fish creation,  only 16 fish max
        when there are at least 15 fish on screen the last fish is more likely to be smaller than player'''
        if len(self._fish_list) < 16:
            if randint(0, 100) > 80:
                if len(self._fish_list) == 15 and self._player.get_size() < 40 and randint(0, 100) > 80:
                    sz = randint(10, self._player.get_size())
                else:
                    sz = randint(10, 175)
                
                if randint(0, 1) == 0: #left side of screen
                    self._fish_list.append(Fish(self._canv, -1/2 * sz, randint(5, self._hight - 5), 
                                                randint(2, 6), 0, sz, self.get_random_color(), 'right'))
                else: #right side of the screen
                    self._fish_list.append(Fish(self._canv, self._width + 1/2 * sz, randint(5, self._hight - 5), 
                                                -(randint(2, 6)), 0, sz, self.get_random_color(), 'left'))
            
    def check_off_screen (self):
        ''' Checks if any fish is off screen
        if player is off screen then player is moved to the opposite side
        if any other fish then it is deleted'''
        for fish in self._fish_list[:]:
            if fish.get_x() < -fish.get_size()/2 or fish.get_x() > self._width + fish.get_size()/2:
                self._fish_list.remove(fish)
        if self._player:
            if self._player.get_x() < -(3/4 * self._player.get_size()):
                self._player.set_x(self._width + self._player.get_size()/4)
            elif self._player.get_x() > self._width + 3/4 * self._player.get_size():
                self._player.set_x(-(self._player.get_size()/4))
            
            if self._player.get_y() < -(3/8 * self._player.get_size()):
                self._player.set_y(self._hight + self._player.get_size()/8)
            elif self._player.get_y() > self._hight + 3/8 * self._player.get_size():
                self._player.set_y(-(self._player.get_size()/8))
                
    def check_collision (self):
        ''' Checks if player hits another fish and if so compares the two fish
        if the player is larger it eats other fish
        if the player is smaller it causes a game over'''
        for fish in self._fish_list[:]:
            if self._player.hit(fish):
                if self._player > fish:
                    self._player.set_size(self._player.get_size() + fish.get_size() // 10)
                    self._fish_list.remove(fish)
                else:
                    self._game_over = True
                    
    def check_win_condition (self):
        ''' Causes player to win when it gets past a certain size'''
        if self._player.get_size() > self._hight / 2:
            self._game_won = True
                
    def player_move (self, event):
        ''' Changes player fish's X/Y velocities based on arrow keys'''
        if event.keysym == 'Up':
            self._player.set_Yvel(-7)
        elif event.keysym == 'Down':
            self._player.set_Yvel(7)
        if event.keysym == 'Right':
            self._player.set_direction('right')
            self._player.set_Xvel(7)
        elif event.keysym == 'Left':
            self._player.set_direction('left')
            self._player.set_Xvel(-7)
    
    def player_stop (self, event):
        ''' When arrow key is released X/Y velocities are reset to 0'''
        if event.keysym == 'Up' or event.keysym == 'Down':
            self._player.set_Yvel(0)
        if event.keysym == 'Right' or event.keysym == 'Left':
            self._player.set_Xvel(0)
    
    def new_game (self, event = None):
        ''' Resets the entire game'''
        self._fish_list = []
        self._player = Fish(self._canv, self._width/2, 1/2 * self._hight, 0, 0, 15, self.get_random_color(), 'right')
        if self._game_over or self._game_won:
            self._game_won = False
            self._game_over = False
            self.animate()
    
    def get_random_color(self):
        ''' Generate random color intensities for red, green & blue and convert them to hex. '''
        return '#{:02X}{:02X}{:02X}'.format(randint(0,255), randint(0,255), randint(0,255))
    
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Fish Game')    
    app = Game(root)
    root.mainloop()
    