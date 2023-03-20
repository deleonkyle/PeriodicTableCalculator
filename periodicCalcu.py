import tkinter as tk

# Dictionary of element data
elements = {
   "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": 1.008, "group": 1, "period": 1},
    "He": {"name": "Helium", "atomic_number": 2, "atomic_mass": 4.003, "group": 18, "period": 1},
    "Li": {"name": "Lithium", "atomic_number": 3, "atomic_mass": 6.941, "group": 1, "period": 2},
    "Be": {"name": "Beryllium", "atomic_number": 4, "atomic_mass": 9.012, "group": 2, "period": 2},
    "B": {"name": "Boron", "atomic_number": 5, "atomic_mass": 10.81, "group": 13, "period": 2},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_mass": 12.01, "group": 14, "period": 2},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": 14.01, "group": 15, "period": 2},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": 16.00, "group": 16, "period": 2},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_mass": 19.00, "group": 17, "period": 2},
    "Ne": {"name": "Neon", "atomic_number": 10, "atomic_mass": 20.18, "group": 18, "period": 2},
    "Na": {"name": "Sodium", "atomic_number": 11, "atomic_mass": 22.99, "group": 1, "period": 3},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "atomic_mass": 24.31, "group": 2, "period": 3},
    "Al": {"name": "Aluminum", "atomic_number": 13, "atomic_mass": 26.98, "group": 13, "period": 3},
    "Si": {"name": "Silicon", "atomic_number": 14, "atomic_mass": 28.09, "group": 14, "period": 3},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": 30.97, "group": 15, "period": 3},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_mass": 32.06, "group": 16, "period": 3},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": 35.45, "group": 17, "period": 3},
    "Ar": {"name": "Argon", "atomic_number": 18, "atomic_mass": 39.95, "group": 18, "period": 3},
    
    # Add more elements here
}

# Function to calculate atomic mass
def calculate_atomic_mass(symbol, num_atoms):
    element = elements.get(symbol)
    if element:
        atomic_mass = element["atomic_mass"] * num_atoms
        return atomic_mass
    else:
        return None

# Function to handle button click events
def calculate_button_click():
    symbol = element_symbol_entry.get()
    num_atoms = int(num_atoms_entry.get())
    atomic_mass = calculate_atomic_mass(symbol, num_atoms)
    if atomic_mass:
        result_label.config(text="The atomic mass of {} is {:.2f} g/mol".format(symbol, atomic_mass))
    else:
        result_label.config(text="Invalid element symbol")

def change_color():
    if calculate_button()["bg"] == "gray":
        calculate_button["bg"] = "blue"
    else:
        calculate_button()["bg"] = "gray"

# Create GUI
root = tk.Tk()
root.title("Periodic Table Calculator")
root.geometry("450x150")
root.config(bg="white")
root.iconbitmap("periodic-table.png")
root.resizable(False, False)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2

# Set the position of the window
root.geometry("+%d+%d" % (x, y))

element_symbol_label = tk.Label(root, text="Element Symbol:", font=("Gadugi", 16), bg="white")
element_symbol_label.grid(row=0, column=0)

element_symbol_entry = tk.Entry(root, font=("Gadugi", 16))
element_symbol_entry.grid(row=0, column=1)

num_atoms_label = tk.Label(root, text="Number of Atoms:", font=("Gadugi", 16), bg="white")
num_atoms_label.grid(row=1, column=0)

num_atoms_entry = tk.Entry(root, font=("Gadugi", 16))
num_atoms_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", bg="white", fg="black", command=calculate_button_click, font=("Gadugi", 14),)
calculate_button.grid(row=2, column=0)

result_label = tk.Label(root, text="", font=("Gadugi", 12), bg="white")
result_label.grid(row=2, column=1)


root.mainloop()