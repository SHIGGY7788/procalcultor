import customtkinter as ctk

# Establishes the main window
main = ctk.CTk()
main.geometry("400x500")
ctk.set_appearance_mode("dark")
main.title("Calculator Pro")

# Main program font
mFont = ctk.CTkFont(family="Impact", size=30)


def cbutton(parent, text, x, y):
    button = ctk.CTkButton(parent,
                           width=70,
                           height=70,
                           text=text,
                           font=mFont,
                           fg_color="black",
                           hover_color="gray",
                           command=lambda: number_entry(text))
    button.place(relx=x, rely=y)



def calc_page():
    cFont = ctk.CTkFont(family="Aharoni", size=20)
    mFrame.pack_forget()
    mText.place_forget()
    mEnter.place_forget()

    cFrame = ctk.CTkFrame(main,
                          width=400,
                          height=500)
    cFrame.pack()

    global numline
    numline = ctk.CTkEntry(cFrame,
                           width=150,
                           height=60,
                           placeholder_text="0",
                           font=cFont)
    numline.place(relx=0.05, rely=0.05)

    dline = ctk.CTkLabel(cFrame,
                         width=400,
                         height=12,
                         fg_color="white",
                         text='')
    dline.place(relx=0, rely=0.2)

    num0 = ctk.CTkButton(cFrame,
                         width=70,
                         height=223,
                         text="0",
                         font=mFont,
                         fg_color="black",
                         hover_color="gray",
                         command=lambda: number_entry(0))
    num0.place(relx=0.7, rely=0.25)

    button_positions = [
        (0.1, 0.25), (0.3, 0.25), (0.5, 0.25),
        (0.1, 0.4), (0.3, 0.4), (0.5, 0.4),
        (0.1, 0.55), (0.3, 0.55), (0.5, 0.55)
    ]

    for i, (x, y) in enumerate(button_positions, start=1):
        cbutton(cFrame, str(i), x, y)



# function to input num buttons into number line
def number_entry(text):
    numline.insert(ctk.END, text)


# Establishes the first frame the user will see
def m_page():
    global mFrame
    mFrame = ctk.CTkFrame(main,
                          width=400,
                          height=500)
    mFrame.pack()
    global mText
    mText = ctk.CTkLabel(mFrame,
                         text="Welcome",
                         font=mFont)
    mText.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

    global mEnter
    mEnter = ctk.CTkButton(mFrame,
                           text="Enter",
                           font=mFont,
                           fg_color="black",
                           hover_color="gray",
                           command=calc_page)
    mEnter.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


# Displays the main page
m_page()

# Loops the main window
main.mainloop()
