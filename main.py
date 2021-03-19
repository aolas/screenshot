import pyautogui
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
count = 1

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    global count
    myScreenshot.save(r'C:\Users\ramun\OneDrive\Pictures\Testai1\screenshot{n}.png'.format(n = count))
    count +=1


myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green', fg='white', font=10)
canvas1.create_window(150, 150, window=myButton)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()

