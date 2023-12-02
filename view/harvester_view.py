import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from view.base_view import BaseView


class HarvesterView(BaseView):
    def __init__(self, controller, model):
        super().__init__(controller, model)

        # Create a notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Create tabs
        self.create_new_harvest_tab()
        self.resume_previous_harvest_tab()

        # Add components for DataAnalyzerView as needed
        self.analyze_button = tk.Button(self.root, text="Back", command=self.controller.switch_to_main_window)
        self.analyze_button.pack(pady=10)

        # Set the title for this specific view
        self.root.title("Harvester Data")

    def create_new_harvest_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Create New Harvest")

        # Widgets for "Create New Harvest" tab
        # Database related
        database_label = tk.Label(tab, text="New Database Name:")
        database_label.grid(row=0, column=0, padx=10, pady=10)

        self.database_name_entry = ttk.Entry(tab)
        self.database_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Parse related
        database_label = tk.Label(tab, text="Choose Template:")
        database_label.grid(row=1, column=0, padx=10, pady=10)

        self.directory_entry = ttk.Entry(tab)
        self.directory_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        browse_button = ttk.Button(tab, text="Browse", command=self.browse_file)
        browse_button.grid(row=1, column=2, padx=10, pady=10)
        
        # Progress bar
        self.progressbar = ttk.Progressbar(tab, orient="horizontal", length=300, mode="determinate")
        self.progressbar.grid(row=2, column=0, columnspan=3, pady=10)

        start_button = tk.Button(tab, text="Start", command=self.start_button_callback)
        start_button.grid(row=8, column=0, padx=5,pady=10)

        resume_button = tk.Button(tab, text="Resume", command=self.start_button_callback)
        resume_button.grid(row=8, column=1, padx=5, pady=10)

        pause_button = tk.Button(tab, text="Pause", command=self.start_button_callback)
        pause_button.grid(row=8, column=2, padx=5, pady=10)

    def resume_previous_harvest_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Resume Previous Harvest")

        # Widgets for "Resume Previous Harvest" tab
        harvest_dropdown_label = tk.Label(tab, text="Select Harvest:")
        harvest_dropdown_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a Combobox
        self.harvest_combobox = ttk.Combobox(tab, state="readonly")
        self.harvest_combobox.grid(row=0, column=1, padx=10, pady=10)
        
        # Populate the Combobox with options (replace with your actual data)
        options = ["theapricity.com", "reddit.com", "saidit.com"]
        self.harvest_combobox["values"] = options
        
        # Set an initial value (optional)
        self.harvest_combobox.set(options[0])

        # Progress bar
        self.progressbar = ttk.Progressbar(tab, orient="horizontal", length=300, mode="determinate")
        self.progressbar.grid(row=1, column=0, columnspan=3, pady=10)

        resume_button = tk.Button(tab, text="Resume", command=self.resume_button_callback)
        resume_button.grid(row=5, column=0, padx=5, pady=10)

        pause_button = tk.Button(tab, text="Pause", command=self.start_button_callback)
        pause_button.grid(row=5, column=1, padx=5, pady=10)
    
    def browse_file(self):
        # Open a file dialog to select a file
        selected_file = filedialog.askopenfilename()

        # Update the entry widget with the selected file path
        if selected_file:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, selected_file)

            # self.controller.model


    def start_button_callback(self):
        # Implement the functionality for the "Start" button
        pass

    def resume_button_callback(self):
        # Implement the functionality for the "Resume" button
        pass