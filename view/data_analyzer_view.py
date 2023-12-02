import tkinter as tk
from view.base_view import BaseView


class DataAnalyzerView(BaseView):
    def __init__(self, controller, model):
        super().__init__(controller, model)

        # Add components for DataAnalyzerView as needed
        self.analyze_button = tk.Button(self.root, text="Back", command=self.controller.switch_to_main_window)
        self.analyze_button.pack(pady=10)

        # Set the title for this specific view
        self.root.title("Analyze Data")
