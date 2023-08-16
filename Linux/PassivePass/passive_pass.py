#!/usr/bin/env python3
from tkinter import *
from tkinter.font import Font
import json
import os
from data.Inbuilt_al import inbuilt


class app():
    def __init__(self):
        pass

    def clear_label(self):
        self.submitted_label.config(text="")
        self.submitted_label

    def wifiname(self,event=None):
        
        self.wifiname123 = self.entry_begin.get().strip()
        if not self.wifiname123:
            self.submitted_label.config(text="WIFI-Name cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return
        

    def append_to_name_in_json_file(self, event=None):
        value = self.entry.get().strip()
        selected_option = self.clicked.get()

        if not value:
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Self Entry cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return

        data = {}
        self.filename = "./data/wifi/"+self.wifiname123+".json"
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        data.setdefault('Words', {})
        data['Words'].setdefault(selected_option, [])
        if value not in data['Words'][selected_option]:
            data['Words'][selected_option].append(value)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=6)
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Submitted: {value} for {selected_option}")
        else:
            self.submitted_label.config(text=f"Entry already exists for {selected_option}")

        self.root.after(3000, self.clear_label)

        self.drp.event_generate("<Down>")
    
    def append_to_router_in_json_file(self, event=None):
        value = self.entry.get().strip()
        selected_option = self.clicked_2.get()

        if not selected_option:
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Self Entry cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return

        data = {}
       
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        data.setdefault('Integers', {})
        data['Integers'].setdefault('router', [])
        if value not in data['Integers']['router']:
            data['Integers']['router'].append(value)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=6)
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Submitted: {value} for {selected_option}")
        else:
            self.submitted_label.config(text=f"Entry already exists for {selected_option}")
        self.root.after(3000, self.clear_label)

        self.drp.event_generate("<Down>")

    def append_to_phn_in_json_file(self, event=None):
        value = self.phn_num.get().strip()
        selected_option = self.clicked_2.get()

        if not value:
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Self Entry cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return

        data = {}
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        data.setdefault('Integers', {})
        data['Integers'].setdefault("phn", [])
        if value not in data['Integers']["phn"]:
            data['Integers']["phn"].append(value)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=6)
            self.phn_num.delete(0, END)
            self.submitted_label.config(text=f"Submitted: {value} for {selected_option}")
        else:
            self.submitted_label.config(text=f"Entry already exists for {selected_option}")
        self.root.after(1000, self.clear_label)

    
    def append_to_dob_in_json_file(self, event=None):
        value = self.entry_age_year.get().strip()
        selected_option = self.clicked_2.get()

        if not value:
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Self Entry cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return

        data = {}

        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        data.setdefault('Integers', {})
        data['Integers'].setdefault("dob", [])
        if value not in data['Integers']["dob"]:
            data['Integers']["dob"].append(value)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=6)
            self.entry_age_year.delete(0, END)
            self.submitted_label.config(text=f"Submitted: {value} for {selected_option}")
        else:
            self.submitted_label.config(text=f"Entry already exists for {selected_option}")

        self.root.after(1000, self.clear_label)

    def append_to_luck_in_json_file(self, event=None):
        value = self.Luck_num.get().strip()
        selected_option = self.clicked_2.get()

        if not value:
            self.entry.delete(0, END)
            self.submitted_label.config(text=f"Self Entry cannot be empty!!")
            self.root.after(1000, self.clear_label)
            return

        data = {}
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        data.setdefault('Integers', {})
        data['Integers'].setdefault("lucky_num", [])
        if value not in data['Integers']["lucky_num"]:
            data['Integers']["lucky_num"].append(value)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=6)
            self.Luck_num.delete(0, END)
            self.submitted_label.config(text=f"Submitted: {value} for {selected_option}")
        else:
            self.submitted_label.config(text=f"Entry already exists for {selected_option}")
        self.root.after(1000, self.clear_label)

    def clear_layout(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()


    def display_home_layout(self):
        self.root.geometry("1080x370")
        self.root.resizable(False, False)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=0)
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(3, weight=0)
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=0)
        self.root.rowconfigure(3, weight=0)
        self.root.rowconfigure(4, weight=0)
        self.root.rowconfigure(5, weight=0)
        self.root.rowconfigure(6, weight=0)
        self.root.rowconfigure(7, weight=0)
        self.root.rowconfigure(8, weight=0)


        

        self.my_font = Font(family="Courier")

        discript = Label(self.root, text="FILL SOME INFORMATION REGARDING TARGET", font=("courier", 16))
        discript.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        name = Label(self.root, text="Names", font=self.my_font)
        name.grid(row=2, column=0, padx=20, pady=20)

       
        self.clicked = StringVar()
        self.clicked.set("Target")
        
        
        self.drp = OptionMenu(self.root, self.clicked, "Father", "Mother", "Brother", "Childrens", "Wife", "Girlfriend","Others")
        self.drp.grid(row=2, column=1, padx=5, pady=5)

        
        
        self.entry = Entry(self.root, width=20, font=("courier", 12))
        self.entry.grid(row=2, column=2, padx=5, pady=5)
        self.entry.bind("<Return>", self.append_to_name_in_json_file)
        self.entry.focus()
        
        
        
        self.Age = Label(self.root, text="YearOfBirth", font=self.my_font)
        self.Age.grid(row=3, column=0, padx=5, pady=5)

        
        
        
        
        self.entry_age_year = Entry(self.root, width=20, font=("courier", 12))
        self.entry_age_year.grid(row=3, column=2, padx=10, pady=10)
        self.entry_age_year.bind("<Return>",self.append_to_dob_in_json_file)
        
        self.phn = Label(self.root, text="Mobile number(Optional):", font=self.my_font)
        self.phn.grid(row=4, column=0, padx=5, pady=5)

        
        
        
        
        self.phn_num = Entry(self.root, width=20, font=("courier", 12))
        self.phn_num.grid(row=4, column=2, padx=10, pady=10)
        self.phn_num.bind("<Return>",self.append_to_phn_in_json_file)

        

        self.Luck_num_la = Label(self.root, text="Lucky numbers-Oftelny used(Optional):", font=self.my_font)
        self.Luck_num_la.grid(row=5, column=0, padx=5, pady=5)
        
        self.Luck_num = Entry(self.root, width=20, font=("courier", 12))
        self.Luck_num.grid(row=5, column=2, padx=10, pady=10)
        self.Luck_num.bind("<Return>",self.append_to_luck_in_json_file)
        
        

        
        
        self.but_luck = Button(self.root, text="Submit", command=self.append_to_name_in_json_file)
        self.but_luck.grid(row=5, column=3, padx=5, pady=5)

        self.Router_Model_la = Label(self.root, text="Router model(Optional):", font=self.my_font)
        self.Router_Model_la.grid(row=6, column=0, padx=5, pady=5)
        self.clicked_2 = StringVar()
        self.clicked_2.set("Model")
        self.Router_Model = OptionMenu(self.root, self.clicked_2, "Digisol ","Tenda", "Netgear", "Tp-link", "D-link","Ubiquiti","Mercusys","iBall","Netis","Sanscord","Linkys","ASUS")
        self.Router_Model.grid(row=6, column=1, padx=10, pady=10)
        self.Router_Model.bind("<Return>")
        
        

        self.but_router = Button(self.root, text="Submit", command=self.append_to_router_in_json_file)
        self.but_router.grid(row=6, column=3, padx=5, pady=5)
        
        self.but_luck = Button(self.root, text="Submit", command=self.append_to_luck_in_json_file)
        self.but_luck.grid(row=5, column=3, padx=5, pady=5)

        self.but_dob = Button(self.root, text="Submit", command=self.append_to_dob_in_json_file)
        self.but_dob.grid(row=3, column=3, padx=5, pady=5)
        
        self.but = Button(self.root, text="Submit", command=self.append_to_name_in_json_file)
        self.but.grid(row=2, column=3, padx=5, pady=5)

        self.but_phn = Button(self.root, text="Submit", command=self.append_to_phn_in_json_file)
        self.but_phn.grid(row=4, column=3, padx=5, pady=5)

        self.but_done = Button(self.root, text="Done", width=15, height=1, command=self.create_generate_window)
        self.but_done.grid(row=8, column=3, padx=5, pady=5)

        
        self.submitted_label = Label(self.root, text="", font=("courier", 12))
        self.submitted_label.grid(row=8, column=0, columnspan=3, pady=5)







    def window(self):
        self.root = Tk()
        self.root.geometry("700x190")
        self.root.resizable(False, False)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        wifi_name = Label(self.root, text="WIFI-Name", font=("Arial", 16))
        wifi_name.grid(row=0, column=1, padx=5, pady=5)
        
        self.entry_begin = Entry(self.root, width=20, font=("courier", 12))
        self.entry_begin.grid(row=1, column=1, padx=5, pady=5)
      
        self.submitted_label = Label(self.root, text="", font=("courier", 12))
        self.submitted_label.grid(row=1, column=1, columnspan=3, pady=5)
        
        self.entry_begin.focus()
    
        self.button_display = Button(self.root, text="Proceed", font=("courier", 20), command=self.callboth)
        self.button_display.grid(row=2, column=1, padx=10, pady=10)
        
        self.root.bind("<Return>", lambda event: self.button_display.invoke())

        self.root.mainloop()
    def change(self):
        wifiname = self.entry_begin.get().strip()
        if not wifiname:
            self.submitted_label.config(text="WIFI-Name cannot be empty!!")
            self.root.after(3000, self.clear_label)
            return
        else:
            
            self.clear_layout()
            self.display_home_layout()
    def callboth(self):
        self.wifiname()
        self.change()
    
    def create_generate_window(self):
        generate_window = Toplevel(self.root)
        generate_window.title("Generate Window")
        generate_window.geometry("400x300")  
        generate_button = Button(generate_window, text="Generate", font=("courier", 20),command=lambda: inbuilt(self.filename,self.wifiname123))
        generate_button.place(relx=0.5, rely=0.5, anchor="center")
        self.root.withdraw() 

    
    

if __name__ == "__main__":
    my_app = app()
    my_app.window()



