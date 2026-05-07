import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json  
import os    

# Dictionary to store the count of each dice face
roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def record_roll(number):
    """Updates the dictionary and redraws the graph/label when a button is clicked."""
    roll_counts[number] += 1
    update_ui()

def clear_data():
    """Resets all roll counts to zero and updates the graph/label."""
    for key in roll_counts:
        roll_counts[key] = 0
    update_ui()

def save_data():
    """Saves the current data to a new JSON file without overwriting old ones."""
    try:
        # 1. Figure out the next available attempt number
        attempt_no = 1
        filename = f"dice_data(attempt{attempt_no}).json"
        
        # Keep increasing the number as long as the file already exists
        while os.path.exists(filename):
            attempt_no += 1
            filename = f"dice_data(attempt{attempt_no}).json"
            
        # 2. Save the file with the new, unique filename
        with open(filename, 'w') as file:
            json.dump(roll_counts, file, indent=4)
        
        # 3. Show a success message with the exact file name
        save_path = os.path.abspath(filename)
        messagebox.showinfo("Success", f"Data successfully saved as:\n{filename}\n\nLocation:\n{save_path}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")

def update_ui():
    """Clears the old graph, draws a new one, and updates the total counter."""
    ax.clear() 
    
    faces = list(roll_counts.keys())
    frequencies = list(roll_counts.values())
    
    ax.bar(faces, frequencies, color='#4da6ff', edgecolor='black')
    
    ax.set_xlabel('Dice Number', fontsize=12)
    ax.set_ylabel('Times Rolled', fontsize=12)
    ax.set_title('Live Dice Roll Tracker', fontsize=14, fontweight='bold')
    ax.set_xticks(faces) 
    
    ax.yaxis.get_major_locator().set_params(integer=True)
    canvas.draw()

    total = sum(roll_counts.values())
    total_label.config(text=f"Total Rolls: {total}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Dice Tracker")
root.geometry("600x700") 

# Create a frame to hold the 6 buttons in a row
button_frame = tk.Frame(root)
button_frame.pack(pady=20) 

# Create buttons 1 through 6
for i in range(1, 7):
    btn = tk.Button(
        button_frame, 
        text=str(i), 
        font=("Arial", 16, "bold"), 
        width=4, 
        height=2,
        bg="#e6e6e6",
        command=lambda n=i: record_roll(n)
    )
    btn.pack(side=tk.LEFT, padx=10)

# Total Rolls Label
total_label = tk.Label(
    root, 
    text="Total Rolls: 0", 
    font=("Arial", 14, "bold"),
    fg="#333333"
)
total_label.pack(pady=5)

# Save Button
save_btn = tk.Button(
    root,
    text="Save as JSON",
    font=("Arial", 12, "bold"),
    bg="#4CAF50", 
    fg="white",
    command=save_data
)
save_btn.pack(pady=5)

# Clear button
clear_btn = tk.Button(
    root,
    text="Clear Data",
    font=("Arial", 12, "bold"),
    bg="#ff4d4d", 
    fg="white",
    command=clear_data
)
clear_btn.pack(pady=5)

# --- Graph Setup ---
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10, fill=tk.BOTH, expand=True)

# Draw the initial empty graph
update_ui()

# Start the application
root.mainloop()