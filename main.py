def open_loginWindow():
    import sqlite3

    import tkinter as tk
    from pathlib import Path
    from tkinter import PhotoImage, messagebox, StringVar

    # Initialize main window
    window = tk.Tk()
    window.geometry("1200x675")
    window.configure(bg="#445C9A")
    window.title("Login")

    # Canvas setup
    canvas = tk.Canvas(window, bg="#445C9A", height=675, width=1200, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    # Create canvas and add image to it
    logo_image = PhotoImage(file="assets/frame0/image_1.png")  # Update with your image path
    label = tk.Label(window,height=675, width=600, image=logo_image, bg="#455D9A")  # Set the background color
    label.place(x=0, y=0)

    # Create a dark rectangle for half of the window
    canvas.create_rectangle(600, 0, 1200, 675, fill="#343346", outline="")

    # Add Text Labels
    canvas.create_text(656, 21, anchor="nw", text="Log-in", fill="#FFFFFF", font=("Arial", 48, "bold"))
    canvas.create_text(656, 335, anchor="nw", text="Password", fill="#FFFFFF", font=("Arial", 24))
    canvas.create_text(656, 198, anchor="nw", text="Username", fill="#FFFFFF", font=("Arial", 24))

    # Username Entry
    username_entry_bg = canvas.create_rectangle(662.5, 250, 1135, 300, fill="#D9D9D9", outline="")
    username_entry = tk.Entry(window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 16))
    username_entry.place(x=662.5, y=251, width=470, height=48)

    # Password Entry
    password_entry_bg = canvas.create_rectangle(662.5, 384, 1135, 434, fill="#D9D9D9", outline="")
    password_entry = tk.Entry(window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 16), show="*")
    password_entry.place(x=662.5, y=385, width=470, height=48)

    # Button to simulate login
    def buttonClick():
        print("Login button clicked")
        username = username_entry.get()
        password = password_entry.get()

        # Connect to the SQLite database
        connection = sqlite3.connect('credentials.db')
        cursor = connection.cursor()
        
        # Check if username and password are in the database
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        
        if result:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            window.destroy()
            open_adminDashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        
        # Close the database connection
        connection.close()

    login_button = tk.Button(window, text="Login", bg="#5A6BAA", fg="white", font=("Arial", 16, "bold"), borderwidth=0,
                            highlightthickness=0, command=lambda: buttonClick())
    login_button.place(x=725, y=505, width=190, height=57)

    #Button for students.
    login_button = tk.Button(window, text="I'm a Student", bg="#5A6BAA", fg="white", font=("Arial", 16, "bold"), borderwidth=0,
                            highlightthickness=0, command=lambda: (window.destroy(), open_mainWindow()))
    login_button.place(x=920, y=505, width=190, height=57)

    # Window settings
    window.resizable(False, False)
    window.mainloop()

