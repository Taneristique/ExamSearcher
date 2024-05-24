import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import gui.core_mechanism.index as dh
class Form:  # Class names should start with uppercase letters
    def __init__(self):
        self.root = tk.Tk()  # Store the root window in self.root
        self.root.title("Exam Searcher By Taneristique v1.0")
        self.lesson_codes=[]
        # File Uploader Section
        self.file_path_label = tk.Label(self.root, text="No file selected yet.")
        self.file_path_label.pack(pady=10)

        self.select_file_button = tk.Button(self.root, text="Select PDF File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        # Global variable (not recommended) - Consider storing within the class
        self.selected_file_path = None  # Initialize to None

        # Checkbox with Lesson Options (All initially selected)
        self.lesson_var = tk.StringVar(value="CUMARTESİ 1.OTURUM")  # Set default selection
        self.lesson_options = ["CUMARTESİ 1.OTURUM", "CUMARTESİ 2.OTURUM", "PAZAR 1.OTURUM", "PAZAR 2.OTURUM", "Bilmiyorum"]

        lesson_frame = tk.Frame(self.root)
        lesson_frame.pack(pady=10)

        for option in self.lesson_options:
            lesson_checkbox = tk.Checkbutton(lesson_frame, text=option, variable=self.lesson_var, onvalue=option)
            lesson_checkbox.pack(anchor=tk.W)
            lesson_checkbox.select()  # Select all checkboxes by default
        # Text Input Field
    
        text_input_label = tk.Label(self.root, text="Enter Lesson Code E.G(MUH302): ")
        text_input_label.pack(pady=5)

        self.text_input = tk.Text(self.root, height=5)
        self.text_input.pack(pady=5)

        # Add Lesson Code Button
        self.add_lesson_button = tk.Button(self.root, text="Add Lesson Code", command=self.add_lesson_code)
        self.add_lesson_button.pack(pady=5)
        # Submit Button
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form)
        submit_button.pack(pady=10)

        # Initialize the dictionary within the function (avoid global)
        self.inputs = self.get_initial_data()  # Function to get initial data

        # Print the initial text content (optional)
        print(self.inputs["text"])
        self.root.mainloop()  # Start the event loop

    def select_file(self):
        """Opens a file selection dialog and returns the chosen file path."""
        filepath = filedialog.askopenfilename()
        if filepath:
            self.file_path_label.config(text=f"Selected File: {filepath}")
            self.selected_file_path = filepath  # Store the selected file path

    def add_lesson_code(self):
        """Gets the text from the text box and adds it to the lesson codes list.

        Optionally updates the text input display to show the added code.
        """

        lesson_code = self.text_input.get("1.0", tk.END).strip()

        # Validation 
        if not lesson_code:
            messagebox.showerror("Error", "Please enter a lesson code.")
            return

        self.lesson_codes.append(lesson_code)  # Add code to the lesson codes list
        self.text_input.delete("1.0", tk.END)  # Clear the text box

    def get_initial_data(self):
        """Returns a dictionary with initial data."""
        return {
            "lesson": self.lesson_var.get(),
            "text": self.lesson_codes,
            "file": self.selected_file_path if self.selected_file_path else None
        }

    def submit_form(self):
        self.inputs.update({
            "lesson": self.lesson_var.get(),
            "text": self.lesson_codes,
            "file": self.selected_file_path if self.selected_file_path else None
        })

        # Validate input (optional)
        if self.lesson_var.get() == "Bilmiyorum":
             self.show_popup(self.checkExamInfo())
        else:
            self.checkExamInfo(self.inputs["lesson"])


    def checkExamInfo(self,title=""):
        if(title==""):
            self.show_popup(dh.pdf_data_handler(self.lesson_codes, str(self.inputs["file"])))
        else:
            self.show_popup(dh.pdf_data_handler(self.lesson_codes, str(self.inputs["file"])),title)

    def show_popup(self, message, title="Lesson Codes"):
        """Displays a popup window with the given message, handling newlines."""
        messagebox.showinfo(title, message) 


