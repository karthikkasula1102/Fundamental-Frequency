# Finding Fundamental(Base)Frequency

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *  #Import Tk for GUI
from tkinter.filedialog import askopenfile
from scipy.fftpack import fft
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Automation Lab")

class Fundamentalfrequency:
    
    def __init__(self, parent):
        
        self.parent = parent
        
        self.button1 = Button(self.parent, text = 'choose file', command = self.mfileopen)
        self.button1.grid(column = 1, row = 0)
        
        self.text = Text(self.parent, height = 2, width = 20)
        self.text.grid(column = 2, row = 0)
        
        self.button2 = Button(self.parent, text = 'Read file', command = self.readFile)
        self.button2.grid(column = 1, row = 1)
        
        self.entry = Entry(self.parent)
        self.entry.grid(column = 1, row = 2)
        
        self.b = Button(self.parent, text="SamplingFrequency", width=20, command=self.calculations)
        self.b.grid(column = 1, row = 3)
        
        self.label = Label(self.parent, text = 'Enter Sampling Freq')
        self.label.grid(column = 0, row = 2)
        
        self.button3 = Button(self.parent, text = 'Display', command = self.display)
        self.button3.grid(column = 1, row = 4)
        
        self.text1 = Text(self.parent, height = 2, width = 10)
        self.text1.grid(column = 2, row = 4)
        
        self.label = Label(self.parent, text = 'Est. Base Freq')
        self.label.grid(column = 3, row = 4)
        
        

    
    def mfileopen(self):
        file1 = filedialog.askopenfile()
        self.file2 = file1.name
        f = open(self.file2, errors = 'ignore')
        print(self.file2)
        self.text.insert('end', str(self.file2) + '\n')
        
        
    def readFile(self):
        self.y = pd.read_excel(self.file2, header = None)
        self.y = self.y.iloc[0, :].values
        N  = len(self.y)
        print(N)
        
    
    def calculations(self):
        self.Fs=float(self.entry.get())  # Sampling frequency
        Ts = 1.0/self.Fs                 # sampling interval
        N  = len(self.y)                 # No. of samples
        self.t = np.linspace(0, N*Ts, N, endpoint = False) # time vector
        #ff = 10;   # frequency of the signal
        #y = A*np.sin(2*np.pi*ff*t) + 8*np.random.normal(0,1,len(t))
        k = np.arange(N)                 # frequency range
        T = N/self.Fs                    
        frq = k/T                        # two sides frequency range
        self.frq = frq[range(N//2)]      # one side frequency range
        
        Y = np.fft.fft(self.y)/N         # fft computing and normalization
        Y = Y[range(N//2)]               # To delete mirror values
        Y[0]=0                           # To delete high peak noise at f=0
        self.mY = abs(Y)                 # Magnitude values
        peak = max(self.mY)              # Selecting peak
        print(peak)
        locY = np.argmax(self.mY)        # To find location of peak
        self.frqY = self.frq[locY]       # To find index of that peak value
        print(self.frqY)
                
    def ploting(self):
        plt.figure(1)
        plt.subplot(2,1,1)
        plt.plot(self.t, self.y)
        plt.xlabel('time')
        plt.ylabel('amplitude')
        plt.show()
        #plt.figure(2)
        plt.subplot(2,1,2)
        plt.plot(self.frq,self.mY)
        plt.xlabel('frequency')
        plt.ylabel('magnitude')
        plt.show()
    
    def display(self):
        figure1 = plt.Figure(figsize=(6,6), dpi=100 )
        #plt.title('Fundamental Frequency')
        ax1 = figure1.add_subplot(2,1,1)
        self.figure = ax1.plot(self.t,self.y, color = 'g')
        scatter1 = FigureCanvasTkAgg(figure1, root) 
        scatter1.get_tk_widget().grid(column = 0, row=5)
        #ax1.legend() 
        ax1.set_xlabel('time')
        ax1.set_ylabel('amplitude')
        ax2 = figure1.add_subplot(2,1,2)
        ax2.plot(self.frq,self.mY, color = 'b')
        #ax1.legend() 
        ax2.set_xlabel('frequency')
        ax2.set_ylabel('magnitude')
        self.text1.insert('end', str(self.frqY) + '\n')


  





   



top = Fundamentalfrequency(root)                # Calling class
sampling = Entry(root)
root.mainloop()