def open_mainWindow():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
    from tkinter import ttk
    import re

    # Function to get the path for assets
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Set up the main Tkinter window
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame2"

    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Create a dropdown (Combobox) for course prefixes
    prefixes = ["ACC", "AFA", "ANT", "ARB", "ART", "BIO", "BLD", "BMK", "BMT", "BPM", "CHM", "CJT", "COM", "COR", "CSM", "CUL", "CAN", "ECN", "EGL", "EGR", "EMT", "ENT", "ESL", "FOS", 
                "FRN", "GEO", "HIM", "HLE", "HNV", "HRT", "HSM", "HST", "HUM", "HUS", "INT", "MAS", "MAT", "MUS", "NTR", "NUM", "NUR", "PAR", "PAS", "PED", "PHL", "PHY", "PMD", "POS", 
                "PRJ", "PSC", "PSY", "RAD", "RST", "SGT", "SOC", "SPN", "TED", "THE", "TRF", "WMS"]

    # Create a canvas
    canvas = Canvas(
        window,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Add texts to the canvas
    canvas.create_text(52.0, 46.0, anchor="nw", text="Welcome to Credit Hour Calculator", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(233.0, 224.0, anchor="nw", text="Prefix", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(487.0, 224.0, anchor="nw", text="Course Number", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(810.0, 224.0, anchor="nw", text="Section Number", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(52.0, 102.0, anchor="nw", text="Input your course details in order to automatically calculate the correct number of credit hours\nbased on Prince George’s Community College and federal guidelines.", fill="#FFFFFF", font=("Jost Regular", 15 * -1))
    canvas.create_text(52.0, 151.0, anchor="nw", text="Note: Ensure that you input accurate Course Information to receive the most precise credit hour calculation. If you have any questions or need assistance, refer to the Help section.", fill="#FFFFFF", font=("Jost Bold", 12 * -1))

    # Load and place images and buttons
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(1150.0, 50.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, bg="#343346", highlightthickness=0, command=lambda: (window.destroy(), open_recordsWindow()), relief="flat")
    button_1.place(x=1025.0, y=25.0, width=50.0, height=50.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, bg="#343346", highlightthickness=0, command=lambda: (window.destroy(), open_helpWindow()), relief="flat")
    button_2.place(x=1075.0, y=25.0, width=50.0, height=50.0)

    # Create the Combobox for prefixes
    prefix_combobox = ttk.Combobox(window, values=prefixes, state="readonly")
    prefix_combobox.place(x=150.0, y=265.0, width=250.0, height=48.0)

    # Create input fields for course details
    def create_entry(x, y, width, height):
        entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))  # Modify if different images are needed
        canvas.create_image(x + width / 2, y + height / 2, image=entry_image)
        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=x, y=y, width=width, height=height)
        return entry

    entry_1 = create_entry(475.0, 265.0, 250.0, 48.0)
    entry_2 = create_entry(800.0, 265.0, 250.0, 48.0)

    # Additional input fields
    canvas.create_text(224.0, 382.0, anchor="nw", text="Weeks", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(487.0, 382.0, anchor="nw", text="In-Class Hours", fill="#FFFFFF", font=("Jost Bold", 30 * -1))
    canvas.create_text(795.0, 382.0, anchor="nw", text="Out-of-Class Hours", fill="#FFFFFF", font=("Jost Bold", 30 * -1))

    entry_3 = create_entry(475.0, 423.0, 250.0, 48.0)
    entry_4 = create_entry(150.0, 423.0, 250.0, 48.0)
    entry_5 = create_entry(800.0, 423.0, 250.0, 48.0)

    def calculate():
        prefix = prefix_combobox.get()
        course_number = entry_1.get()
        section_number = entry_2.get()

        if re.match(r'^\d{4}[A-Z]?$', course_number):
            if re.match(r'^[A-Z]{2}\d{2}$', section_number):
                weeks = entry_4.get()
                in_class_hours = entry_3.get()
                out_of_class_hours = entry_5.get()
                credit_hours = round(((int(in_class_hours)+int(out_of_class_hours)) * int(weeks)) / 60, 0)
                class_name = prefix + "-" + str(course_number) + "-" + str(section_number)
                print(class_name)
                print(credit_hours)
                window.destroy()
                open_resultsWindow(class_name, in_class_hours, out_of_class_hours, credit_hours)
            else:
                 messagebox.showerror("Invalid input", "Please enter the section number in the format 'XX00' where X is a capital letter and 0 is a digit.")
        else:
            messagebox.showerror("Invalid input", "Please enter a valid number with a 4 digits and optionally a capital letter at the end.")

    # Submit button
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: calculate(), relief="flat")
    button_3.place(x=475.0, y=540.0, width=250.0, height=50.0)

    # Rectangle for layout
    canvas.create_rectangle(51.0, 88.23243336740023, 568.9194711351643, 94.69264080282942, fill="#FFFFFF", outline="")
    window.resizable(False, False)
    window.mainloop()

def open_resultsWindow(class_name, in_class_hours, out_of_class_hours, credit_hours):
    from pathlib import Path
    from tkinter import Tk, Text, Button, Label, PhotoImage

    import sqlite3
    from datetime import datetime

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame7"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Set up the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Title label
    title_label = Label(
        window,
        text="Here Are Your Results...",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Regular", 30)
    )
    title_label.place(x=52, y=37)

    # Text box for results
    result_text = Text(
        window,
        bg="#313241",
        fg="#FFFFFF",
        wrap="word",
        font=("Arial", 16)
    )
    result_text.tag_configure("class_name", font=("Arial", 24, "bold"))
    result_text.insert("1.0", str(class_name) + "\n\n\n")
    result_text.tag_add("class_name", "1.0", "1.end")
    result_text.insert("2.0", "In a class that contains " + str(in_class_hours) + " in class hours and " + str(out_of_class_hours) + " out of class hours, " + str(class_name) + " is a class that should have " + str(credit_hours) + " credit hours.")
    result_text.configure(state="disabled")  # Set to read-only
    result_text.place(x=52, y=99, width=1078, height=292)

    # Informational message
    info_message = Label(
        window,
        text=("Thank You for Using Credit Hour Calculator for Prince George’s Community College!\n\n"
            "Congratulations on successfully calculating your course credit hours! We hope this tool has made your planning "
            "easier and helped clarify your\nacademic workload. Based on the details you provided, the calculated credit hours "
            "for your course are displayed below. You can save this result for\nfuture reference or make adjustments as needed."),
        bg="#343346",
        fg="#9AE197",
        justify="left",
        font=("Jost Regular", 13)
    )
    info_message.place(x=52, y=423)

    # Function for button click (placeholder)
    def on_button_click(button_id):
        print(f"button_{button_id} clicked")

    def storeData():
        conn = sqlite3.connect('records.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            date TEXT,
            time TEXT,
            class_name TEXT,
            in_class_hours REAL,
            out_of_class_hours REAL,
            credit_hours REAL,
            UNIQUE(class_name, in_class_hours, out_of_class_hours, credit_hours)
        )
        ''')
        conn.commit()
            

        # Get the current date and time
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')

        try:
            # Insert the new record only if the combination doesn't exist
            cursor.execute('''
                INSERT OR IGNORE INTO records (date, time, class_name, in_class_hours, out_of_class_hours, credit_hours)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (current_date, current_time, class_name, in_class_hours, out_of_class_hours, credit_hours))
        
            if cursor.rowcount == 0:
                print("Record already exists.")
            else:
                print("Record inserted successfully.")
                
            # Commit the changes
            conn.commit()

        except sqlite3.Error as e:
            print("An error occurred:", e)

    # Action buttons
    button_1_img = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_1_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_feedbackWindow()),
        relief="flat"
    )
    button_1.place(x=920, y=574, width=186, height=35)

    button_2_img = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_2_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_button_click(2),
        relief="flat"
    )
    button_2.place(x=652, y=574, width=193, height=35)

    button_3_img = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window,
        image=button_3_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: storeData(),
        relief="flat"
    )
    button_3.place(x=377, y=574, width=186, height=35)

    button_4_img = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        window,
        image=button_4_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat"
    )
    button_4.place(x=102, y=574, width=186, height=35)

    # Top-right buttons (icons)
    button_5_img = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        window,
        image=button_5_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat",
        bg="#343346"
    )
    button_5.place(x=1125, y=25, width=55, height=55)

    button_6_img = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        window,
        image=button_6_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat",
        bg="#343346"
    )
    button_6.place(x=1075, y=27, width=50, height=50)

    button_7_img = PhotoImage(file=relative_to_assets("button_7.png"))
    button_7 = Button(
        window,
        image=button_7_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat",
        bg="#343346"
    )
    button_7.place(x=1025, y=27, width=50, height=50)

    window.resizable(False, False)
    window.mainloop()

