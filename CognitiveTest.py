'''
CognitiveTest.py
================
Author: Hasi

Rules:
-----
    * Select the color of the word display.
'''

from tkinter import *
import random, time
COLORS = ['red', 'green', 'yellow', 'blue', 'gold', 'purple', 'black', 'cyan']
TOTAL_QUESTIONS = 10
def shuffle(li):
    '''
    Returns shuffled list
    '''
    for i in range(len(li)):
        a = random.randint(0, len(li)-1)
        b = random.randint(0, len(li)-1)
        li[a], li[b] = li[b], li[a]
    return li

def average(li):
    '''
    Returns average of list
    '''
    a = 0
    for i in li:
        a += i
    return a/len(li)

class CognitiveTest:
    def __init__(self):
        '''
        Setup TopLevel window for the app
        '''
        self.score = 0
        self.TIME = []
        self.QUESTION = 0 # Number of questions asked
        self.tk = Tk()
        self.tk.title('Cognitive Test')
        self.tk.minsize(400, 200)
        self.tk.maxsize(600, 300)
        self.frame1()
        self.tk.mainloop()

    def frame1(self):
        '''
        Prints question and its options
        '''
        print('Question Number : {}'.format(self.QUESTION))
        if self.QUESTION == TOTAL_QUESTIONS:
            return self.frame3()
        self.QUESTION += 1
        self.c1 = random.choice(COLORS) # Color name
        self.c2 = random.choice(COLORS) # Text color
        self.options = []
        self.f1 = Frame()
        Label(self.f1, text='Cognitive Test', font='Helvetica 30').grid(row=0,column=0)
        self.l1 = Label(self.f1, font='Helvetica 20 bold')
        self.l1.grid(row=1, column=0)
        self.l1['text'] = self.c1.capitalize()
        self.l1['foreground'] = self.c2
        self.l2 = Label(self.f1, font='Helvetica 20 bold')
        self.l2.grid(row=1, column=1)
        self.l2['text'] = self.score
        
        self.options.append(self.c2.capitalize())
        # Make Sure there is no repitition in options
        while len(self.options) != 4:
            choice = random.choice(COLORS).capitalize()
            self.options.append(choice)
            for i in self.options:
                if self.options.count(i) > 1:
                    self.options.remove(i)
        self.f1.grid(row=0, column=0)

        # Options
        self.f2 = Frame()
        self.buttons = []
        commands = [self.__A, self.__B, self.__C, self.__D]
        #print(self.options)
        self.options = shuffle(self.options)
        #print(self.options)
        for i in range(len(self.options)):
            self.buttons.append(Button(self.f2, text=self.options[i], font='Helvetica 20 bold',command=commands[i]))
            self.buttons[i].grid(row=0, column=i)
            
        self.f2.grid(row=1, column=0)
        self.t1 = time.time()

    def frame3(self):
        self.f1.destroy()
        self.f2.destroy()
        self.f3 = Frame()
        Label(self.f3, text='Cognitive Test', font='Helvetica 30 bold').grid(row=0,column=0)
        Label(self.f3, text='Score', font='Helvetica 30').grid(row=1,column=0)
        Label(self.f3, text=self.score/self.QUESTION, font='Helvetica 30').grid(row=1,column=1)
        Label(self.f3, text='Time ', font='Helvetica 30').grid(row=2,column=0)
        Label(self.f3, text=str(average(self.TIME[1:]))[:5]+' seconds', font='Helvetica 30').grid(row=2,column=1)
        Button(self.f3, text='Retest', font='Helvetica 30 bold', command=self.__retest).grid(row=3, column=0)
        self.f3.grid(row=1, column=0)
        
    def __A(self):
        if self.buttons[0]['text'].lower() == self.c2:
            self.score += 1
        print ('A')
        self.t2 = time.time()
        self.TIME.append(self.t2-self.t1)
        self.f1.update()
        self.f1.destroy()
        self.f2.destroy()
        self.frame1()

    def __B(self):
        if self.buttons[1]['text'].lower() == self.c2:
            self.score += 1
        print ('B')
        self.t2 = time.time()
        self.TIME.append(self.t2-self.t1)
        self.f1.update()
        self.f1.destroy()
        self.f2.destroy()
        self.frame1()

    def __C(self):
        if self.buttons[2]['text'].lower() == self.c2:
            self.score += 1
        print ('C')
        self.t2 = time.time()
        self.TIME.append(self.t2-self.t1)
        self.f1.update()
        self.f1.destroy()
        self.f2.destroy()
        self.frame1()

    def __D(self):
        if self.buttons[3]['text'].lower() == self.c2:
            self.score += 1
        print ('D')
        self.t2 = time.time()
        self.TIME.append(self.t2-self.t1)
        self.f1.update()
        self.f1.destroy()
        self.f2.destroy()
        self.frame1()

    def __retest(self):
        self.f3.destroy()
        self.QUESTION = 0
        self.TIME = []
        self.score=0
        self.frame1()

if __name__ == '__main__':
    CognitiveTest()
