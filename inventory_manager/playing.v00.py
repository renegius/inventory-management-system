from tkinter import ttk
from tkinter import messagebox
import tkinter
import pymysql
from datetime import datetime
#
#############################################################
#
#Main window:
window=tkinter.Tk()
window.title("Stock Management System")

#5 empty strings
placeholder_array=['','','','','']

#Connection to the database
def connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='London@2025',
        db='stockmanagementsystem'
    )
    return conn 

#Calling the function and make a cursor for deal with the mysql
conn=connection()
cursor=conn.cursor()

for i in range(0,5):
    placeholder_array[i]=tkinter.StringVar()

#Functions
def read():
    cursor.connection.ping()
    sql=f"SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks ORDER BY item_id ASC"
    cursor.execute(sql)
    results=cursor.fetchall()
    #conn.commit()
    conn.close()
    return results

def refeshTable(data=None):
    # Clear the table
    for data_row in my_tree.get_children():
        my_tree.delete(data_row)
    
    # If data is provided, use it; otherwise, fetch all data from the database
    if data is None:
        data = read()
    
    # Insert the data into the table
    for array in data:
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    
    my_tree.tag_configure('orow', background="#EEEEEE")
    my_tree.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

def setph(word,num):
    for ph in range (0,5):
        if ph == num:
            placeholder_array[ph].set(word)

def save():
    item_id_input=str(item_id_entry.get())
    item_name_input=str(item_name_entry.get())
    item_price_input=str(item_price_entry.get())
    item_qnty_input=str(item_qnty_entry.get())
    item_category_input=str(item_category_combo.get())
    valid=True
    if not(item_id_input and item_id_input.strip()) or not(item_name_input and item_name_input.strip()) or not(item_price_input and item_price_input.strip()) or not(item_qnty_input and item_qnty_input.strip()) or not(item_category_input and item_category_input.strip()):
        messagebox.showwarning("","Please fill up entries")
        return
    try:
        cursor.connection.ping()
        sql=f"SELECT * FROM stocks WHERE item_id = '{item_id_input}'"
        cursor.execute(sql)
        check_item_id=cursor.fetchall()
        if len(check_item_id) > 0:
            messagebox.showwarning("","Item ID already used")
            return
        else:
            cursor.connection.ping()
            sql=f"INSERT INTO stocks (item_id, item_name, item_price, item_qnty, item_category) VALUES ('{item_id_input}','{item_name_input}','{item_price_input}','{item_qnty_input}','{item_category_input}')"
            cursor.execute(sql)
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("","Error while saving")
        return
    refeshTable()