def open_feedbackWindow():

    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
    import sqlite3
    from datetime import datetime
    import re

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame1"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    feedback_window = Tk()

    feedback_window.geometry("1200x675")
    feedback_window.configure(bg = "#343346")

    canvas = Canvas(
        feedback_window,
        bg = "#343346",
        height = 675,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        600.0,
        675.0,
        fill="#445C9A",
        outline="")

    canvas.create_text(
        160.0,
        25.0,
        anchor="nw",
        text="Application Feedback ",
        fill="#FFFFFF",
        font=("Jost Bold", 30 * -1)
    )

    canvas.create_rectangle(
        104.0,
        72.15368943446472,
        494.502933775831,
        77.84632732626692,
        fill="#FFFFFF",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        300.0,
        165.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=35.0,
        y=155.0,
        width=530.0,
        height=18.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        300.0,
        232.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=35.0,
        y=222.0,
        width=530.0,
        height=18.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        300.0,
        301.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=35.0,
        y=291.0,
        width=530.0,
        height=18.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        300.0,
        369.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=35.0,
        y=359.0,
        width=530.0,
        height=18.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        300.0,
        437.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=35.0,
        y=427.0,
        width=530.0,
        height=18.0
    )

    canvas.create_text(
        35.0,
        130.0,
        anchor="nw",
        text="Name: ",
        fill="#FFFFFF",
        font=("Jost Bold", 14 * -1)
    )

    canvas.create_text(
        35.0,
        197.0,
        anchor="nw",
        text="Email:",
        fill="#FFFFFF",
        font=("Jost Bold", 14 * -1)
    )

    canvas.create_text(
        35.0,
        266.0,
        anchor="nw",
        text="What improvements would you suggest? : ",
        fill="#FFFFFF",
        font=("Jost Bold", 14 * -1)
    )

    canvas.create_text(
        35.0,
        334.0,
        anchor="nw",
        text="What do you like most about the app? : ",
        fill="#FFFFFF",
        font=("Jost Bold", 14 * -1)
    )

    canvas.create_text(
        35.0,
        402.0,
        anchor="nw",
        text="Any other comments or suggestions? : ",
        fill="#FFFFFF",
        font=("Jost Bold", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (feedback_window.destroy(), open_loginWindow()),
        relief="flat",
        bg="#455D9A"
    )
    button_1.place(
        x=75.0,
        y=560.0,
        width=200.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (storeData()),
        relief="flat",
        bg="#455D9A"
    )
    button_2.place(
        x=325.0,
        y=560.0,
        width=200.0,
        height=35.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        900.0,
        496.0,
        image=image_image_1
    )

    canvas.create_text(
        675.0,
        295.0,
        anchor="nw",
        text="Help us improve! Your feedback is valuable to us. Please take a minute\nto share your experience.",
        fill="#FFFFFF",
        font=("Jost Regular", 15 * -1)
    )

    canvas.create_text(
        675.0,
        177.0,
        anchor="nw",
        text="If you found this tool helpful, consider leaving us feedback by\ncompleting the survey to let us know what you liked or suggest\nimprovements. Your insights directly contribute to enhancing this tool\nfor all Prince George’s Community College students.",
        fill="#FFFFFF",
        font=("Jost Regular", 15 * -1)
    )

    canvas.create_text(
        675.0,
        140.0,
        anchor="nw",
        text="Stay Involved",
        fill="#FFFFFF",
        font=("Jost Bold", 15 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        181.0,
        528.0000130192075,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        421.0,
        526.9999930859649,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1150.0,
        50.0,
        image=image_image_4
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (feedback_window.destroy(), open_helpWindow()),
        relief="flat",
        bg="#343346"
    )
    button_3.place(
        x=1075.0,
        y=25.0,
        width=50.0,
        height=50.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (feedback_window.destroy(), open_recordsWindow()),
        relief="flat",
        bg="#343346"
    )
    button_4.place(
        x=1025.0,
        y=25.0,
        width=50.0,
        height=50.0
    )

    def storeData():
        if re.match(r"^[^@]+@[^@]+\.[^@]+$", str(entry_2.get())):
            name = entry_1.get()
            email = entry_2.get()
            suggested_improvements = entry_3.get()
            like_most = entry_4.get()
            other = entry_5.get()
            if name and email and suggested_improvements and like_most and other:
                connection = sqlite3.connect('records.db')
                cursor = connection.cursor()

                # Set the current date as the submission_date
                submission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # SQL query to insert data into the feedback table
                insert_query = """
                INSERT INTO feedback (name, email, suggested_improvements, like_most, other, submission_date)
                VALUES (?, ?, ?, ?, ?, ?)
                """
                
                # Execute the query with the provided data
                cursor.execute(insert_query, (name, email, suggested_improvements, like_most, other, submission_date))
                
                # Commit the transaction
                connection.commit()
                messagebox.showinfo("Success!","Feedback inserted successfully!")
                feedback_window.destroy()
                open_loginWindow()
            else:
                messagebox.showerror("Invalid input", "Please fill all fields before submitting.")
        else:
            print(entry_2.get())
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")

    feedback_window.resizable(False, False)
    feedback_window.mainloop()

def open_FAQWindow():
    from pathlib import Path
    from tkinter import Tk, Label, Button, PhotoImage

    # Define paths to the output and assets directories
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame3"

    # Helper function to get the path of assets
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Initialize the Tkinter window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Load images for buttons
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))

    # Create and place the buttons
    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, bg="#343346", command=lambda: (window.destroy(), open_helpWindow()), relief="flat")
    button_1.place(x=1075, y=25, width=50, height=50)

    button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, bg="#343346", command=lambda: (window.destroy(), open_recordsWindow()), relief="flat")
    button_2.place(x=1025, y=25, width=50, height=50)

    button_3 = Button(window, image=button_image_3, borderwidth=0, highlightthickness=0, bg="#343346", command=lambda: (window.destroy(), open_mainWindow()), relief="flat")
    button_3.place(x=1125, y=25, width=50, height=50)

    # Load and display the main image
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_label_1 = Label(window, image=image_image_1, bg="#343346")
    image_label_1.place(x=25, y=475)

    # Frequently Asked Questions
    Label(window, text="Frequently Asked Questions", font=("Jost Bold", 22), bg="#343346", fg="#9AB3F0").place(x=36, y=54)
    Label(window, text="Here are some frequently asked questions to help you get started with the Credit Hour Calculator!", font=("Jost Medium", 19), bg="#343346", fg="#FFFFFF", wraplength=600).place(x=37, y=93)

    # Questions
    Label(window, text="Q: How Do I Calculate My Credit Hours?", font=("Jost Bold", 18), bg="#343346", fg="#E61B1F").place(x=107, y=168)
    Label(window, text="Q: Can I Go Back & Edit My Entries?", font=("Jost SemiBold", 18), bg="#343346", fg="#E61B1F").place(x=107, y=254)
    Label(window, text="Q: How Do I Save & View My Results?", font=("Jost SemiBold", 18), bg="#343346", fg="#E61B1F").place(x=107, y=325)
    Label(window, text="Q: Is My Data Secure?", font=("Jost Bold", 18), bg="#343346", fg="#E61B1F").place(x=307, y=429)
    Label(window, text="Q: Who Can I Contact If I Encounter an Issue?", font=("Jost Bold", 18), bg="#343346", fg="#E61B1F").place(x=307, y=490)

    # Answers
    Label(window, text="A: Simply enter your course details on the Calculation Page by using the drop-down menu for each section, and then the app will automatically total your credit hours based on your input.", font=("Jost Light", 16), bg="#343346", fg="#FFFFFF", wraplength=1000, justify="left").place(x=156, y=203)
    Label(window, text="A: Yes, if you feel the need to edit your entries, you can go back to the Calculation Page or select “Recalculate” on the Results Page.", font=("Jost Light", 16), bg="#343346", fg="#FFFFFF", wraplength=1000, justify="left").place(x=156, y=278)
    Label(window, text="A: When results are generated on the Results Page, you have the option to save your results by selecting the “Save” Button. You can view your saved results when selecting your Profile Icon on the top right of the screen.", font=("Jost Light", 16), bg="#343346", fg="#FFFFFF", wraplength=1000, justify="left").place(x=156, y=351)
    Label(window, text="A: Yes, the app complies with data privacy standards to keep your information safe", font=("Jost Light", 16), bg="#343346", fg="#FFFFFF", wraplength=1000, justify="left").place(x=357, y=455)
    Label(window, text="A: If you need further assistance, please contact our support team!", font=("Jost Light", 16), bg="#343346", fg="#FFFFFF", wraplength=700, justify="left").place(x=357, y=516)

    # Prevent window resizing
    window.resizable(False, False)
    window.mainloop()

