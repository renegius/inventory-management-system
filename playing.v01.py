#############################################################
#
#                      2025 - 05 
#           **** COMPUTER SYSTEM ASSIGNMENT ****
#                    Anthony Cepeda
#
#############################################################
#
from tkinter import ttk
from tkinter import messagebox
import tkinter
import pymysql
#from datetime import datetime
#Main window:
window=tkinter.Tk()
window.title("Inventory Management System")

#Array for the input of the .Entry
placeholder_array=['','','','','']

################################
#       ***FUNCTIONS***        #
################################

#Connection to the database
def connection():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'London@2025',
        db = 'stockmanagementsystem'
    )
    return conn 

#Calling the function and make a cursor for deal with the mysql
conn=connection()
cursor=conn.cursor()

#Print in the .Entry the strings in the case of get them from set_placehoder_array
for n in range(1,5):
   placeholder_array[n]=tkinter.StringVar()

#Execute querie in DB to get rows of information
def read_items_db():
    cursor.connection.ping()
    sql=f"SELECT * FROM stocks ORDER BY item_id ASC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.close()
    return results

#Get the selected item of the screen
def get_selected_item():
    return my_tree.selection()[0]

def clear_table_outputs():
    for data_row in my_tree.get_children():
        my_tree.delete(data_row)

#if data is NULL then take all the data from read_items_db, if data has some input, then use it for the array
def refresh_table_mytree(data = None):

    clear_table_outputs()

    # If data is null fetch all data from the database
    if data is None:
        data = read_items_db()
    
    # Insert the data into the table / in the case the data is not None, then show only the data input
    for array in data:
        my_tree.insert(parent = '', index = 'end', iid = array, text = "", values = (array))
    
    my_tree.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

#Introduce to the placeholder array the entries from select and from clear (NULL)
def set_placeholder_array(word,num):
    for placeholder in range (1,5):
        if placeholder == num:
            placeholder_array[placeholder].set(word)

#Get data input for each item attribute
def get_item_data_input():
       return (
           #str(item_id_entry.get()),
           str(item_name_entry.get()),
           str(item_price_entry.get()),
           str(item_qnty_entry.get()),
           str(item_category_combo.get())
       ) 

#Return true or false, True if any field is empty
def is_input_fields_invalid(item_name_input, item_price_input, item_qnty_input, item_category_input):
    return (
        #not(item_id_input and item_id_input.strip()) or 
        not(item_name_input and item_name_input.strip()) or 
        not(item_price_input and item_price_input.strip()) or 
        not(item_qnty_input and item_qnty_input.strip()) or 
        not(item_category_input and item_category_input.strip())
    )

def save_item_db():

    item_name_input, item_price_input, item_qnty_input, item_category_input = get_item_data_input()

    if is_input_fields_invalid(item_name_input, item_price_input, item_qnty_input, item_category_input):
        messagebox.showwarning("","Please fill up entries")
        return
    
    try:

        cursor.connection.ping()
        sql=f"INSERT INTO stocks (item_name, item_price, item_qnty, item_category) VALUES ('{item_name_input}','{item_price_input}','{item_qnty_input}','{item_category_input}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("","Error while saving")
        return
    
    clear_button()

def update_item_db():
    try:
        #Select item row and item ID for set the update
        selected_item = get_selected_item()
        item_id = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showwarning("","Please select a data row")
    
    item_name_input, item_price_input, item_qnty_input, item_category_input = get_item_data_input()

    if is_input_fields_invalid( item_name_input, item_price_input, item_qnty_input, item_category_input):
        messagebox.showwarning("","Please fill up entries")
        return
    
    try:
        cursor.connection.ping()
        sql=f"UPDATE stocks SET item_name = '{item_name_input}', item_price = '{item_price_input}', item_qnty = '{item_qnty_input}', item_category = '{item_category_input}' WHERE item_id = '{item_id}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()

    except Exception as err:
        messagebox.showwarning("","Error occured ref: "+str(err))
        return
    
    messagebox.showinfo("", "Item has been successfully updated")

    clear_button()

