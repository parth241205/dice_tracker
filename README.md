Dice Roll Tracker
A lightweight Python desktop application that tracks dice rolls and visualizes the results in real-time using a bar chart. Built with Tkinter for the GUI and Matplotlib for data visualization. This tool is useful for tabletop games, probability experiments, or just tracking quick statistics.

Features
Interactive GUI: Simple button interface to log rolls for dice faces 1 through 6.

Real-Time Visualization: A dynamically updating Matplotlib bar chart showing the frequency of each number.

Roll Counter: Keeps a running total of how many times the dice has been rolled in the current session.

Clear Data: A quick reset button to clear the chart and start a new session without restarting the app.

Export to JSON: Save your current session data to a local JSON file. Automatically increments file names (e.g., dice_data(attempt1).json, dice_data(attempt2).json) so you never accidentally overwrite your history.

Prerequisites
Python 3.x

Matplotlib

Installation & Usage
Clone or download this repository to your local machine.

Open your terminal or command prompt and install the required library:
pip install matplotlib
Navigate to the folder containing the script and run the application:

To run the file open your terminal and write the command:
   python dice_tracker.py
(Note: Use python3 instead of python depending on your system configuration).

Technologies Used
Python (Core logic)

Tkinter (Graphical User Interface)

Matplotlib (Data visualization and graphing)

JSON (Data exporting)