def update():
    selected_item_id=''
    try:
        selected_item=my_tree.selection()[0]
        selected_item_id=str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showwarning("","Please select a data row")
    print(selected_item_id)
    item_id_input=str(item_id_entry.get())
    item_name_input=str(item_name_entry.get())
    item_price_input=str(item_price_entry.get())
    item_qnty_input=str(item_qnty_entry.get())
    item_category_input=str(item_category_combo.get())
    if not(item_id_input and item_id_input.strip()) or not(item_name_input and item_name_input.strip()) or not(item_price_input and item_price_input.strip()) or not(item_qnty_input and item_qnty_input.strip()) or not(item_category_input and item_category_input.strip()):
        messagebox.showwarning("","Please fill up entries")
        return
    if(selected_item_id!=item_id_input):
        messagebox.showwarning("","You can't change Item ID")
        return
    try:
        cursor.connection.ping()
        sql=f"UPDATE stocks SET item_name = '{item_name_input}', item_price = '{item_price_input}', item_qnty = '{item_qnty_input}', item_category = '{item_category_input}' WHERE item_id = '{item_id_input}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        #
        my_tree.item(selected_item, values=(item_id_input, item_name_input, item_price_input, item_qnty_input, item_category_input, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    except Exception as err:
        messagebox.showwarning("","Error occured ref: "+str(err))
        return
    
    messagebox.showinfo("", "Item has been successfully updated")

def delete():
    try:
        if(my_tree.selection()[0]):
            decision = messagebox.askquestion("","Delete the seletec data?")
            if(decision!='yes'):
                return
            else:
                selected_item=my_tree.selection()[0]
                item_id=str(my_tree.item(selected_item)['values'][0])
                try:
                    cursor.connection.ping()
                    sql=f"DELETE FROM stocks WHERE item_id = '{item_id}'"
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("","Data has been successfully deleted")
                except:
                    messagebox.showinfo("","Sorry, an error occured")
                refeshTable()
    except:
        messagebox.showwarning("","Please select a data row")

def select():
    try:
        selected_item=my_tree.selection()[0]
        item_id=str(my_tree.item(selected_item)['values'][0])
        item_name=str(my_tree.item(selected_item)['values'][1])
        item_price=str(my_tree.item(selected_item)['values'][2])
        item_qnty=str(my_tree.item(selected_item)['values'][3])
        item_category=str(my_tree.item(selected_item)['values'][4])
        setph(item_id,0)
        setph(item_name,1)
        setph(item_price,2)
        setph(item_qnty,3)
        setph(item_category,4)
    except:
        messagebox.showwarning("","Please select data row ")

def find():
    item_id_input = item_id_entry.get().strip()
    item_name_input = item_name_entry.get().strip()
    item_price_input = item_price_entry.get().strip()
    item_qnty_input = item_qnty_entry.get().strip()
    item_category_input = item_category_combo.get().strip()

    cursor.connection.ping()

    if item_id_input:
        sql = "SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks WHERE item_id = %s"
        params = (item_id_input,)
    elif item_name_input:
        sql = "SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks WHERE item_name LIKE %s"
        params = (f"%{item_name_input}%",)
    elif item_price_input:
        sql = "SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks WHERE item_price LIKE %s"
        params = (f"%{item_price_input}%",)
    elif item_qnty_input:
        sql = "SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks WHERE item_qnty LIKE %s"
        params = (f"%{item_qnty_input}%",)
    elif item_category_input:
        sql = "SELECT item_id, item_name, item_price, item_qnty, item_category, item_date FROM stocks WHERE item_category LIKE %s"
        params = (f"%{item_category_input}%",)
    else:
        messagebox.showwarning("", "Please fill up one of the entries")
        return

    try:
        cursor.execute(sql, params)
        result = cursor.fetchall()

        if result:
            # Update the table with the search results
            refeshTable(result)
        else:
            messagebox.showwarning("", "No data found")
    except pymysql.Error as err:
        messagebox.showwarning("", f"Error: {err}")
    finally:
        conn.close()

def clear():
    for num in range (0,5):
            setph('',(num))
    refeshTable()
    
#############################################################
#
# Frame for Buttons and Form Entries
frame = tkinter.Frame(window)
frame.grid(row=1, column=0, sticky="nsew")

# Configure the rows for the frame to ensure the buttons and entries expand
frame.grid_rowconfigure(0, weight=3)  # First row for the buttons
frame.grid_rowconfigure(1, weight=3)  # Second row for the form entries
frame.grid_columnconfigure(0, weight=3)  # Left column for buttons
frame.grid_columnconfigure(1, weight=3)  # Right column for form entries

# Manage Frame for Buttons PARA ALL 
manage_frame = tkinter.Frame(frame)
manage_frame.grid(row=0, column=0)

# BUTTONS Inside the manage_frame
save_btn = tkinter.Button(manage_frame, text="SAVE", width=10, borderwidth=5, bg="#808080", fg='black', command=save, font=('Arial', 12))
update_btn = tkinter.Button(manage_frame, text="UPDATE", width=10, borderwidth=5, bg="#808080", fg='black', command=update, font=('Arial', 12))
delete_btn = tkinter.Button(manage_frame, text="DELETE", width=10, borderwidth=5, bg="#808080", fg='black', command=delete, font=('Arial', 12))
select_btn = tkinter.Button(manage_frame, text="SELECT", width=10, borderwidth=5, bg="#808080", fg='black', command=select, font=('Arial', 12))
find_btn = tkinter.Button(manage_frame, text="FIND", width=10, borderwidth=5, bg="#808080", fg='black', command=find, font=('Arial', 12))
clear_btn = tkinter.Button(manage_frame, text="CLEAR", width=10, borderwidth=5, bg="#808080", fg='black', command=clear, font=('Arial', 12))

save_btn.grid(row=0, column=0, sticky="nsew")
update_btn.grid(row=0, column=1, sticky="nsew")
delete_btn.grid(row=0, column=2, sticky="nsew")
select_btn.grid(row=0, column=3, sticky="nsew")
find_btn.grid(row=0, column=4, sticky="nsew")
clear_btn.grid(row=0, column=5, sticky="nsew")
#
#
#
#
# Entries Frame for Form Inputs
entries_frame = tkinter.Frame(frame)
entries_frame.grid(row=1, column=0)
#
#
# LABELS of Entries inside manage_frame 
item_id_label = tkinter.Label(entries_frame, text="ITEM ID", anchor="center", width=10, font=('Arial', 12))
item_name_label = tkinter.Label(entries_frame, text="NAME", anchor="center", width=10, font=('Arial', 12))
item_price_label = tkinter.Label(entries_frame, text="PRICE", anchor="center", width=10, font=('Arial', 12))
item_qnty_label = tkinter.Label(entries_frame, text="QUANTITY", anchor="center", width=10, font=('Arial', 12))
item_category_label = tkinter.Label(entries_frame, text="CATEGORY", anchor="center", width=10, font=('Arial', 12))

item_id_label.grid(row=0, column=2, padx=10, pady=10)
item_name_label.grid(row=1, column=2, padx=10, pady=10)
item_price_label.grid(row=2, column=2, padx=10, pady=10)
item_qnty_label.grid(row=3, column=2, padx=10, pady=10)
item_category_label.grid(row=4, column=2, padx=10, pady=10)
#
#Entries FIELDS
#
#Categories for the array

category_array = ['Laptop', 'Tablet', 'Smartwatch', 'Headphones', 'Gaming Console', 'Monitor', 'Printer', 'Storage', 'Accessories', 'Smartphone']

item_id_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[0])
item_name_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[1])
item_price_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[2])
item_qnty_entry = tkinter.Entry(entries_frame, width=50, font=('Arial', 12), textvariable=placeholder_array[3])
item_category_combo = ttk.Combobox(entries_frame, width=48, font=('Arial', 12), textvariable=placeholder_array[4], values=category_array)