def open_contactWindow():
    from pathlib import Path
    from tkinter import Tk, Button, Label, PhotoImage, Frame

    # Define the paths for output and assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame5"

    # Function to make asset paths relative to the project
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Create the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Add a frame for the left-side rectangle area
    left_frame = Frame(window, bg="#445C9A", width=600, height=675)
    left_frame.place(x=0, y=0)

    # Create canvas and add image to it
    logo_image = PhotoImage(file="assets/frame5/image_1.png")  # Update with your image path
    label = Label(window,height=350, width=350, image=logo_image, bg="#455D9A")  # Set the background color
    label.place(x=125, y=162.5)

    # Add the title label
    title_label = Label(
        left_frame,
        text="Get In Contact With Us!",
        bg="#445C9A",
        fg="#FFFFFF",
        font=("Jost ExtraBold", 35)
    )
    title_label.place(x=52.5, y=80)

    # Add content labels
    info_label = Label(
        window,
        text="If you still have questions or need further assistance, please feel free to contact our support team.",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost SemiBold", 19),
        wraplength=500,
        justify="left"
    )
    info_label.place(x=640, y=111)

    support_label = Label(
        window,
        text="After-Hours Support: If you need help outside of these hours, please refer to our FAQ section or submit a request via our feedback form. We’ll respond as soon as possible during our next business hours.",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Regular", 19),
        wraplength=500,
        justify="left"
    )
    support_label.place(x=640, y=490)

    # Contact information labels
    email_label = Label(
        window,
        text="Email: ",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Black", 19)
    )
    email_label.place(x=640, y=275)

    email_value_label = Label(
        window,
        text="support@pgcccalculator.edu",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Regular", 19)
    )
    email_value_label.place(x=680, y=308)

    phone_label = Label(
        window,
        text="Phone: ",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Black", 19)
    )
    phone_label.place(x=640, y=206)

    phone_value_label = Label(
        window,
        text="(301) 546-1234",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Regular", 19)
    )
    phone_value_label.place(x=680, y=233)

    hours_label = Label(
        window,
        text="Help & Support Hours of Operation:",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Black", 19)
    )
    hours_label.place(x=640, y=360)

    hours_value_label = Label(
        window,
        text="Monday - Thursdays: 8AM - 5PM\nFriday: 8AM - 3PM\nSaturday - Sunday: Closed",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Regular", 19),
        justify="left"
    )
    hours_value_label.place(x=680, y=387)

    # Add the buttons
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat"
    )
    button_1.place(x=1123, y=23, width=54, height=55)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat"
    )
    button_2.place(x=1075, y=25, width=50, height=50)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat"
    )
    button_3.place(x=1025, y=25, width=50, height=50)

    # Prevent resizing
    window.resizable(False, False)
    window.mainloop()

