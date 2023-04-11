# importing the required modules  
from tkinter import *                   # importing all widgets and methods from tkinter  
from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
from datetime import date               # importing the date module from datetime  
  
# --------------------- Defining Functions ---------------------  

  
# function to reset all the entries  
def reset_entries():  
    # using the delete() method to delete the entries
    maximum_pressure_field.delete(0, END)  
    cylinder_bore_field.delete(0, END)  
    allowable_hoop_stress_label.delete(0, END)  
  
    # temporarily disabling the entries
    maximum_pressure_var.config(state = "disabled")  
    cylinder_bore_var.config(state = "disabled")  
    allowable_hoop_stress_var.config(state = "disabled")  
  
    # configuring the state of the different states to normal
    calculate_button.config(state = "normal")  

  
    # setting the values of the objects of the StringVar() class to current given values
    #change
    maximum_pressure_var.set(maximum_pressure_field)  
    cylinder_bore_var.set(cylinder_bore_field)  
    allowable_hoop_stress_var.set(allowable_hoop_stress_label)  
  
    # setting the value of the object of the StringVar() class to empty in result row  
    thickness_var.set("")  
  
  
# reset function  
def reset():  
    # calling the reset_entries() function  
    reset_entries()  
  
    # displaying a message box to display success message  
    mb.showinfo("Reset Entries", "All Entries are reset successfully!")  
  
# function to check errors in entering the data  
def check_for_errors():  
    # if any of the field is empty return a message box to display error  
    if (maximum_pressure_field.get() == "" or cylinder_bore_field.get() == "" or allowable_hoop_stress_label.get() == ""):  
        # displaying a message box to display error  
        mb.showerror("Input Error", "Invalid Format! Please Try Again.")  
          
        # calling the reset_entries() function  
        reset_entries()  
        return -1  
  
# function to calculate thickness  
def calculate_cylinder_thickness():  
    # calling the check_for_errors() function and storing the result in a variable  
    val = check_for_errors()  
      
    # checking if the value of the variable is equal to -1 or not   
    if val == -1:  
        # return if value is -1  
        return  
  
    else:  
        # retrieving the values stored in the objects of the StringVar() class in integer data types  
        maximum_pressure_value = int(maximum_pressure_var.get())  
        cylinder_bore_value = int(cylinder_bore_var.get())  
        allowable_hoop_stress_value = int(allowable_hoop_stress_var.get())  
        reboring_factor = 100 # change to conditional values
  
        # using the try-except method  
        try:  
            thickness = (maximum_pressure_value * cylinder_bore_value)/(2 * allowable_hoop_stress_value) + reboring_factor
            return thickness
  
        # raising an exception for ValueError  
        except ValueError:  
            # displaying the error if the entered date is out of range  
            mb.showerror("Out of Range", "Entered value.")  
            # calling the reset_entries() function to reset the data  
            reset_entries()  
  
