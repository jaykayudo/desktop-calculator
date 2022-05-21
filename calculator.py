import tkinter as tk
import tkinter.ttk as ttk
import re

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Josho Calculator")
        self.resizable(False,False)
        self.frameHeight = 100
        self.buttonHeight = 1
        self.buttonWidth = 3
        self.fontsize = 25
        self.padxright = 20
        self.mathareacolor = '#d9dddc'
        self.activebuttoncolor = '#d9dddc'
        self.pady = 10
        self.fontFamily = None
        self.bgColor = '#5097a4'
        self.calcArea = tk.Text(self,bg = self.mathareacolor,height=2,width=15,font=(self.fontFamily,30),state='disabled',wrap=tk.NONE,borderwidth = 0,cursor = 'arrow')
        self.answerArea = tk.Text(self,bg = self.mathareacolor,height=2,width=15,font=(self.fontFamily,30),state='normal',wrap=tk.NONE,borderwidth = 0,cursor='arrow')
    
        self.answerArea.insert(1.0,"0")
        self.answerArea.config(state = 'disabled')
        self.scrollbar = tk.Scrollbar(self,command = self.calcArea.xview,orient = 'horizontal')
        self.calcArea.config(xscrollcommand= self.scrollbar.set)
        self.topFrame = tk.Frame(self,height=self.frameHeight,bg=self.bgColor) 
        self.middleFrame = tk.Frame(self,height=self.frameHeight,bg=self.bgColor)
        self.bottomFrame = tk.Frame(self,height = self.frameHeight,bg=self.bgColor)
        self.leastFrame = tk.Frame(self,height=self.frameHeight,bg=self.bgColor)
        self.topFrame.pack_propagate(0)
        self.calcArea.pack(side='top',anchor = "n",fill='x')
        self.answerArea.pack(side='top',anchor = "n",fill='x')
        self.scrollbar.pack(side='top',anchor='n',fill='x')
        self.topFrame.pack(side='top',anchor = 'n',fill='x')
        self.middleFrame.pack(side='top',anchor = 'n',fill='x')
        self.bottomFrame.pack(side='top',anchor = 'n',fill='x')
        self.leastFrame.pack(side='top',anchor = 'n',fill='x')
        self.number_button(font= (self.fontFamily,self.fontsize),width=self.buttonWidth,height=self.buttonHeight,activebackground = self.activebuttoncolor,highlightbackground = self.activebuttoncolor)
    
    def number_button(self,**kwargs):
        self.num1 = tk.Button(self.bottomFrame,text='1',command=self.num1command,**kwargs)
        self.num2 = tk.Button(self.bottomFrame,text='2',command=self.num2command,**kwargs)
        self.num3 = tk.Button(self.bottomFrame,text='3',command=self.num3command,**kwargs)
        self.num4 = tk.Button(self.middleFrame,text='4',command=self.num4command,**kwargs)
        self.num5 = tk.Button(self.middleFrame,text='5',command=self.num5command,**kwargs)
        self.num6 = tk.Button(self.middleFrame,text='6',command=self.num6command,**kwargs)
        self.num7 = tk.Button(self.topFrame,text='7',command=self.num7command,**kwargs)
        self.num8 = tk.Button(self.topFrame,text='8',command=self.num8command,**kwargs)
        self.num9 = tk.Button(self.topFrame,text='9',command=self.num9command,**kwargs)
        self.num0 = tk.Button(self.leastFrame,text='0',command=self.num0command,**kwargs)
        self.numequ = tk.Button(self.leastFrame,text='=',command=self.numequcommand,**kwargs)
        self.numpo = tk.Button(self.leastFrame,text='.',command=self.numpocommand,**kwargs)
        self.num1.pack(side='left',padx=(10,self.padxright),pady=10)
        self.num2.pack(side='left',padx=(0,self.padxright))
        self.num3.pack(side='left',padx=(0,self.padxright))
        self.num4.pack(side='left',padx=(10,self.padxright))
        self.num5.pack(side='left',padx=(0,self.padxright))
        self.num6.pack(side='left',padx=(0,self.padxright))
        self.num7.pack(side='left',padx=(10,self.padxright))
        self.num8.pack(side='left',padx=(0,self.padxright))
        self.num9.pack(side='left',padx=(0,self.padxright))
         
        self.num0.pack(side='left',padx=(10,self.padxright),pady=(0,self.pady))
        self.numpo.pack(side='left',padx=(0,self.padxright),pady=(0,self.pady))
        

        #arithemetic signs
        self.plussign = tk.Button(self.topFrame,text='+',command = self.plussigncommand,**kwargs)
        self.minussign = tk.Button(self.middleFrame,text='-',command=self.minussigncommand,**kwargs)
        self.dividesign = tk.Button(self.bottomFrame,text='/',command=self.dividesigncommand,**kwargs)
        self.timessign = tk.Button(self.leastFrame,text='x',command=self.timessigncommand,**kwargs)
        
        self.plussign.pack(side='left',padx=(0,self.padxright))
        self.minussign.pack(side='left',padx=(0,self.padxright))
        self.dividesign.pack(side='left',padx=(0,self.padxright))
        self.timessign.pack(side='left',padx=(0,self.padxright),pady=(0,self.pady))
        self.numequ.pack(side='left',padx=(0,self.padxright),pady=(0,self.pady))

        self.delsign = tk.Button(self.topFrame,text='DEL',command=self.delsigncommand,**kwargs)
        self.acsign = tk.Button(self.middleFrame,text='AC',command=self.acsigncommand,**kwargs)
        self.mplussign = tk.Button(self.bottomFrame,text='M+',command=self.mplussigncommand,**kwargs)
        self.mminussign = tk.Button(self.leastFrame,text='M-',command=self.mminussigncommand,**kwargs)


        self.delsign.pack(side='left',padx=(0,self.padxright))
        self.acsign.pack(side='left',padx=(0,self.padxright))
        self.mplussign.pack(side='left',padx=(0,self.padxright))
        self.mminussign.pack(side='left',padx=(0,self.padxright),pady=(0,self.pady))
    def num1command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'1')
        self.calcArea.config(state='disabled')
    def num2command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'2')
        self.calcArea.config(state='disabled')
    def num3command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'3')
        self.calcArea.config(state='disabled')
    def num4command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'4')
        self.calcArea.config(state='disabled')
    def num5command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'5')
        self.calcArea.config(state='disabled')
    def num6command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'6')
        self.calcArea.config(state='disabled')
    def num7command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'7')
        self.calcArea.config(state='disabled')
    def num8command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'8')
        self.calcArea.config(state='disabled')
    def num9command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'9')
        self.calcArea.config(state='disabled')
    def num0command(self):
        self.calcArea.config(state='normal')
        self.calcArea.insert(tk.END,'0')
        self.calcArea.config(state='disabled')
    def numpocommand(self):
        self.calcArea.config(state='normal')
        text = self.calcArea.get(1.0,tk.END)
        if text != "\n":#return a backslach n string if there is nothing
            if text[-2] == '-' or text[-2] == 'x' or text[-2] == '/' or text[-2] == '+' or text[-2] == '.':
                pass
            else:
                self.calcArea.insert(tk.END,'.')
        self.calcArea.config(state='disabled')
    def numequcommand(self):
        math = self.calcArea.get(1.0,tk.END)
        total = self.calculateMath(math)
        self.answerArea.config(state ='normal')
        self.answerArea.delete(1.0,tk.END)
        self.answerArea.insert(1.0,str(total))
        self.answerArea.config(state='disabled')

    def plussigncommand(self):
        
        self.calcArea.config(state='normal')
        text = self.calcArea.get(1.0,tk.END)
        if text != "\n":#return a backslach n string if there is nothing
            if text[-2] == '-' or text[-2] == 'x' or text[-2] == '/' or text[-2] == '+':
                index = self.calcArea.index(tk.END)
                start = index+'-2c'
                end = index +'-1c'
                self.calcArea.replace(start,end,'+')
            else:
                self.calcArea.insert(tk.END,'+')
        self.calcArea.config(state='disabled')
    def minussigncommand(self):
        self.calcArea.config(state='normal')
        text = self.calcArea.get(1.0,tk.END)
        if text != "\n":#return a backslach n string if there is nothing
            if text[-2] == '-' or text[-2] == 'x' or text[-2] == '/' or text[-2] == '+':
                index = self.calcArea.index(tk.END)
                start = index+'-2c'
                end = index +'-1c'
                self.calcArea.replace(start,end,'-')
            else:
                self.calcArea.insert(tk.END,'-')
        self.calcArea.config(state='disabled')
                
    def dividesigncommand(self):
        self.calcArea.config(state='normal')
        text = self.calcArea.get(1.0,tk.END)
        if text != "\n":#return a backslach n string if there is nothing
            if text[-2] == '-' or text[-2] == 'x' or text[-2] == '/' or text[-2] == '+':
                index = self.calcArea.index(tk.END)
                start = index+'-2c'
                end = index +'-1c'
                self.calcArea.replace(start,end,'/')
            else:
                self.calcArea.insert(tk.END,'/')
        self.calcArea.config(state='disabled')
    def timessigncommand(self):
        self.calcArea.config(state='normal')
        text = self.calcArea.get(1.0,tk.END)
        if text != "\n":#return a backslach n string if there is nothing
            if text[-2] == '-' or text[-2] == 'x' or text[-2] == '/' or text[-2] == '+':
                index = self.calcArea.index(tk.END)
                start = index+'-2c'
                end = index +'-1c'
                self.calcArea.replace(start,end,'x')
            else:
                self.calcArea.insert(tk.END,'x')
        self.calcArea.config(state='disabled')
    def delsigncommand(self):
        self.calcArea.configure(state = 'normal')
        text = self.calcArea.get(1.0,tk.END)
        text = text[0:-2]
        self.calcArea.delete(1.0,tk.END)
        self.calcArea.insert(1.0,text)
        self.calcArea.configure(state='disabled')
    def acsigncommand(self):
        self.calcArea.config(state='normal')
        self.calcArea.delete(1.0,tk.END)
        self.calcArea.config(state='disabled')
        self.answerArea.config(state='normal')
        self.answerArea.delete(1.0,tk.END)
        self.answerArea.insert(1.0,"0")
        self.answerArea.config(state='disabled')
    def mplussigncommand(self):
        pass
    def mminussigncommand(self):
        pass
    def calculateMath(self,math):
        mathsearch = re.findall(r'[+\-x/]*[0-9]+\.*[0-9]*',math)
        
        total = 0
        if mathsearch:
            total = float(mathsearch[0])
            try:
                for x in mathsearch:
                    
                    
                    if x[0] == '+':
                        total = total + float(x[1:])
                    if x[0] == '-':
                        total = total - float(x[1:])
                    if x[0] == 'x':
                        total = total * float(x[1:])
                    if x[0] == '/':
                        total = total / float(x[1:])
            except:
                total ="Syntax Error"
           
        return total







if __name__ == "__main__":
    calc = Calc()
    calc.mainloop()