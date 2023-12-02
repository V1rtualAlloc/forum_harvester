import tkinter as tk
from view.base_view import BaseView


class MainView(BaseView):
    def __init__(self, controller, model):
        super().__init__(controller, model)

        self.harvest_button = tk.Button(self.root, text="Harvest", command=self.controller.switch_to_harvester_window)
        self.harvest_button.pack(pady=10)

        self.analyze_button = tk.Button(self.root, text="Analyze", command=self.controller.switch_to_data_analyzer_window)
        self.analyze_button.pack(pady=10)

        # Set the title for this specific view
        self.root.title("Main Window")

        # Set the dimensions of the window
        self.root.geometry("300x100")