def delete_item_db():
    try:
        selected_item = get_selected_item()

        if selected_item:
            decision = messagebox.askquestion("","Delete the selected data?")

            if decision != 'yes':
                return
            
            else:
                item_id = str(my_tree.item(selected_item)['values'][0])

                try:
                    cursor.connection.ping()
                    sql = f"DELETE FROM stocks WHERE item_id = '{item_id}'"
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("","Data has been successfully deleted")

                except:
                    messagebox.showinfo("","Sorry, an error occured")

                
                refresh_table_mytree()
        else:
            messagebox.showwarning("","Please select a data row")
    except:
        messagebox.showwarning("","Sorry there was a problem with the DB, try again later")

    clear_button()

def select_item_db():
   
    selected_item = get_selected_item()
    
    if not selected_item:
        messagebox.showwarning("","Please select data row ")
        return
    
    item_id = str(my_tree.item(selected_item)['values'][0])
    item_name = str(my_tree.item(selected_item)['values'][1])
    item_price = str(my_tree.item(selected_item)['values'][2])
    item_qnty = str(my_tree.item(selected_item)['values'][3])
    item_category = str(my_tree.item(selected_item)['values'][4])

    set_placeholder_array(item_id,0)
    set_placeholder_array(item_name,1)
    set_placeholder_array(item_price,2)
    set_placeholder_array(item_qnty,3)
    set_placeholder_array(item_category,4)

def find_item_db():

    item_name_input = item_name_entry.get().strip()
    item_price_input = item_price_entry.get().strip()
    item_qnty_input = item_qnty_entry.get().strip()
    item_category_input = item_category_combo.get().strip()

    cursor.connection.ping()

    if item_name_input:
        sql = "SELECT * FROM stocks WHERE item_name LIKE %s"
        params = (f"%{item_name_input}%",)
    elif item_price_input:
        sql = "SELECT * FROM stocks WHERE item_price LIKE %s"
        params = (f"%{item_price_input}%",)
    elif item_qnty_input:
        sql = "SELECT * FROM stocks WHERE item_qnty LIKE %s"
        params = (f"%{item_qnty_input}%",)
    elif item_category_input:
        sql = "SELECT * FROM stocks WHERE item_category LIKE %s"
        params = (f"%{item_category_input}%",)
    else:
        messagebox.showwarning("", "Please fill up one of the entries")
        return

    try:
        cursor.execute(sql, params)
        result = cursor.fetchall()

        if result:
            # Update the table with the search results
            refresh_table_mytree(result)
        else:
            messagebox.showwarning("", "No data found")

    except pymysql.Error as err:
        messagebox.showwarning("", f"Error: {err}")

    finally:
        conn.close()

def clear_button():
    for num in range (1,5):
        set_placeholder_array('',(num))

    refresh_table_mytree()
    
################################
##   ***WINDOW DESGIN***      ##
################################

# Frame for Buttons and Form Entries
frame = tkinter.Frame(window)
frame.grid(row=1, column=0, sticky="nsew")

# Configure the rows for the frame to ensure the buttons and entries expand
frame.grid_rowconfigure(0, weight=3)
frame.grid_rowconfigure(1, weight=3)
frame.grid_columnconfigure(0, weight=3)
frame.grid_columnconfigure(1, weight=3)

# Manage Frame for Buttons
manage_frame = tkinter.Frame(frame)
manage_frame.grid(row=0, column=0)