def open_helpWindow():
    from tkinter import Tk, Canvas, Button, PhotoImage
    from pathlib import Path

    # Define path to assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame4"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Initialize Tkinter window
    helpWindow = Tk()
    helpWindow.geometry("1200x675")
    helpWindow.configure(bg="#343346")

    # Set up canvas
    canvas = Canvas(
        helpWindow,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Load and place images
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(600.0, 168.0, image=image_image_1)

    # Create text on canvas
    canvas.create_text(
        378.0, 143.0,
        anchor="nw",
        text="Hello, How Can We Help?",
        fill="#FFFFFF",
        font=("Jost Bold", 36 * -1)
    )

    # Set up buttons with images
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: (helpWindow.destroy(), open_feedbackWindow())
    )
    button_1.place(x=837.5, y=338.0, width=250.0, height=200.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: (helpWindow.destroy(), open_contactWindow())
    )
    button_2.place(x=470.0, y=338.0, width=250.0, height=200.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: (helpWindow.destroy(), open_FAQWindow()),
    )
    button_3.place(x=112.5, y=338.0, width=250.0, height=200.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        bg="#343346",
        command=lambda: (helpWindow.destroy(), open_mainWindow())
    )
    button_4.place(x=1125.0, y=25.0, width=50.0, height=50.0)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        bg="#343346",
        command=lambda: (helpWindow.destroy(), open_helpWindow())
    )
    button_5.place(x=1075.0, y=25.0, width=50.0, height=50.0)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: (helpWindow.destroy(), open_recordsWindow()),
        bg="#343346"
    )
    button_6.place(x=1024.0, y=25.0, width=50.0, height=50.0)

    # Finalize and run
    helpWindow.resizable(False, False)
    helpWindow.mainloop()

