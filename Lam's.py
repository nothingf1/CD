import math
import tkinter as tk

class Lamport:
    def __init__(self):
        # Arrays for events and timestamps
        self.e = [[0 for _ in range(10)] for _ in range(10)]
        self.en = [[0 for _ in range(10)] for _ in range(10)]
        self.ev = [0] * 10
        # Number of processes
        self.p = 0
        # HashMap for relationships
        self.hm = {}

    def calc(self):
        # Get input for number of processes and events
        self.p = int(input("Enter the number of processes: "))
        for i in range(1, self.p + 1):
            self.ev[i] = int(input(f"Enter the no of events per process {i}: "))
        # Get input for relationships
        for i in range(1, self.p + 1):
            print(f"For process: {i}")
            for j in range(1, self.ev[i] + 1):
                input_val = int(input(f"For event: {j} "))
                k = i * 10 + j
                self.hm[k] = input_val
                if j == 1:
                    self.en[i][j] = 1
        # Calculate timestamps
        for i in range(1, self.p + 1):
            for j in range(2, self.ev[i] + 1):
                k = i * 10 + j
                if self.hm.get(k) == 0:
                    self.en[i][j] = self.en[i][j - 1] + 1
                else:
                    a = self.hm.get(k)
                    p1 = a // 10
                    e1 = a % 10
                    self.en[i][j] = max(self.en[p1][e1], self.en[i][j - 1]) + 1
        # Print timestamps
        for i in range(1, self.p + 1):
            for j in range(1, self.ev[i] + 1):
                print(self.en[i][j])
        # Create the GUI
        self.draw_gui()

    def draw_gui(self):
        root = tk.Tk()
        root.title("Lamport Clock")
        canvas = tk.Canvas(root, width=500, height=500)
        canvas.pack()

        # Draw lines for processes
        for i in range(1, self.p + 1):
            canvas.create_line(50, 100 * i, 450, 100 * i, fill="black")
    
        # Draw events and arrows
        for i in range(1, self.p + 1):
            for j in range(1, self.ev[i] + 1):
                k = i * 10 + j
                x = 50 * j
                y = 100 * i - 3
                canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="blue")
                canvas.create_text(x, y - 5, text=f"e{i}{j}({self.en[i][j]})")
                h1 = self.hm.get(k)
                if h1 != 0:
                    h11 = h1 // 10
                    h12 = h1 % 10
                    canvas.create_line(50 * h12 + 2, 100 * h11, 50 * j + 2, 100 * i, arrow=tk.LAST, fill="red")
        root.mainloop()

if __name__ == "__main__":
    lamport = Lamport()
    lamport.calc()
