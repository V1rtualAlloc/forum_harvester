import tkinter as tk


class BaseView:
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        self.root = tk.Tk()
        self.running = False

    def run(self):
        self.running = True
        self.root.mainloop()

    def stop(self):
        self.running = False
        self.root.destroy()

    def is_running(self):
        return self.running
