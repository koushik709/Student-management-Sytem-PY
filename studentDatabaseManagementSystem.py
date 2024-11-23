######### ---------------------- main page buttons command
def addstudent():
    id_manual_flag = False
    def addstudent_submit():
        id = idval.get()
        name = nameval.get()
        father_name = fnameval.get()
        mother_name = mnamval.get()
        dob=dobval.get()
        gender=genderval.get()
        nationality=nationalityval.get()
        present_address=presentAddressval.get()
        religion=religionval.get()
        personal_phn_no=phoneval.get()
        email=emailval.get()
        blood_group=bloodval.get()
        try:
            query = """
                            INSERT INTO studentdata 
                            (id, name, father_name, mother_name, dob, gender, nationality, present_address, religion, personal_phn_no, email, blood_group)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
            values = (
            id, name, father_name, mother_name, dob, gender, nationality, present_address, religion, personal_phn_no,
            email, blood_group)

            # Execute query
            mycursor.execute(query, values)

            con.commit()
            res=messagebox.askyesnocancel('query','Did you enter the information correctly and proceed to submit?',parent= addroot)
            if(res==True):
                if not id_manual_flag:
                    serial_number = get_serial_number()
                    new_serial_number = increment_serial_number(serial_number)
                    idval.set(new_serial_number)
                    print(new_serial_number)
                    addroot.destroy()
            #datas = mycursor.fetchall()
            #mycursor.execute(res)
        except Exception as e:
            # Show error with exception details
            messagebox.showerror('Error', f"An error occurred: {e}", parent=addroot)



    def addstudent_cancel():
        addroot.destroy()

        # Function to get the current serial number from a file

    def get_serial_number():
        try:
            with open("login_serial.txt", "r") as file:
                serial_number = int(file.read().strip())
        except FileNotFoundError:
            serial_number = 0  # Start from 0 if the file does not exist
        return serial_number

        # Function to increment and save the serial number

    def increment_serial_number(serial_number):
        serial_number += 1
        with open("login_serial.txt", "w") as file:
            file.write(str(serial_number))
        return serial_number

        # Initialize the serial number at the start

    serial_number = get_serial_number()

    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry('700x550+310+80')
    addroot.resizable(False,False)
    addroot.config(bg = 'light blue')

    ### addroot add students label
    welcomelabel= Label(addroot,text= '----------------------------------------------Enter Student Details----------------------------------------------', font=('chiller',26,'bold'),bg='light blue')
    welcomelabel.pack(side= TOP,anchor='w' ,expand= True)

    id = Label(addroot, text='ID No                        :', font=('arial', 10, 'bold'), width=17, anchor='w',relief=RIDGE, borderwidth=3)
    id.pack(side=TOP, anchor='w', padx=30, expand=True)

    name = Label(addroot, text='Name                       :',font=('arial',10,'bold'),width=17,anchor='w', relief= RIDGE, borderwidth=3)
    name.pack(side= TOP,anchor='w',padx= 30, expand= True)

    fatherName = Label(addroot, text="Mother's Name         :", font=('arial', 10, 'bold'),width=17,anchor='w', relief=RIDGE, borderwidth=3)
    fatherName.pack(side=TOP,anchor='w',padx= 30, expand=True)

    motherName = Label(addroot, text="Father's Name          :",font=('arial',10,'bold'),width=17,anchor='w', relief= RIDGE, borderwidth=3)
    motherName.pack(side= TOP,anchor='w',padx= 30, expand= True)

    birthDate = Label(addroot, text='Date of Birth             :', font=('arial', 10, 'bold'),width=17,anchor='w', relief=RIDGE, borderwidth=3)
    birthDate.pack(side=TOP,anchor='w',padx= 30, expand=True)

    gender = Label(addroot, text='Gender                     :', font=('arial', 10, 'bold'),width=17, anchor='w',relief=RIDGE,borderwidth=3)
    gender.pack(side=TOP, anchor='w', padx=30, expand=True)

    nationality = Label(addroot, text='Nationality                :', font=('arial', 10, 'bold'),width=17,anchor='w', relief=RIDGE,borderwidth=3)
    nationality.pack(side=TOP, anchor='w', padx=30, expand=True)

    presentAddress = Label(addroot,   text='Present Address       :', font=('arial', 10, 'bold'),width=17, anchor='w',relief=RIDGE,borderwidth=3)
    presentAddress.pack(side=TOP, anchor='w', padx=30, expand=True)

    religion = Label(addroot, text='Religion                   :', font=('arial', 10, 'bold'), width=17, anchor='w',relief=RIDGE, borderwidth=3)
    religion.pack(side=TOP, anchor='w', padx=30, expand=True)

    phone = Label(addroot, text='Personal Phone No  :', font=('arial', 10, 'bold'), width=17, anchor='w',relief=RIDGE, borderwidth=3)
    phone.pack(side=TOP, anchor='w', padx=30, expand=True)

    email = Label(addroot, text='Email Address          :', font=('arial', 10, 'bold'), width=17, anchor='w',relief=RIDGE, borderwidth=3)
    email.pack(side=TOP, anchor='w', padx=30, expand=True)

    blood = Label(addroot, text='Blood Group             :', font=('arial', 10, 'bold'), width=17, anchor='w',relief=RIDGE, borderwidth=3)
    blood.pack(side=TOP, anchor='w', padx=30, expand=True)


    ##--------- submit and home button
    submitButton = Button(addroot, text='Submit', font=('roman', 11, 'bold'),command=addstudent_submit, bg='gold2', bd=3, relief=RIDGE,borderwidth=3, width=15, height=1)
    submitButton.pack(side= TOP,pady=18, padx= 134,anchor='w',expand= True)

    cancelfromaddstudentbutton_home = Button(addroot, text='Cancel', font=('roman', 11, 'bold'),command=addstudent_cancel, bg='gold2', bd=3, relief=RIDGE,borderwidth=3, width=15, height=1)
    cancelfromaddstudentbutton_home.place(x= 450,y= 490)


    ######  entry boxes
    idval= StringVar()
    idval.set(serial_number)
    nameval= StringVar()
    fnameval= StringVar()
    mnamval= StringVar()
    dobval= StringVar()
    genderval= StringVar()
    nationalityval= StringVar()
    presentAddressval= StringVar()
    religionval= StringVar()
    phoneval= StringVar()
    emailval= StringVar()
    bloodval= StringVar()

    def id_manually():
        nonlocal id_manual_flag
        res1= messagebox.askyesnocancel('notofication','Do you proceed to add ID manually?')
        if res1==True:
            id_manual_flag = True
            identry.config(state="normal")


    identry = Entry(addroot, font=('arial', 13,'bold'), width=35, bg='light yellow',textvariable=idval,state="disabled")
    identry.place(x=195, y=64)

    enter_id_manually = Button(addroot, text='Enter ID Manually', font=('chiller', 9, 'bold'),command=id_manually,

                                                bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=16, height=1)
    enter_id_manually.place(x=524, y=61)

    nameentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=nameval)
    nameentry.place(x=195,y= 97)

    fnameentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=fnameval)
    fnameentry.place(x=195,y= 132)

    mnameentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=mnamval)
    mnameentry.place(x=195,y= 166)

    birthentry= DateEntry(addroot, font=('arial', 13), date_pattern='dd/mm/yyyy',bd=1, width=48,bg='light yellow',textvariable=dobval)
    birthentry.place(x=195,y= 199)

    genderentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=genderval)
    genderentry.place(x=195,y= 234)

    nationalityentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=nationalityval)
    nationalityentry.place(x=195,y= 267)

    presentAddressentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=presentAddressval)
    presentAddressentry.place(x=195,y= 301)

    religionSTR = ["Muslim", "Hindu", "Buddha", "Christian", "Others"]
    religionentry = OptionMenu(addroot, religionval, *religionSTR)
    religionentry.config(width=69,bd=1,)
    religionentry.place(x=195,y= 334)

    personalphoneentry= Entry(addroot, font=('arial', 13), width=50,bg='light yellow',textvariable=phoneval)
    personalphoneentry.place(x=195,y= 371)

    emailentry = Entry(addroot, font=('arial', 13), width=50, bg='light yellow',textvariable=emailval)
    emailentry.place(x=195, y=407)

    bloodentry = Entry(addroot, font=('arial', 13), width=50, bg='light yellow',textvariable=bloodval)
    bloodentry.place(x=195, y=441)

    addroot.mainloop()


def  searchstudent():
    def searchAll():
        try:
            str1= 'select * from studentdata'
            mycursor.execute(str1)
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)
        except:
            messagebox.showerror('Error','Connect to your database')
            searchroot.destroy()




    def searchstudent_Search():
        id = idval.get()
        name = nameval.get()
        gender=genderval.get()
        religion=religionval.get()
        blood_group=bloodval.get()

        if id != '':
            str1= 'SELECT * FROM studentdata WHERE id=%s'
            mycursor.execute(str1,(id,))
            datas= mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]
                searchstudenttable.insert('',END,values=val)

        if name != '':
            str1 = 'SELECT * FROM studentdata WHERE name LIKE %s'
            name_search = f"%{name}%"
            mycursor.execute(str1, (name_search,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if gender != '':
            str1 = 'SELECT * FROM studentdata WHERE gender=%s'
            mycursor.execute(str1, (gender,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if religion != '':
            str1 = 'SELECT * FROM studentdata WHERE religion=%s'
            mycursor.execute(str1, (religion,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if blood_group != '':
            str1 = 'SELECT * FROM studentdata WHERE blood_group=%s'
            mycursor.execute(str1, (blood_group,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

    def searchstudent_cancel():
        searchroot.destroy()

    searchroot = Toplevel()
    searchroot.grab_set()
    searchroot.geometry('1200x550+30+50')
    searchroot.resizable(False, False)
    searchroot.config(bg='light yellow')

    welcomesearchstudentlabel = Label(searchroot, text='Search Student Details', font=('chiller',36,'bold'),bg='light yellow').pack(side=TOP,pady=5)
    #welcomesearchstudentlabel.place(x=450,y=10)

    ### searchroot search students label

    leftFrame = Frame(searchroot, bg= 'light yellow',bd=3, relief=GROOVE, borderwidth=5)
    leftFrame.place(x=20,y=80,width= 400, height= 440)

    rightFrame = Frame(searchroot, bg= 'light yellow',bd=3, relief=GROOVE, borderwidth=5)
    rightFrame.place(x=450,y=80,width= 730, height= 440)

    welcomelabel = Label(leftFrame,
                         text='------------------------------Search Student By------------------------------',
                         font=('chiller', 22, 'bold'), bg='light yellow')
    welcomelabel.pack(side=TOP, anchor='w', expand=True)

    id = Label(leftFrame, text='ID No            :', font=('arial', 10, 'bold'), width=11, anchor='w',
               relief=RIDGE, borderwidth=3)
    id.pack(side=TOP, anchor='w', padx=20, expand=True)

    name = Label(leftFrame, text='Name           :', font=('arial', 10, 'bold'), width=11, anchor='w',
                 relief=RIDGE, borderwidth=3)
    name.pack(side=TOP, anchor='w', padx=20, expand=True)



    gender = Label(leftFrame, text='Gender         :', font=('arial', 10, 'bold'), width=11, anchor='w',
                   relief=RIDGE, borderwidth=3)
    gender.pack(side=TOP, anchor='w', padx=20, expand=True)


    religion = Label(leftFrame, text='Religion       :', font=('arial', 10, 'bold'), width=11, anchor='w',
                           relief=RIDGE, borderwidth=3)
    religion.pack(side=TOP, anchor='w', padx=20, expand=True)

    blood = Label(leftFrame, text='Blood Group :', font=('arial', 10, 'bold'), width=11, anchor='w',
                  relief=RIDGE, borderwidth=3)
    blood.pack(side=TOP, anchor='w', padx=20, expand=True)

    ##--------- Search and home button
    SearchButton = Button(leftFrame, text='Search', font=('roman', 11, 'bold'), command=searchstudent_Search, bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    SearchButton.pack(side=TOP, pady=18, padx=8, anchor='w', expand=True)

    SearchAllButton = Button(leftFrame, text='Show All', font=('roman', 11, 'bold'), command=searchAll,
                          bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    SearchAllButton.place(x=137,y=365)

    cancelfromsearchstudentbutton_home = Button(leftFrame, text='Cancel', font=('roman', 11, 'bold'), command=searchstudent_cancel,
                                           bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    cancelfromsearchstudentbutton_home.place(x=265, y=365)

    ######  entry boxes
    idval = StringVar()
    nameval = StringVar()
    genderval = StringVar()
    religionval = StringVar()
    bloodval = StringVar()

    identry = Entry(leftFrame, font=('arial', 13), bd=2, width=25, bg='light blue', textvariable=idval)
    identry.place(x=125, y=82)

    nameentry = Entry(leftFrame, font=('arial', 13),bd=2, width=25, bg='light blue', textvariable=nameval)
    nameentry.place(x=125, y=135)

    genderentry = Entry(leftFrame, font=('arial', 13),bd=2, width=25, bg='light blue', textvariable=genderval)
    genderentry.place(x=125, y=189)

    religionSTR= ["Muslim","Hindu", "Buddha", "Christian", "Others"]
    religionentry = OptionMenu(leftFrame, religionval,*religionSTR)
    religionentry.config(width= 31, bg= 'light blue',bd=1)
    religionentry.place(x=125, y=240)

    bloodentry = Entry(leftFrame, font=('arial', 13),bd=2, width=25, bg='light blue', textvariable=bloodval)
    bloodentry.place(x=125, y=295)

    ##################################search student table
    style= ttk.Style()
    style.configure('Treeview.Heading',font=('times',13,'bold'),foreground= 'blue',background= 'ash')
    style.configure('Treeview',font=('times',12,'bold'),foreground= 'black',background='cyan')
    scroll_x= Scrollbar(rightFrame, orient=HORIZONTAL)
    scroll_y=Scrollbar(rightFrame,orient=VERTICAL)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    searchstudenttable = Treeview(rightFrame,columns=('Id','Name',"Mother's name","Father's name",'Date of Birth','Gender','Nationality','Present Address','Religion','Personal Phn No','Email','Blood Group'),yscrollcommand= scroll_y.set, xscrollcommand= scroll_x.set)
    scroll_x.config(command=searchstudenttable.xview)
    scroll_y.config(command=searchstudenttable.yview)

    searchstudenttable.heading('Id',text='Id')
    searchstudenttable.heading('Name',text='Name')
    searchstudenttable.heading("Mother's name",text="Mother's name")
    searchstudenttable.heading("Father's name",text="Father's name")
    searchstudenttable.heading('Date of Birth',text='Date of Birth')
    searchstudenttable.heading('Gender',text='Gender')
    searchstudenttable.heading('Nationality',text='Nationality')
    searchstudenttable.heading('Present Address',text='Present Address')
    searchstudenttable.heading('Religion',text='Religion')
    searchstudenttable.heading('Personal Phn No',text='Personal Phn No')
    searchstudenttable.heading('Email',text='Email')
    searchstudenttable.heading('Blood Group',text='Blood Group')
    searchstudenttable['show']= 'headings'
    searchstudenttable.column('Id',width=100)
    searchstudenttable.column('Name',width=200)
    searchstudenttable.column("Mother's name",width=150)
    searchstudenttable.column("Father's name",width=150)
    searchstudenttable.column('Date of Birth',width=100)
    searchstudenttable.column('Gender',width=100)
    searchstudenttable.column('Nationality',width=100)
    searchstudenttable.column('Present Address',width=400)
    searchstudenttable.column('Religion',width=100)
    searchstudenttable.column('Personal Phn No',width=100)
    searchstudenttable.column('Email',width=100)
    searchstudenttable.column('Blood Group',width=100)
    searchstudenttable.pack(fill=BOTH,expand= 1)

    searchroot.mainloop()


def deletestudent():

    def deletebutton_delete():
        opt= searchstudenttable.focus()
        content= searchstudenttable.item(opt)
        opt2= content['values'][0]
        str1='DELETE FROM studentdata where id=%s'
        mycursor.execute(str1,(opt2))
        con.commit()
        messagebox.showinfo('notification','Id {} deleted successfully'.format(opt2))

        str1 = 'SELECT * FROM studentdata'
        mycursor.execute(str1)
        datas = mycursor.fetchall()
        searchstudenttable.delete(*searchstudenttable.get_children())
        for i in datas:
            val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            searchstudenttable.insert('', END, values=val)


    '''def searchAll():
        try:
            str1 = 'select * from studentdata'
            mycursor.execute(str1)
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)
        except:
            messagebox.showerror('Error', 'Connect to your database')'''

    def searchstudent_Search():
        id = idval.get()
        name = nameval.get()
        gender = genderval.get()
        religion = religionval.get()
        blood_group = bloodval.get()

        if id != '':
            str1 = 'SELECT * FROM studentdata WHERE id=%s'
            mycursor.execute(str1, (id,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if name != '':
            str1 = 'SELECT * FROM studentdata WHERE name LIKE %s'
            name_search = f"%{name}%"
            mycursor.execute(str1, (name_search,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if gender != '':
            str1 = 'SELECT * FROM studentdata WHERE gender=%s'
            mycursor.execute(str1, (gender,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if religion != '':
            str1 = 'SELECT * FROM studentdata WHERE religion=%s'
            mycursor.execute(str1, (religion,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

        if blood_group != '':
            str1 = 'SELECT * FROM studentdata WHERE blood_group=%s'
            mycursor.execute(str1, (blood_group,))
            datas = mycursor.fetchall()
            searchstudenttable.delete(*searchstudenttable.get_children())
            for i in datas:
                val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                searchstudenttable.insert('', END, values=val)

    def searchstudent_cancel():
        deleteroot.destroy()

    deleteroot = Toplevel()
    deleteroot.grab_set()
    deleteroot.geometry('1200x550+30+50')
    deleteroot.resizable(False, False)
    deleteroot.config(bg='light yellow')

    welcomesearchstudentlabel = Label(deleteroot, text='Search Student Details', font=('chiller', 36, 'bold'),
                                      bg='light yellow').pack(side=TOP, pady=5)
    # welcomesearchstudentlabel.place(x=450,y=10)

    ### deleteroot search students label

    leftFrame = Frame(deleteroot, bg='light yellow', bd=3, relief=GROOVE, borderwidth=5)
    leftFrame.place(x=20, y=80, width=400, height=440)

    rightFrame = Frame(deleteroot, bg='light yellow', bd=3, relief=GROOVE, borderwidth=5)
    rightFrame.place(x=450, y=80, width=730, height=440)

    welcomelabel = Label(leftFrame,
                         text='------------------------------Search Student By------------------------------',
                         font=('chiller', 22, 'bold'), bg='light yellow')
    welcomelabel.pack(side=TOP, anchor='w', expand=True)

    id = Label(leftFrame, text='ID No            :', font=('arial', 10, 'bold'), width=11, anchor='w',
               relief=RIDGE, borderwidth=3)
    id.pack(side=TOP, anchor='w', padx=20, expand=True)

    name = Label(leftFrame, text='Name           :', font=('arial', 10, 'bold'), width=11, anchor='w',
                 relief=RIDGE, borderwidth=3)
    name.pack(side=TOP, anchor='w', padx=20, expand=True)

    gender = Label(leftFrame, text='Gender         :', font=('arial', 10, 'bold'), width=11, anchor='w',
                   relief=RIDGE, borderwidth=3)
    gender.pack(side=TOP, anchor='w', padx=20, expand=True)

    religion = Label(leftFrame, text='Religion       :', font=('arial', 10, 'bold'), width=11, anchor='w',
                     relief=RIDGE, borderwidth=3)
    religion.pack(side=TOP, anchor='w', padx=20, expand=True)

    blood = Label(leftFrame, text='Blood Group :', font=('arial', 10, 'bold'), width=11, anchor='w',
                  relief=RIDGE, borderwidth=3)
    blood.pack(side=TOP, anchor='w', padx=20, expand=True)



    ##--------- Search and home button
    SearchButton = Button(leftFrame, text='Search', font=('roman', 11, 'bold'), command=searchstudent_Search,
                          bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    SearchButton.pack(side=TOP, pady=18, padx=8, anchor='w', expand=True)

    deletebutton = Button(leftFrame, text='Delete', font=('roman', 11, 'bold'), command=deletebutton_delete,
                             bg='gold2',
                             bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    deletebutton.place(x=137, y=365)

    cancelfromsearchstudentbutton_home = Button(leftFrame, text='Cancel', font=('roman', 11, 'bold'),
                                                command=searchstudent_cancel,
                                                bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    cancelfromsearchstudentbutton_home.place(x=265, y=365)

    ######  entry boxes
    idval = StringVar()
    nameval = StringVar()
    genderval = StringVar()
    religionval = StringVar()
    bloodval = StringVar()

    identry = Entry(leftFrame, font=('arial', 13), bd=2, width=25, bg='light blue', textvariable=idval)
    identry.place(x=125, y=82)

    nameentry = Entry(leftFrame, font=('arial', 13), bd=2, width=25, bg='light blue', textvariable=nameval)
    nameentry.place(x=125, y=135)

    genderentry = Entry(leftFrame, font=('arial', 13), bd=2, width=25, bg='light blue', textvariable=genderval)
    genderentry.place(x=125, y=189)

    religionSTR = ["Muslim", "Hindu", "Buddha", "Christian", "Others"]
    religionentry = OptionMenu(leftFrame, religionval, *religionSTR)
    religionentry.config(width=31, bg='light blue', bd=1)
    religionentry.place(x=125, y=240)

    bloodentry = Entry(leftFrame, font=('arial', 13), bd=2, width=25, bg='light blue', textvariable=bloodval)
    bloodentry.place(x=125, y=295)

    ##################################search student table
    style = ttk.Style()
    style.configure('Treeview.Heading', font=('times', 13, 'bold'), foreground='blue', background='ash')
    style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', background='cyan')
    scroll_x = Scrollbar(rightFrame, orient=HORIZONTAL)
    scroll_y = Scrollbar(rightFrame, orient=VERTICAL)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    searchstudenttable = Treeview(rightFrame, columns=(
    'Id', 'Name', "Mother's name", "Father's name", 'Date of Birth', 'Gender', 'Nationality', 'Present Address',
    'Religion', 'Personal Phn No', 'Email', 'Blood Group'), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    scroll_x.config(command=searchstudenttable.xview)
    scroll_y.config(command=searchstudenttable.yview)
    searchstudenttable.heading('Id', text='Id')
    searchstudenttable.heading('Name', text='Name')
    searchstudenttable.heading("Mother's name", text="Mother's name")
    searchstudenttable.heading("Father's name", text="Father's name")
    searchstudenttable.heading('Date of Birth', text='Date of Birth')
    searchstudenttable.heading('Gender', text='Gender')
    searchstudenttable.heading('Nationality', text='Nationality')
    searchstudenttable.heading('Present Address', text='Present Address')
    searchstudenttable.heading('Religion', text='Religion')
    searchstudenttable.heading('Personal Phn No', text='Personal Phn No')
    searchstudenttable.heading('Email', text='Email')
    searchstudenttable.heading('Blood Group', text='Blood Group')
    searchstudenttable['show'] = 'headings'
    searchstudenttable.column('Id', width=100)
    searchstudenttable.column('Name', width=200)
    searchstudenttable.column("Mother's name", width=150)
    searchstudenttable.column("Father's name", width=150)
    searchstudenttable.column('Date of Birth', width=100)
    searchstudenttable.column('Gender', width=100)
    searchstudenttable.column('Nationality', width=100)
    searchstudenttable.column('Present Address', width=400)
    searchstudenttable.column('Religion', width=100)
    searchstudenttable.column('Personal Phn No', width=100)
    searchstudenttable.column('Email', width=100)
    searchstudenttable.column('Blood Group', width=100)
    searchstudenttable.pack(fill=BOTH, expand=1)

    try:
        str1 = 'select * from studentdata'
        mycursor.execute(str1)
        datas = mycursor.fetchall()
        searchstudenttable.delete(*searchstudenttable.get_children())
        for i in datas:
            val = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            searchstudenttable.insert('', END, values=val)
    except:
        messagebox.showerror('Error', 'Connect to your database')
        deleteroot.destroy()

    deleteroot.mainloop()


def updatestudent():
    def updatestudent_cancel():
        updateroot.destroy()

    def updatestudent_update():
        try:
            # Get the updated values from the entry fields
            id = idval.get()
            name = nameval.get()
            father_name = fnameval.get()
            mother_name = mnamval.get()
            dob = dobval.get()
            gender = genderval.get()
            nationality = nationalityval.get()
            present_address = presentAddressval.get()
            religion = religionval.get()
            personal_phn_no = phoneval.get()
            email = emailval.get()
            blood_group = bloodval.get()

            # Ensure that the ID is provided (as we need it to identify the student)
            if id == '':
                messagebox.showerror('Error', 'Student ID is required to update details')
                return

            # Prepare the SQL query to update student data
            str1 = '''UPDATE studentdata SET 
                        name=%s, father_name=%s, mother_name=%s, dob=%s, gender=%s, 
                        nationality=%s, present_address=%s, religion=%s, personal_phn_no=%s, 
                        email=%s, blood_group=%s 
                      WHERE id=%s'''

            # Execute the query with the updated values
            mycursor.execute(str1, (name, father_name, mother_name, dob, gender, nationality,
                                    present_address, religion, personal_phn_no, email, blood_group, id))

            # Commit the changes to the database
            con.commit()

            # Display success message
            messagebox.showinfo('Success', 'Student details updated successfully!')

        except Exception as e:
            messagebox.showerror('Error', f'Could not update data: {str(e)}')

    def updatestudent_searchByID():
        try:
            id = idval.get()

            if id != '':
                str1 = 'SELECT * FROM studentdata WHERE id=%s'
                mycursor.execute(str1, (id,))

                student_data = mycursor.fetchone()

                if student_data:
                    identry.delete(0, END)
                    identry.insert(0, student_data[0])

                    nameentry.delete(0, END)
                    nameentry.insert(0, student_data[1])

                    fnameentry.delete(0, END)
                    fnameentry.insert(0, student_data[2])

                    mnameentry.delete(0, END)
                    mnameentry.insert(0, student_data[3])

                    genderentry.delete(0, END)
                    genderentry.insert(0, student_data[5])

                    birthentry.delete(0, END)
                    birthentry.insert(0, student_data[4])

                    nationalityentry.delete(0, END)
                    nationalityentry.insert(0, student_data[6])

                    presentAddressentry.delete(0, END)
                    presentAddressentry.insert(0, student_data[7])

                    personalphoneentry.delete(0, END)
                    personalphoneentry.insert(0, student_data[9])

                    emailentry.delete(0, END)
                    emailentry.insert(0, student_data[10])

                    bloodentry.delete(0, END)
                    bloodentry.insert(0, student_data[11])

                    religionentry.delete(0, END)
                    religionentry.insert(0, student_data[8])
                else:
                    messagebox.showerror('Error', 'Student not found for the given ID')
            else:
                messagebox.showwarning('Input Error', 'Please enter an ID to search')

        except Exception as e:
            messagebox.showerror('Error', f'Could not fetch data: {str(e)}')

    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry('700x550+310+80')
    updateroot.resizable(False, False)
    updateroot.config(bg='light blue')

    ### updateroot update students label
    welcomelabel = Label(updateroot,
                         text='----------------------------------------------Update Student Details----------------------------------------------',
                         font=('chiller', 26, 'bold'), bg='light blue')
    welcomelabel.pack(side=TOP, anchor='w', expand=True)

    id = Label(updateroot, text='ID No                        :', font=('arial', 10, 'bold'), width=17, anchor='w',
               relief=RIDGE, borderwidth=3)
    id.pack(side=TOP, anchor='w', padx=30, expand=True)

    name = Label(updateroot, text='Name                       :', font=('arial', 10, 'bold'), width=17, anchor='w',
                 relief=RIDGE, borderwidth=3)
    name.pack(side=TOP, anchor='w', padx=30, expand=True)

    fatherName = Label(updateroot, text="Mother's Name         :", font=('arial', 10, 'bold'), width=17, anchor='w',
                       relief=RIDGE, borderwidth=3)
    fatherName.pack(side=TOP, anchor='w', padx=30, expand=True)

    motherName = Label(updateroot, text="Father's Name          :", font=('arial', 10, 'bold'), width=17, anchor='w',
                       relief=RIDGE, borderwidth=3)
    motherName.pack(side=TOP, anchor='w', padx=30, expand=True)

    birthDate = Label(updateroot, text='Date of Birth             :', font=('arial', 10, 'bold'), width=17, anchor='w',
                      relief=RIDGE, borderwidth=3)
    birthDate.pack(side=TOP, anchor='w', padx=30, expand=True)

    gender = Label(updateroot, text='Gender                     :', font=('arial', 10, 'bold'), width=17, anchor='w',
                   relief=RIDGE, borderwidth=3)
    gender.pack(side=TOP, anchor='w', padx=30, expand=True)

    nationality = Label(updateroot, text='Nationality                :', font=('arial', 10, 'bold'), width=17, anchor='w',
                        relief=RIDGE, borderwidth=3)
    nationality.pack(side=TOP, anchor='w', padx=30, expand=True)

    presentAddress = Label(updateroot, text='Present Address       :', font=('arial', 10, 'bold'), width=17, anchor='w',
                           relief=RIDGE, borderwidth=3)
    presentAddress.pack(side=TOP, anchor='w', padx=30, expand=True)

    religion = Label(updateroot, text='Religion                   :', font=('arial', 10, 'bold'), width=17, anchor='w',
                     relief=RIDGE, borderwidth=3)
    religion.pack(side=TOP, anchor='w', padx=30, expand=True)

    phone = Label(updateroot, text='Personal Phone No  :', font=('arial', 10, 'bold'), width=17, anchor='w', relief=RIDGE,
                  borderwidth=3)
    phone.pack(side=TOP, anchor='w', padx=30, expand=True)

    email = Label(updateroot, text='Email Address          :', font=('arial', 10, 'bold'), width=17, anchor='w',
                  relief=RIDGE, borderwidth=3)
    email.pack(side=TOP, anchor='w', padx=30, expand=True)

    blood = Label(updateroot, text='Blood Group             :', font=('arial', 10, 'bold'), width=17, anchor='w',
                  relief=RIDGE, borderwidth=3)
    blood.pack(side=TOP, anchor='w', padx=30, expand=True)

    ##--------- submit and home button
    updateButton = Button(updateroot, text='Update', font=('roman', 11, 'bold'), command=updatestudent_update, bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    updateButton.pack(side=TOP, pady=18, padx=134, anchor='w', expand=True)

    cancelfromupdatestudentbutton_home = Button(updateroot, text='Cancel', font=('roman', 11, 'bold'),
                                             command=updatestudent_cancel, bg='gold2', bd=3, relief=RIDGE, borderwidth=3,
                                             width=15, height=1)
    cancelfromupdatestudentbutton_home.place(x=450, y=490)

    searchButton = Button(updateroot, text='Search', font=('arial', 10, 'bold'), command=updatestudent_searchByID,
                          bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=11)
    searchButton.place(x=549, y=60)

    ######  entry boxes
    idval = StringVar()
    nameval = StringVar()
    fnameval = StringVar()
    mnamval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    nationalityval = StringVar()
    presentAddressval = StringVar()
    religionval = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    bloodval = StringVar()

    identry = Entry(updateroot, font=('arial', 13, 'bold'), width=38, bg='light yellow',  textvariable=idval)
    identry.place(x=195, y=64)

    nameentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=nameval)
    nameentry.place(x=195, y=97)

    fnameentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=fnameval)
    fnameentry.place(x=195, y=132)

    mnameentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=mnamval)
    mnameentry.place(x=195, y=166)

    birthentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=dobval)
    birthentry.place(x=195, y=200)

    genderentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=genderval)
    genderentry.place(x=195, y=234)

    nationalityentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=nationalityval)
    nationalityentry.place(x=195, y=267)

    presentAddressentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow',
                                textvariable=presentAddressval)
    presentAddressentry.place(x=195, y=301)

    religionentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=religionval)
    religionentry.place(x=195, y=336)

    personalphoneentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow',  textvariable=phoneval)
    personalphoneentry.place(x=195, y=371)

    emailentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow',  textvariable=emailval)
    emailentry.place(x=195, y=407)

    bloodentry = Entry(updateroot, font=('arial', 13), width=50, bg='light yellow', textvariable=bloodval,)
    bloodentry.place(x=195, y=441)

    updateroot.mainloop()


def showstudent():
    print('add')


def examstudent():
    #advance view and basic view
    '''def exam_searchbyID():
        try:
            id = idval.get()

            if id != '':
                str1 = 'SELECT * FROM studentdata WHERE id=%s'
                mycursor.execute(str1, (id,))

                student_data = mycursor.fetchone()

                if student_data:
                    identry.delete(0, END)
                    identry.insert(0, student_data[0])

                    nameentry.delete(0, END)
                    nameentry.insert(0, student_data[1])

                    fnameentry.delete(0, END)
                    fnameentry.insert(0, student_data[2])

                    mnameentry.delete(0, END)
                    mnameentry.insert(0, student_data[3])

                    genderentry.delete(0, END)
                    genderentry.insert(0, student_data[5])

                    birthentry.delete(0, END)
                    birthentry.insert(0, student_data[4])

                    nationalityentry.delete(0, END)
                    nationalityentry.insert(0, student_data[6])

                    presentAddressentry.delete(0, END)
                    presentAddressentry.insert(0, student_data[7])

                    personalphoneentry.delete(0, END)
                    personalphoneentry.insert(0, student_data[9])

                    emailentry.delete(0, END)
                    emailentry.insert(0, student_data[10])

                    bloodentry.delete(0, END)
                    bloodentry.insert(0, student_data[11])

                    religionentry.delete(0, END)
                    religionentry.insert(0, student_data[8])
                else:
                    messagebox.showerror('Error', 'Student not found for the given ID')
            else:
                messagebox.showwarning('Input Error', 'Please enter an ID to search')

        except Exception as e:
            messagebox.showerror('Error', f'Could not fetch data: {str(e)}')'''
    def advanceViewbutton():

        def advncesearchbutton():
            pass

        def advnceclearbutton():
            pass

        def advnceupdatebutton():
            pass

        def advncemarkenter():
            pass





        advncroot = Toplevel()
        advncroot.grab_set()
        advncroot.geometry('1600x550+100+100')
        advncroot.resizable(False, False)
        advncroot.config(bg='light yellow')

        downframe = Frame(advncroot,bg='light gray',relief=GROOVE,bd=3,borderwidth=5)
        downframe.place(x=20,y=105,width=1560,height= 430)



        #################lebels advance veiw
        idadvnce = Label(advncroot, text='ID No            :', font=('arial', 10, 'bold'), width=11, anchor='w',bg='light yellow')
        idadvnce.place(x=1120, y=20)

        idadvnce = Entry(advncroot, font=('arial', 13), bd=2, width=13, bg='light blue', textvariable=idval)
        idadvnce.place(x=1220, y=20)

        nameadvnce = Label(advncroot, text='Name           :', font=('arial', 10, 'bold'), width=11, anchor='w',
                    bg='light yellow', borderwidth=3)
        nameadvnce.place(x=20, y=15)

        getnameadvnce = Label(advncroot, text='shahriar kabir moon', font=('arial', 10, 'bold'), width=30, anchor='w', bg='light yellow', borderwidth=3)
        getnameadvnce.place(x=115, y=15)

        semesteradvnc = Label(advncroot, text='Semester       :', font=('arial', 10, 'bold'), width=11, anchor='w', bg='light yellow')
        semesteradvnc.place(x=280, y=15)

        getsemesteradvnc = Label(advncroot, text='spring 2024', font=('arial', 10, 'bold'), width=11, anchor='w',
                              bg='light yellow')
        getsemesteradvnc.place(x=380, y=15)

        deptadvnc = Label(advncroot, text='Dept. name  :', font=('arial', 10, 'bold'), width=11, anchor='w',
                              bg='light yellow')
        deptadvnc.place(x=540, y=15)

        getdeptadvnc = Label(advncroot, text='cse', font=('arial', 10, 'bold'), width=11, anchor='w', bg='light yellow')
        getdeptadvnc.place(x=640, y=15)

        intakeadvnc = Label(advncroot, text='Intake           :', font=('arial', 10, 'bold'), width=11, anchor='w', bg='light yellow')
        intakeadvnc.place(x=20, y=50)

        getintakeadvnc = Label(advncroot, text='51', font=('arial', 10, 'bold'), width=11, anchor='w',
                            bg='light yellow')
        getintakeadvnc.place(x=120, y=50)

        secadvnc = Label(advncroot, text='Section          :', font=('arial', 10, 'bold'), width=11, anchor='w',
                          bg='light yellow')
        secadvnc.place(x=280, y=50)

        getsecadvnc = Label(advncroot, text='13', font=('arial', 10, 'bold'), width=11, anchor='w',
                         bg='light yellow')
        getsecadvnc.place(x=380, y=50)

        cgpaadvnc = Label(advncroot, text='CGPA           :', font=('arial', 10, 'bold'), width=11, anchor='w',
                          bg='light yellow')
        cgpaadvnc.place(x=540, y=50)

        getcgpaadvnc = Label(advncroot, text='3.97', font=('arial', 10, 'bold'), width=11, anchor='w',
                          bg='light yellow')
        getcgpaadvnc.place(x=640, y=50)

        searchbuttonadvnce = Button(advncroot, text='Search', font=('arial', 10, 'bold'), bg='gold2', bd=3, relief=RIDGE,
                              borderwidth=3, width=11, height=1, command=searchbutton_search)
        searchbuttonadvnce.place(x=1370, y=16)


        advncclearbutton = Button(advncroot, text='Clear', font=('arial', 10, 'bold'), bg='gold2', bd=3, relief=RIDGE,
                              borderwidth=3, width=11, height=1, command=advnceclearbutton)
        advncclearbutton.place(x=1490, y=16)

        advncemarkbutton = Button(advncroot, text='Enter Total Marks', font=('arial', 10, 'bold'), bg='gold2', bd=3,
                                    relief=RIDGE,
                                    borderwidth=3, width=14, height=1,command=advncemarkenter)
        advncemarkbutton.place(x=1220, y=60)

        advnceupdatebutton = Button(advncroot, text='Update Marks', font=('arial', 10, 'bold'), bg='gold2', bd=3,
                                    relief=RIDGE,
                                    borderwidth=3, width=11, height=1, command=advnceupdatebutton)
        advnceupdatebutton.place(x=1370, y=60)

        advncecancelbutton = Button(advncroot, text='Cancel', font=('arial', 10, 'bold'), bg='gold2', bd=3,
                                    relief=RIDGE,
                                    borderwidth=3, width=11, height=1, command=searchbutton_search)
        advncecancelbutton.place(x=1490, y=60)

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('times', 13, 'normal'), foreground='black', background='ash')
        style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', background='cyan')
        scroll_x = Scrollbar(downframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(downframe, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        advnctreetable= Treeview(downframe,columns=('Course Title','Attendance mark','Assignment 1','Assignment 2','Average Assignment','Class Test 1(CT-1)','Class Test 2(CT-2)','Class Test 3(CT-3)','Average CT Mark','Presentation Mark','Average Class Performance','Mid Term','Final','Grade'),yscrollcommand= scroll_y.set, xscrollcommand= scroll_x.set)
        scroll_x.config(command=advnctreetable.xview)
        scroll_y.config(command=advnctreetable.yview)

        advnctreetable.heading('Course Title', text='Course Title')
        advnctreetable.heading('Attendance mark', text='Attendance mark')
        advnctreetable.heading('Assignment 1', text='Assignment 1')
        advnctreetable.heading('Assignment 2', text='Assignment 2')
        advnctreetable.heading('Average Assignment', text='Avg Assignment')
        advnctreetable.heading('Class Test 1(CT-1)', text='CT-1')
        advnctreetable.heading('Class Test 2(CT-2)', text='CT-2')
        advnctreetable.heading('Class Test 3(CT-3)', text='CT-3')
        advnctreetable.heading('Average CT Mark', text='Avg CT')
        advnctreetable.heading('Presentation Mark', text='Presentation')
        advnctreetable.heading('Average Class Performance', text='Avg Class Performance(30)')
        advnctreetable.heading('Mid Term', text='Mid Term (30)')
        advnctreetable.heading('Final', text='Final (40)')
        advnctreetable.heading('Grade', text='GPA')

        advnctreetable['show'] = 'headings'

        advnctreetable.column('Course Title', width=40)
        advnctreetable.column('Attendance mark', width=40)
        advnctreetable.column('Assignment 1', width=40)
        advnctreetable.column('Assignment 2', width=40)
        advnctreetable.column('Average Assignment', width=40)
        advnctreetable.column('Class Test 1(CT-1)', width=40)
        advnctreetable.column('Class Test 2(CT-2)', width=40)
        advnctreetable.column('Class Test 3(CT-3)', width=40)
        advnctreetable.column('Average CT Mark', width=40)
        advnctreetable.column('Presentation Mark', width=40)
        advnctreetable.column('Average Class Performance', width=40)
        advnctreetable.column('Mid Term', width=40)
        advnctreetable.column('Final', width=40)
        advnctreetable.column('Grade', width=40)

        advnctreetable.pack(fill=BOTH, expand=1)

        advncroot.mainloop()

    def searchbutton_search():
        pass
    def marksentrybutton_marks():
        advncexamroot = Toplevel()
        advncexamroot.grab_set()
        advncexamroot.geometry('500x600+500+50')
        advncexamroot.resizable(False, False)
        advncexamroot.config(bg='light yellow')

        advncexamroot.mainloop()

    def showallbutton_showall():
        pass

    def cancelbutton_cancel():
        pass

    examroot = Toplevel()
    examroot.grab_set()
    examroot.geometry('1200x550+30+50')
    examroot.resizable(False, False)
    examroot.config(bg='light yellow')

    welcomesearchstudentlabel = Label(examroot, text='Search Student Details', font=('chiller', 36, 'bold'),
                                      bg='light yellow').pack(side=TOP, pady=5)
    # welcomesearchstudentlabel.place(x=450,y=10)

    ###################examroot search students label

    leftFrame = Frame(examroot, bg='light yellow', bd=3, relief=GROOVE, borderwidth=5)
    leftFrame.place(x=20, y=80, width=330, height=440)

    rightFrame = Frame(examroot, bg='light yellow', bd=3, relief=GROOVE, borderwidth=5)
    rightFrame.place(x=380, y=80, width=800, height=440)

    welcomelabel = Label(leftFrame,
                         text='------------------------------Search Student By------------------------------',
                         font=('chiller', 22, 'bold'), bg='light yellow')
    welcomelabel.pack(side=TOP, anchor='w', expand=False)

    id = Label(leftFrame, text='ID No            :', font=('arial', 10, 'bold'), width=11, anchor='w',
               relief=RIDGE, borderwidth=3)
    id.place(x= 10,y=100)

    name = Label(leftFrame, text='Name           :', font=('arial', 10, 'bold'), width=11, anchor='w',
                 relief=RIDGE, borderwidth=3)
    name.place(x= 10,y=140)

    idval = StringVar()
    nameval = StringVar()

    identry = Entry(leftFrame, font=('arial', 13), bd=2, width=21, bg='light blue', textvariable=idval)
    identry.place(x=115 ,y=100)


    nameentry = Entry(leftFrame, font=('arial', 13), bd=2, width=21, bg='light blue', textvariable=nameval)
    nameentry.place(x= 115,y=140)

    searchbutton = Button(leftFrame, text='Search', font=('arial', 11, 'bold'),bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=11, height=1,command=searchbutton_search)
    searchbutton.place(x=35, y=250)

    showAllbutton = Button(leftFrame, text='Show All Marks', font=('arial', 11, 'bold'),bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=11, height=1,command=showallbutton_showall)
    showAllbutton.place(x=175, y=250)

    advanceViewButton = Button(leftFrame, text='Advance View', font=('arial', 11, 'bold'),bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=11, height=1,command=advanceViewbutton)
    advanceViewButton.place(x=35, y=300)

    marksentryButton = Button(leftFrame, text='Enter Marks', font=('arial', 11, 'bold'),bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=11, height=1,command=marksentrybutton_marks)
    marksentryButton.place(x=175, y=300)

    cancelButton = Button(leftFrame, text='Cancel', font=('arial', 11, 'bold'),bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=11, height=1,command=cancelbutton_cancel)
    cancelButton.place(x=35, y=350)



    ##--------- Search and home button
    '''SearchButton = Button(leftFrame, text='Search', font=('roman', 11, 'bold'),
                          bg='gold2',
                          bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    SearchButton.pack(side=TOP, pady=18, padx=8, anchor='w', expand=True)

    SearchAllButton = Button(leftFrame, text='Show All', font=('roman', 11, 'bold'),
                             bg='gold2',
                             bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    SearchAllButton.place(x=137, y=365)

    cancelfromsearchstudentbutton_home = Button(leftFrame, text='Cancel', font=('roman', 11, 'bold'),

                                                bg='gold2', bd=3, relief=RIDGE, borderwidth=3, width=15, height=1)
    cancelfromsearchstudentbutton_home.place(x=265, y=365)'''

    examroot.mainloop()



def student():
    print('add')


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do You Want To Exit?')
    if(res==True):
        root.destroy()

########################### connect db func

def ConnectDB():
    #root.destroy()

    def submitDB():
        global con, mycursor
        #host= hostval.get()
        #user= userval.get()
        #password= passwordval.get()

        host='localhost'
        user='root'
        password='02140731'
        try:
            con= pymysql.connect(host= host,user= user, password=password)
            mycursor= con.cursor()
            connectDBbutton.config(text='Connected',background='green',foreground='white' ,width=17)
        except:
            messagebox.showerror('notifications','user or password is incorrect. please try again',parent= dbroot)
            return
        try:
            mycursor.execute('CREATE DATABASE IF NOT EXISTS studentmanagementsystem')
            mycursor.execute('USE studentmanagementsystem')
            str1 = '''
                CREATE TABLE IF NOT EXISTS studentdata(
                    id INT NOT NULL PRIMARY KEY,
                    name VARCHAR(50),
                    father_name VARCHAR(50),
                    mother_name VARCHAR(50),
                    dob VARCHAR(20),
                    gender VARCHAR(20),
                    nationality VARCHAR(30),
                    present_address VARCHAR(300),
                    religion VARCHAR(20),
                    personal_phn_no VARCHAR(30),
                    email VARCHAR(100),
                    blood_group VARCHAR(10)
                )
            '''
            mycursor.execute(str1)
            con.commit()
            messagebox.showerror('notification','database has connected successfully',parent= dbroot)

        except Exception as e:
            messagebox.showerror('Database Connection Error', f'Error: {e}',parent= dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.geometry('400x300+700+170')
    dbroot.config(bg= 'light blue')

######------------------- dbroot labels
    hostnameLabel = Label(dbroot,text='Host name : ',bg='white', font=('arial', 11, 'bold'), relief=GROOVE, borderwidth=3,width=10,anchor='w')
    hostnameLabel.place(x=10,y=50)

    usernameLabel = Label(dbroot, text='User name : ', bg='white', font=('arial', 11, 'bold'), relief=GROOVE,borderwidth=3, width=10, anchor='w')
    usernameLabel.place(x=10, y=100)

    passwordLabel = Label(dbroot, text='Password  : ', bg='white', font=('arial', 11, 'bold'), relief=GROOVE,borderwidth=3, width=10, anchor='w')
    passwordLabel.place(x=10, y=150)

#########--------------- entry labels
    hostval= StringVar()
    userval=StringVar()
    passwordval=StringVar()
    hostEntry= Entry(dbroot, font=('times', 11,), relief=RIDGE,borderwidth=3,bg='white', width=37,textvariable=hostval)
    hostEntry.place(x=120,y=50)

    usernameEntry = Entry(dbroot, font=('times', 11,), relief=RIDGE, borderwidth=3, bg='white', width=37,textvariable=userval)
    usernameEntry.place(x=120, y=100)

    passwordEntry = Entry(dbroot, font=('times', 11,), relief=RIDGE, borderwidth=3, bg='white', width=37,textvariable= passwordval)
    passwordEntry.place(x=120, y=150)

    submitButton = Button(dbroot,text = 'Submit', font=('roman', 11, 'bold'), bg='gold2', bd= 3, relief= RIDGE, borderwidth= 3,width= 15,height=1,command=submitDB)
    submitButton.place(x=160, y=220)



    dbroot.mainloop()

######################## clock ticking
def tick():
    time_string= time.strftime("%H:%M:%S")
    date_string= time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200, tick)

############################### welcome to sdms part and mechs
import random
colors= ['red','green','blue','pink','red2','grey','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg = fg)
    SliderLabel.after(200,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if count>=len(ss):
        count = 0
        text = ''
        SliderLabel.config(text= text)
    else:
        text = text +ss[count]
        SliderLabel.config(text= text)
        count+=1
    SliderLabel.after(100, IntroLabelTick)


################################## root
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
from tkcalendar import DateEntry

import time
root = Tk()
root.title('student database management system')
root.geometry('1000x550+140+30')
root.config(bg='light yellow')
root.resizable(False,False)

######################################   main page
mainpage = Frame(root, bg= 'light grey', relief=GROOVE, borderwidth=5)
mainpage.place(x=20,y=80,width= 962, height= 450)

################################ slider label
ss= 'Welcome to Student Management System'
count = 0
text = ''
###################################### slider
SliderLabel = Label(root, text=ss,font=('chiller', 15, 'italic bold'),relief=RIDGE, borderwidth=4,width=42, bg='cyan')
SliderLabel.place(x=220,y=0)
IntroLabelTick()
IntroLabelColorTick()

################################   clock
clock = Label(root, font=('times', 10, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0,y=0)
tick()

######################################## connect database button
connectDBbutton= Button(root, text ='Connect To Database', font=('chiller', 13, 'italic bold'), relief=RIDGE, borderwidth=4, bg='blue', activebackground='red',activeforeground='white',command=ConnectDB )
connectDBbutton.place(x=815,y=0)


######################################## buttons of main pages
from PIL import Image, ImageTk

img1 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\add students.png")
img1 = img1.resize((120, 120), Image._initialized)
addstudentphoto = ImageTk.PhotoImage(img1)

addStudentButton = Button(root, image=addstudentphoto, width=120, height=120, relief=GROOVE, borderwidth=4,activebackground='red',command=addstudent)
addStudentButton.place(x=105, y=120)
addlabel = Label(root, text= 'Add Student', font=('chiller',16,'bold'))
addlabel.place(x=105,y=250)

## search student
img2 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\search student 3.png")
img2 = img2.resize((120, 120), Image._initialized)
searchstudentphoto = ImageTk.PhotoImage(img2)

searchstudentbutton = Button(root, image=searchstudentphoto,command=searchstudent, width=120, height=120, relief=GROOVE, borderwidth=4,activebackground='red')
searchstudentbutton.place(x=325, y=120)
addlabel = Label(root, text= 'Search Student', font=('chiller', 23,'bold'))
addlabel.place(x=312,y=250)

## delete student
img3 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\delete student.png")
img3 = img3.resize((120, 120), Image._initialized)
deletestudentphoto = ImageTk.PhotoImage(img3)

deletestudentbutton = Button(root, image=deletestudentphoto, width=120,command=deletestudent, height=120, relief=GROOVE, borderwidth=4,activebackground='red')
deletestudentbutton.place(x=545, y=120)
addlabel = Label(root, text= 'Delete Student', font=('chiller', 23,'bold'))
addlabel.place(x=532,y=250)

## update student
img4 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\update student 2.png")
img4 = img4.resize((120, 120), Image._initialized)
updatestudentphoto = ImageTk.PhotoImage(img4)

updatestudentbutton = Button(root, image=updatestudentphoto, width=120,command=updatestudent, height=120, relief=GROOVE, borderwidth=4,activebackground='red')
updatestudentbutton.place(x=765, y=120)
addlabel = Label(root, text= 'Update Student', font=('chiller', 23,'bold'))
addlabel.place(x=752,y=250)

## show all details
img5 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\show details.png")
img5 = img5.resize((120, 120), Image._initialized)
showstudentphoto = ImageTk.PhotoImage(img5)

showstudentbutton = Button(root, image=showstudentphoto, width=120, height=120,command=showstudent, relief=GROOVE, borderwidth=4,activebackground='red')
showstudentbutton.place(x=105, y=320)
addlabel = Label(root, text= 'Show Student Details', font=('chiller', 23,'bold'))
addlabel.place(x=62,y=450)

## enter student marks
img6 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\enter marrks 2.png")
img6 = img6.resize((120, 120), Image._initialized)
enterexamstudentphoto = ImageTk.PhotoImage(img6)

enterexamstudentbutton = Button(root, image=enterexamstudentphoto, width=120,command=examstudent, height=120, relief=GROOVE, borderwidth=4,activebackground='red')
enterexamstudentbutton.place(x=325, y=320)
addlabel = Label(root, text= 'Exam Details', font=('chiller', 23,'bold'))
addlabel.place(x=323,y=450)

#######################################show student data


## exit
img8 = Image.open(r"H:\My Drive\project and codes\python projects\sdms\pythonProject\icons\exit 2.png")
img8 = img8.resize((120, 120), Image._initialized)
exitstudentphoto = ImageTk.PhotoImage(img8)

exitstudentbutton = Button(root, image=exitstudentphoto, width=120, height=120, relief=GROOVE, borderwidth=4,activebackground='red', command=exitstudent)
exitstudentbutton.place(x=765, y=320)
addlabel = Label(root, text= 'EXIT', font=('chiller', 23,'bold'),width=10)
addlabel.place(x=767,y=450)

#############################
root.mainloop()