# BUTTONS Inside the manage_frame
save_btn = tkinter.Button(manage_frame, text="SAVE", width=10, borderwidth=5, bg="#808080", fg='black', command=save_item_db, font=('Arial', 12))
update_btn = tkinter.Button(manage_frame, text="UPDATE", width=10, borderwidth=5, bg="#808080", fg='black', command=update_item_db, font=('Arial', 12))
delete_btn = tkinter.Button(manage_frame, text="DELETE", width=10, borderwidth=5, bg="#808080", fg='black', command=delete_item_db, font=('Arial', 12))
select_btn = tkinter.Button(manage_frame, text="SELECT", width=10, borderwidth=5, bg="#808080", fg='black', command=select_item_db, font=('Arial', 12))
find_btn = tkinter.Button(manage_frame, text="FIND", width=10, borderwidth=5, bg="#808080", fg='black', command=find_item_db, font=('Arial', 12))
clear_btn = tkinter.Button(manage_frame, text="CLEAR", width=10, borderwidth=5, bg="#808080", fg='black', command=clear_button, font=('Arial', 12))

save_btn.grid(row=0, column=0, sticky="nsew")
update_btn.grid(row=0, column=1, sticky="nsew")
delete_btn.grid(row=0, column=2, sticky="nsew")
select_btn.grid(row=0, column=3, sticky="nsew")
find_btn.grid(row=0, column=4, sticky="nsew")
clear_btn.grid(row=0, column=5, sticky="nsew")

# Entries Frame for Form Inputs
entries_frame = tkinter.Frame(frame)
entries_frame.grid(row=1, column=0)

# Entries Labels 
item_name_label = tkinter.Label(entries_frame, text="NAME", anchor="center", width=10, font=('Arial', 12))
item_price_label = tkinter.Label(entries_frame, text="PRICE", anchor="center", width=10, font=('Arial', 12))
item_qnty_label = tkinter.Label(entries_frame, text="QUANTITY", anchor="center", width=10, font=('Arial', 12))
item_category_label = tkinter.Label(entries_frame, text="CATEGORY", anchor="center", width=10, font=('Arial', 12))

item_name_label.grid(row=1, column=2, padx=10, pady=10)
item_price_label.grid(row=2, column=2, padx=10, pady=10)
item_qnty_label.grid(row=3, column=2, padx=10, pady=10)
item_category_label.grid(row=4, column=2, padx=10, pady=10)

#Entries Fields
item_name_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[1])
item_price_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[2])
item_qnty_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[3])
item_category_combo = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[4])

item_name_entry.grid(row=1, column=3, padx=10, pady=5)
item_price_entry.grid(row=2, column=3, padx=10, pady=5)
item_qnty_entry.grid(row=3, column=3, padx=10, pady=5)
item_category_combo.grid(row=4, column=3, padx=10, pady=5)


#MY TREE TABLE
frame_tree = tkinter.Frame(window)
frame_tree.grid(row=0, column=0, sticky="nsew")

frame_tree.grid_rowconfigure(0, weight=1)
frame_tree.grid_columnconfigure(0, weight=1)

my_tree=ttk.Treeview(frame_tree,show='headings')
style=ttk.Style()

style.configure("Treeview", rowheight=30, font=('Arial', 11))

my_tree['columns']=('Item Id','Name','Price','Quantity','Category','Date',)

my_tree.heading("Item Id",text="ITEM ID",anchor=tkinter.CENTER)
my_tree.heading("Name",text="NAME",anchor=tkinter.CENTER)
my_tree.heading("Price",text="PRICE",anchor=tkinter.CENTER)
my_tree.heading("Quantity",text="QUANTITY",anchor=tkinter.CENTER)
my_tree.heading("Category",text="CATEGORY",anchor=tkinter.CENTER)
my_tree.heading("Date",text="DATE",anchor=tkinter.CENTER)

my_tree.column('#0',width=0,stretch=tkinter.NO)
my_tree.column('Item Id',anchor=tkinter.CENTER,width=50)
my_tree.column('Name',anchor=tkinter.W,width=150)
my_tree.column('Price',anchor=tkinter.CENTER,width=100)
my_tree.column('Quantity',anchor=tkinter.CENTER,width=100)
my_tree.column('Category',anchor=tkinter.W,width=100)
my_tree.column('Date',anchor=tkinter.CENTER,width=100)

refresh_table_mytree()

window.resizable(True,True)
window.mainloop()