def open_recordsWindow():
    from pathlib import Path
    from tkinter import Tk, Entry, Label, Button, PhotoImage, messagebox

    import sqlite3
    import re

    # Define the paths for output and assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame6"

    # Function to make asset paths relative to the project
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Create the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    def fetch_record(date, class_name):
        if re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', date):
            if re.match(r'^[A-Za-z][A-Za-z][A-Za-z]-\d\d\d\d[A-Za-z]?-[A-Za-z][A-Za-z]\d\d$', class_name):
                window.destroy()
                open_historyWindow(date, class_name)
            else:
                messagebox.showerror("Invalid input","Please enter the class in XXX-0000-XX00 where X is a capital letter and 0 is a digit.")
        else:
            messagebox.showerror("Invalid input","Please enter the date in YYYY-MM-DD.")
    # Header title
    header_label = Label(
        window,
        text="Credit Calculation History",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Black", 28)
    )
    header_label.place(x=392.5, y=39)

    # Description text
    description_label = Label(
        window,
        text="The credit calculation history serves as a dedicated space where you can access and review your most recent past credit hour calculations.",
        bg="#343346",
        fg="#FFFFFF",
        justify="center",
        font=("Jost Regular", 18),
        wraplength=1100,
    )
    description_label.place(x=77.5, y=85)

    # Label for "Enter a Date Below"
    date_label = Label(
        window,
        text="Enter a Date Below:",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Bold", 30)
    )
    date_label.place(x=80, y=203)

    # Entry field for date
    entry_1 = Entry(
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        font=("Arial", 14),
        highlightthickness=0
    )
    entry_1.place(x=121, y=254, width=250, height=48)

    # Label for "Enter a Course Number"
    course_label = Label(
        window,
        text="Enter a Course Number:",
        bg="#343346",
        fg="#FFFFFF",
        font=("Jost Bold", 30)
    )
    course_label.place(x=80, y=440)

    # Entry field for course number
    entry_2 = Entry(
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        font=("Arial", 14),
        highlightthickness=0
    )
    entry_2.place(x=121, y=487, width=250, height=48)

    # Add the buttons
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat"
    )
    button_1.place(x=1125, y=25, width=50, height=50)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat"
    )
    button_2.place(x=1077, y=25, width=50, height=50)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat"
    )
    button_3.place(x=1027, y=25, width=50, height=50)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        window,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg="#343346",
        command=lambda: (fetch_record(entry_1.get(), entry_2.get())),
        relief="flat"
    )
    button_4.place(x=739, y=279, width=180, height=178)

    # Prevent resizing
    window.resizable(False, False)
    window.mainloop()

def open_historyWindow(date, class_name):
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage, Text, messagebox

    import sqlite3

    # Define the asset paths
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame8"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Initialize the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Create a canvas for drawing
    canvas = Canvas(
        window,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Create and place buttons
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg = "#343346",
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat"
    )
    button_1.place(x=1123.0, y=23.0, width=54.0, height=55.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg = "#343346",
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat"
    )
    button_2.place(x=1075.0, y=25.0, width=50.0, height=50.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg = "#343346",
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat"
    )
    button_3.place(x=1025.0, y=25.0, width=50.0, height=50.0)

    # Create text labels
    canvas.create_text(
        371.0,
        39.0,
        anchor="nw",
        text="Credit Calculation History",
        fill="#FFFFFF",
        font=("Jost Black", 28 * -1)
    )

    canvas.create_text(
        46.0,
        85.0,
        anchor="nw",
        text="The credit calculation history serves as a dedicated space where you can access and review your most recent past credit hour calculations.",
        fill="#FFFFFF",
        font=("Jost Regular", 18 * -1)
    )

    # Create a text box for results
    result_text = Text(
        bd=0,
        bg="#313241",
        fg="#000716",
        highlightthickness=0
    )
    result_text.tag_configure("class_name", font=("Arial", 24, "bold"))
    result_text.place(x=72.0, y=222.0, width=1078.0, height=292.0)

    # Create and place action buttons
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg = "#343346",
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(x=800.0, y=574.0, width=220.0, height=35.0)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        bg = "#343346",
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat"
    )
    button_6.place(x=180.0, y=574.0, width=220.0, height=35.0)

    canvas.create_text(
        72.0,
        176.0,
        anchor="nw",
        text="Here Are Your Results...",
        fill="#FFFFFF",
        font=("Jost Regular", 30 * -1)
    )

    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    try:
        # Query to fetch the record based on date and class_name
        cursor.execute('''
            SELECT * FROM records WHERE date = ? AND class_name = ?
        ''', (date, class_name))
                    
        # Fetch the result
        record = cursor.fetchone()
        print(record)
                    
        if record:
            # Print the record details
            result_text.insert("1.0", "Record found:" + "\n")
            result_text.insert("2.0", "Date: " + record[0] + "\n")
            result_text.insert("3.0", "Time: " + record[1] + "\n")
            result_text.insert("4.0", "Class Name: " + record[2] + "\n")
            result_text.insert("5.0", "In Class Hours: " + str(record[3]) + "\n")
            result_text.insert("6.0", "Out of Class Hours: " + str(record[4]) + "\n")
            result_text.insert("7.0", "Credit Hours: " + str(record[5]) + "\n")
            result_text.tag_add("class_name", "1.0", "1.end")
            result_text.configure(fg="#FFFFFF")
            result_text.configure(state="disabled")  # Set to read-only
        else:
            messagebox.showerror("No record found","No record found for the specified date and class name.")                     
    except sqlite3.Error as e:
        print("An error occurred:", e)
    
    cursor.close()
    conn.close()

    # Disable window resizing
    window.resizable(False, False)

    # Run the application
    window.mainloop()

