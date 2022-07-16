from tkinter import *
def findGst():
    org_cost = int(org_priceField.get())
    N_price = int(net_priceField.get())
    gst_rate = ((N_price - org_cost) * 100) / org_cost;
    gst_rateField.insert(10, str(gst_rate) + " % ")

def clearAll():
    org_priceField.delete(0, END)
    net_priceField.delete(0, END)
    gst_rateField.delete(0, END)

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("GST Rate Finder")
    gui.geometry("300x300")
    org_price = Label(gui, text="Original Price",
                      bg="blue")
    net_price = Label(gui, text="Net Price",
                      bg="blue")
    find = Button(gui, text="Find", fg="Black",
                  bg="Red",
                  command=findGst)
    gst_rate = Label(gui, text="Gst Rate", bg="blue")
    clear = Button(gui, text="Clear", fg="Black",
                   bg="Red",
                   command=clearAll)
    org_price.grid(row=1, column=1, padx=10, pady=10)

    net_price.grid(row=2, column=1, padx=10, pady=10)

    find.grid(row=3, column=2, padx=10, pady=10)

    gst_rate.grid(row=4, column=1, padx=10, pady=10)

    clear.grid(row=5, column=2, padx=10, pady=10)

    org_priceField = Entry(gui)

    net_priceField = Entry(gui)

    gst_rateField = Entry(gui)

    org_priceField.grid(row=1, column=2, padx=10, pady=10)

    net_priceField.grid(row=2, column=2, padx=10, pady=10)

    gst_rateField.grid(row=4, column=2, padx=10, pady=10)

    gui.mainloop()



    