# main function  
if __name__ == "__main__":  
  
    # creating an object of the Tk() class  
    gui_root = Tk()  
    # setting the title of the application  
    gui_root.title("Cylindrical Block Specification Calculator")  
    # setting the geometry of the application  
    gui_root.geometry("700x450+650+250")  
    # disabling the resizable option  
    gui_root.resizable(0, 0)  
    # configuring the background color of the application  
    gui_root.config(bg = "#FEECCF")  
    # setting the icon for the application  
  
    # creating frames to provide better structure for other widgets  
    header_frame = Frame(gui_root, bg = "#FEECCF")  
    entry_frame = Frame(gui_root, bg = "#FEECCF")  
    result_frame = Frame(gui_root, bg = "#FEECCF")  
  
    # using the pack() method to set the position of these frames on the window  
    header_frame.pack(pady = 10)  
    entry_frame.pack(pady = 10)  
    result_frame.pack(pady = 10)  
  
    # --------------------- Frame 1 ---------------------  
    # creating the label to display the heading of the application  
    header_label = Label(  
        header_frame,  
        text = "Cylindrical Block Specification Calculator",  
        font = ("verdana", "20", "bold"),  
        bg = "#FEECCF",  
        fg = "#C8871E"  
        )  
  
    # using the pack() method to set the position of the label on the window  
    header_label.pack(fill = "both", pady = 10)  
  
    # --------------------- Frame 2 ---------------------  
    # creating the labels to display information like maximum_pressure_label, cylinder_bore_label, allowable_hoop_stress_label
    maximum_pressure_label = Label(  
        entry_frame,  
        text = "maximum_pressure",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
  
    cylinder_bore_label = Label(  
        entry_frame,  
        text = "cylinder_bore",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
  
    allowable_hoop_stress_label = Label(  
        entry_frame,  
        text = "allowable_hoop_stress",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
      
      
    # using the grid() method to set the position of these labels in the grid format on the window  
    maximum_pressure_label.grid(row = 0, column = 1, padx = 10, pady = 10)  
    cylinder_bore_label.grid(row = 0, column = 2, padx = 10, pady = 10)  
    allowable_hoop_stress_label.grid(row = 0, column = 3, padx = 10, pady = 10)      
      
    
    # creating the objects of StringVar() class  
    maximum_pressure_var = StringVar(entry_frame)  
    cylinder_bore_var = StringVar(entry_frame)  
    allowable_hoop_stress_var = StringVar(entry_frame)  

  
    # setting the initial values for the object  
    maximum_pressure_var.set("")  
    cylinder_bore_var.set("")  
    allowable_hoop_stress_var.set("")  
  
    # creating some entry fields for the user to input data  
    maximum_pressure_field = Entry(  
        entry_frame,  
        width = 6,  
        font = ("verdana", "10"),   
        textvariable = maximum_pressure_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    cylinder_bore_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = cylinder_bore_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    allowable_hoop_stress_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = allowable_hoop_stress_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    # using the grid() method to set the positions of these entries fields in a grid manner on the window  
    maximum_pressure_field.grid(row = 1, column = 1, padx = 10, pady = 10)  
    cylinder_bore_field.grid(row = 1, column = 2, padx = 10, pady = 10)  
    allowable_hoop_stress_field.grid(row = 1, column = 3, padx = 10, pady = 10)  

  
    # --------------------- Frame 3 ---------------------  
    # creating an object of the IntVar() class  
    thickness_var = StringVar(result_frame)  
  
    # setting an initial value of the object  
    thickness_var.set("")  
  
    # creating the label to display result statements  
    footer_label = Label(  
        result_frame,   
        text = "The Calculated Thickness is:",   
        font = ("verdana", "10", "bold"),   
        bg = "#FEECCF",   
        fg = "#C8871E"  
        )  
  
    thickness_label = Label(  
        result_frame,   
        textvariable = thickness_var,   
        font = ("verdana", "10", "bold"),   
        bg = "#FEECCF",   
        fg = "#1FA73B"  
        )  
  
    # using the grid() method to set the position of these labels in the grid manner on the window  
    footer_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)  
    thickness_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)  
  
    # creating the buttons to reset the entries and yield the result  
    reset_button = Button(  
        result_frame,   
        text = "Reset Entries",   
        width = 12,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        command = reset,   
        bg = "#FF0000",   
        fg = "#FFFFFF"  
        )  
  
    calculate_button = Button(  
        result_frame,   
        text = "Calculate cylinder thickness",   
        width = 12,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        command = calculate_cylinder_thickness,   
        bg = "#00FF00",   
        fg = "#000000"  
        )  
  
    # using the grid() method to set the position of these buttons in the grid manner on the window  
    reset_button.grid(row = 1, column = 0, padx = 10, pady = 10)  
    calculate_button.grid(row = 1, column = 1, padx = 10, pady = 10)  
  
    # using the mainloop() method to run the application  
    gui_root.mainloop()