def open_adminDashboard():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage

    # Define paths to assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame9"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Create the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#D9D9D9")

    # Set up the canvas
    canvas = Canvas(
        window,
        bg="#D9D9D9",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Create background rectangles
    canvas.create_rectangle(
        0.0, 375.0, 450.0, 525.0,
        fill="#D9D9D9", outline=""
    )
    canvas.create_rectangle(
        0.0, 0.0, 1200.0, 375.0,
        fill="#343346", outline=""
    )

    # Add text to the canvas
    canvas.create_text(
        449.0, 18.0,
        anchor="nw",
        text="WELCOME ADMIN!",
        fill="#FFFFFF",
        justify="center",
        font=("Jost Black", 20)
    )
    canvas.create_text(
        315.0, 51.0,
        anchor="nw",
        text="PRINCE GEORGE’S COMMUNITY COLLEGE",
        fill="#FFFFFF",
        justify="center",
        font=("Jost ExtraLight", 20)
    )
    canvas.create_text(
        187.5, 123.0,
        anchor="nw",
        text=(
            "Welcome! Thank you for your dedication to fostering a supportive learning\n"
            "environment at Prince George's Community College. Your work in reviewing feedback and\n"
            "tracking academic progress directly impacts our students' success. We're grateful for\n"
            "your continued commitment to excellence and collaboration. Let’s make a difference together!"
        ),
        fill="#FFFFFF",
        justify="center",
        font=("Jost Regular", 15)
    )

    # Load images and create buttons
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_feedbackDataWindow()),
        relief="flat"
    )
    button_1.place(x=0.0, y=375.0, width=450.0, height=150.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_recordsDataWindow()),
        relief="flat"
    )
    button_2.place(x=0.0, y=525.0, width=450.0, height=150.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_loginWindow()),
        relief="flat"
    )
    button_3.place(x=450.0, y=525.0, width=450.0, height=150.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat"
    )
    button_4.place(x=450.0, y=375.0, width=450.0, height=150.0)

    # Place image on the canvas
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1049.0, 524.0, image=image_image_1
    )

    # Disable window resizing and run main loop
    window.resizable(False, False)
    window.mainloop()

def open_feedbackDataWindow():
    from pathlib import Path
    from tkinter import Tk, Canvas, Text, Button, PhotoImage, messagebox, Scrollbar, END
    import sqlite3

    # Define paths to assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame10"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Create the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Set up the canvas
    canvas = Canvas(
        window,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Add text to the canvas
    canvas.create_text(
        44.0, 35.0,
        anchor="nw",
        text="FEEDBACK & SURVEY RESPONSES",
        fill="#FFFFFF",
        font=("Jost Regular", 30)
    )

    # Create an entry background image and Text widget
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(599.5, 366.5, image=entry_image_1)

    entry_1 = Text(
        bd=0,
        bg="#1e1d28",
        fg="#FFFFFF",
        highlightthickness=0
    )

    scrollbar = Scrollbar(window, command=entry_1.yview)
    scrollbar.pack(side='right', fill='y')
    entry_1.config(yscrollcommand=scrollbar.set)

    entry_1.place(
        x=44.0,
        y=109.0,
        width=1111.0,
        height=513.0
    )

    # Add a button with an image
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_adminDashboard()),
        relief="flat"
    )
    button_1.place(
        x=933.0,
        y=35.0,
        width=222.0,
        height=43.0
    )


    # Connect to the SQLite database
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    # Execute the query to get all rows from the feedback table
    cursor.execute("SELECT * FROM feedback")

    # Fetch all the results (rows)
    rows = cursor.fetchall()

    # Clear the current content in the Text widget
    entry_1.delete(1.0, END)

    # Loop through the rows and insert each row into the Text widget
    for index, row in enumerate(rows, start=1):
        entry_1.insert(END, f"Index: {index}\n")
        entry_1.insert(END, f"ID: {row[0]}\n")
        entry_1.insert(END, f"Name: {row[1]}\n")
        entry_1.insert(END, f"Email: {row[2]}\n")
        entry_1.insert(END, f"Suggested Improvements: {row[3]}\n")
        entry_1.insert(END, f"Like Most: {row[4]}\n")
        entry_1.insert(END, f"Other: {row[5]}\n")
        entry_1.insert(END, f"Submission Date: {row[6]}\n")
        entry_1.insert(END, "-" * 50 + "\n")  # Separator between records

    # Close the connection
    conn.close()

    # Disable window resizing and run main loop
    window.resizable(False, False)
    window.mainloop()