item_id_entry.grid(row=0, column=3, padx=10, pady=5)
item_name_entry.grid(row=1, column=3, padx=10, pady=5)
item_price_entry.grid(row=2, column=3, padx=10, pady=5)
item_qnty_entry.grid(row=3, column=3, padx=10, pady=5)
item_category_combo.grid(row=4, column=3, padx=10, pady=5)
#
#
#
#
#MY TREE TABLES
## Frame for MY_TREE and Form Entries
frame_tree = tkinter.Frame(window)
frame_tree.grid(row=0, column=0, sticky="nsew")

frame_tree.grid_rowconfigure(0, weight=1)
frame_tree.grid_columnconfigure(0, weight=1)

my_tree=ttk.Treeview(frame_tree,show='headings')
style=ttk.Style()

style.configure("Treeview", rowheight=30, font=('Arial', 11))

my_tree['columns']=('Item Id','Name','Price','Quantity','Category','Date',)

my_tree.column('#0',width=0,stretch=tkinter.NO)
my_tree.column('Item Id',anchor=tkinter.CENTER,width=50)
my_tree.column('Name',anchor=tkinter.W,width=150)
my_tree.column('Price',anchor=tkinter.CENTER,width=100)
my_tree.column('Quantity',anchor=tkinter.CENTER,width=100)
my_tree.column('Category',anchor=tkinter.W,width=100)
my_tree.column('Date',anchor=tkinter.CENTER,width=100)

my_tree.heading("Item Id",text="ITEM ID",anchor=tkinter.CENTER)
my_tree.heading("Name",text="NAME",anchor=tkinter.CENTER)
my_tree.heading("Price",text="PRICE",anchor=tkinter.CENTER)
my_tree.heading("Quantity",text="QUANTITY",anchor=tkinter.CENTER)
my_tree.heading("Category",text="CATEGORY",anchor=tkinter.CENTER)
my_tree.heading("Date",text="DATE",anchor=tkinter.CENTER)

my_tree.tag_configure('orow',background="#EEEEEE")
#position of my tree
#my_tree.grid(in_=frame_tree, row=0, column=0, sticky="nsew", padx=10, pady=10)

refeshTable()

window.resizable(True,True)
window.mainloop()