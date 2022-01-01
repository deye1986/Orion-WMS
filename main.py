import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title('Orion - v.0 development build')
root.iconbitmap('icon.ico')
root.minsize(height = 500, width = 600)
root.maxsize(height = 500, width = 600)

inventory = []

def document():
    with open('Orion_Inventory.txt', 'w') as file:
        pass #######

def search_for_item():
    global search_name_entry

    y = search_name_entry.get() + ','
    clear_text_from_search()
    if y in inventory:
        print(f'found {y} in inventory.')
        result = tk.Label(
            main_frame,
            text = f'found {y} in inventory.')
        result.pack()
        return
    else:
        print(f'item {y} not found')
        result_none = tk.Label(
            main_frame,
            text = f'Item: {y} not in inventory.')
        result_none.pack()
        

def display_inventory():
    inventory_on_screen = tk.Label(
    main_frame,
    text = inventory
    )
    inventory_on_screen.pack()

def clear_main_screen_frame():    
    inventory_on_screen.pack_forget()

def clear_text_from_entry():
    name_entry.delete(0, tk.END)

def clear_text_from_search():
    search_name_entry.delete(0, tk.END)

def add_item(enter_key=''):
    global name_entry
    z = name_entry.get()
    print(z)
    clear_text_from_entry()
    if z != '':
        inventory.append(z + ',')
        status_bar.pack_forget()
        status_item_saved.pack(side = 'right')
        return
    else:
        print('invalid input.')
        invalid_input = tk.Label(
            main_frame,
            text = 'Invalid input - Item must have a name.')
        invalid_input.pack()
  
def inventory_size():
    print(len(inventory))
    num_in_inv = len(inventory)
    n = tk.Label(
    main_frame,
    text = f'found {num_in_inv} items in inventory.'
    )
    n.pack()

control_frame = tk.Frame(bg = 'yellow')
control_frame.pack(side = 'top', fill = 'x')
main_frame = tk.Frame()
main_frame.pack(side = 'left', fill = 'y')
status_frame = tk.Frame()
status_frame.pack(side = 'bottom', fill = 'x')

title_label = tk.Label(
    control_frame,
    background = 'yellow',
    text = 'Inventory options:')
title_label.grid(row=1, column=1)

name_label = tk.Label(
    control_frame,
    background = 'yellow',
    text = 'Item name:')
name_label.grid(row=2, column=1)

name_entry = tk.Entry(control_frame)
name_entry.grid(row=2, column=2)

add_item_button = tk.Button(
    control_frame,
    padx = 1,
    pady = 1,
    text = 'Add Item',
    command = add_item)
root.bind('<Return>', add_item)
add_item_button.grid(row=2, column=3)

search_name_label = tk.Label(
    control_frame,
    text = 'Search item:',
    background = 'yellow',)
search_name_label.grid(row=3, column=1)

search_name_entry = tk.Entry(control_frame)
search_name_entry.grid(row=3, column=2)

search_item_button = tk.Button(
    control_frame,
    text = 'Search Inventory',
    command = search_for_item)
search_item_button.grid(row=3, column=3)

terminal_buttons = tk.Label(
    control_frame,
    text='Developer/debug options:',
    background = 'yellow')
terminal_buttons.grid(row=4, column=1)

status_button = tk.Button(
    control_frame,
    padx = 4,
    pady = -1,
    text = 'Number of items',
    command = inventory_size)
status_button.grid(row=5, column=1)

display_inventory_button = tk.Button(
    control_frame,
    text = 'Display inventory',
    command = display_inventory)
display_inventory_button.grid(row=5, column=2)

status_bar = tk.Label(
    status_frame,
    text = 'Status : System up')
status_bar.pack(side = 'right')

status_item_saved = tk.Label(
    status_frame,
    text = 'Item saved to inventory.'
)


root.mainloop()