def open_recordsDataWindow():
    from pathlib import Path
    from tkinter import Tk, Canvas, Text, Button, PhotoImage, END, Scrollbar
    import sqlite3

    # Define paths to assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame10"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # Create the main window
    window = Tk()
    window.geometry("1200x675")
    window.configure(bg="#343346")

    # Set up the canvas
    canvas = Canvas(
        window,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Add text to the canvas
    canvas.create_text(
        44.0, 35.0,
        anchor="nw",
        text="STUDENT REPORTS",
        fill="#FFFFFF",
        font=("Jost Regular", 30)
    )

    # Create an entry background image and Text widget
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(599.5, 366.5, image=entry_image_1)

    entry_1 = Text(
        bd=0,
        bg="#1e1d28",
        fg="#FFFFFF",
        highlightthickness=0
    )

    # Create a Scrollbar and link it to the Text widget
    scrollbar = Scrollbar(window, command=entry_1.yview)
    scrollbar.pack(side='right', fill='y')

    # Configure the Text widget to update the scrollbar position
    entry_1.config(yscrollcommand=scrollbar.set)

    entry_1.place(
        x=44.0,
        y=109.0,
        width=1111.0,
        height=513.0
    )

    # Add a button with an image
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), open_adminDashboard()),
        relief="flat"
    )
    button_1.place(
        x=933.0,
        y=35.0,
        width=222.0,
        height=43.0
    )

    # Connect to the SQLite database
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    # Execute the query to get all rows from the feedback table
    cursor.execute("SELECT * FROM records")

    # Fetch all the results (rows)
    rows = cursor.fetchall()

    # Clear the current content in the Text widget
    entry_1.delete(1.0, END)

    # Loop through the rows and insert each row into the Text widget
    for index, row in enumerate(rows):
        entry_1.insert('end', f"Index: {index + 1}\n")
        entry_1.insert('end', f"Date: {row[0]}\n")
        entry_1.insert('end', f"Time: {row[1]}\n")
        entry_1.insert('end', f"Class Name: {row[2]}\n")
        entry_1.insert('end', f"In-Class Hours: {row[3]}\n")
        entry_1.insert('end', f"Out-of-Class Hours: {row[4]}\n")
        entry_1.insert('end', f"Credit Hours: {row[5]}\n")
        entry_1.insert('end', "-" * 50 + '\n')

    # Close the connection
    conn.close()

    # Disable window resizing and run main loop
    window.resizable(False, False)
    window.mainloop()

def open_thankyouWindow():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame11"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("1200x675")
    window.configure(bg="#343346")

    canvas = Canvas(
        window,
        bg="#343346",
        height=675,
        width=1200,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    # Buttons at the top
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg=("#343346"),
        command=lambda: (window.destroy(), open_mainWindow()),
        relief="flat"
    )
    button_1.place(x=1123.0, y=23.0, width=54.0, height=55.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg=("#343346"),
        command=lambda: (window.destroy(), open_helpWindow()),
        relief="flat"
    )
    button_2.place(x=1075.0, y=25.0, width=50.0, height=50.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg=("#343346"),
        command=lambda: (window.destroy(), open_recordsWindow()),
        relief="flat"
    )
    button_3.place(x=1025.0, y=25.0, width=50.0, height=50.0)

    # Center ellipse
    canvas.create_oval(
        20.0, 56.0, 1179.0, 611.0,
        fill="#455D9A",
        outline=""
    )

    # Main message text
    canvas.create_text(
        63.0,
        267.0,
        anchor="nw",
        text="Thank you for using the Prince George’s Community College Credit Hour Calculator! We’re\nthrilled to support you in planning your academic journey and maximizing your course load\nefficiency. Our goal is to make your experience as smooth and valuable as possible, helping you\nfocus on what matters most—your education and success. We appreciate your time and trust in\nusing this tool and look forward to supporting you through each semester.",
        fill="#FFFFFF",
        justify="center",
        font=("Jost Regular", 25 * -1)
    )

    # Center button at the bottom
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg=("#455D9A"),
        command=lambda: (window.destroy(), open_loginWindow()),
        relief="flat"
    )
    button_4.place(x=546.0, y=507.0, width=112.0, height=94.0)

    # Top image
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(599.0, 161.0, image=image_image_1)

    window.resizable(False, False)
    window.mainloop()

open_loginWindow()
