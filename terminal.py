import tkinter as tk
from tkinter import scrolledtext
import subprocess
from NLP_to_command import nlp_command
def process_command():
    command = input_field.get()
    input_field.delete(0, tk.END)

    # Display the command in the terminal
    terminal_area.insert(tk.END, f"> {command}\n")
    
    if command.lower() == "exit":
        root.destroy()
        return
    
    try:
        # Use subprocess to execute the command
        bash = nlp_command(command)
        print(bash)
        result = subprocess.run(bash, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr
    except Exception as e:
        output = f"Error: {e}"

    # Display the output or error in the terminal
    terminal_area.insert(tk.END, f"{output}\n")

    # Auto-scroll to the bottom of the terminal
    terminal_area.see(tk.END)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Terminal Emulator with Subprocess")
root.geometry("700x500")

# Create a scrolled text widget to display terminal output
terminal_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=25, width=80)
terminal_area.pack(pady=10)
terminal_area.insert(tk.END, "Welcome to the Terminal Emulator!\nType 'exit' to quit.\n")

# Create an entry widget for user input
input_field = tk.Entry(root, width=80)
input_field.pack(pady=5)
input_field.bind("<Return>", lambda event: process_command())  # Bind the Return key to process_command

# Add a button to process commands
submit_button = tk.Button(root, text="Enter", command=process_command)
submit_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
