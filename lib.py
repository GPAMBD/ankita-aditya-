from tkinter import *
import datetime as dt




def event_issue_book():
    # event for issue book button
    def event_ib1():
        i = IssueBook()
        i.issue_book_to_student()
        i.write_issue_data_into_file()
        temp = Label(ib_base, text="Book issued Successfully!!!", bg="blue", foreground="red", font=16)
        temp.place(x=380, y=470)

    def event_ib2():
        ib_txt1.delete(0, END)
        ib_txt2.delete(0, END)
        ib_txt1.focus()

    # GUI for issue book
    ib_base = Tk()
    ib_base.geometry("950x630+370+20")
    ib_base.configure(bg="Blue")
    ib_base.title("Frame : Issue Book")
    ib_lb1 = Label(ib_base, text="ISSUE BOOK", font=("Arial bold", 19))
    ib_lb1.place(x=400, y=50)
    ib_lb2 = Label(ib_base, text="Student Enrollment Number", font=40, bg="black", foreground="white")
    ib_lb2.place(x=250, y=200)
    ib_lb3 = Label(ib_base, text="Book Number", font=40, bg="black", foreground="white")
    ib_lb3.place(x=342, y=270)
    ib_txt1 = Entry(ib_base, width="50")
    ib_txt1.place(x=470, y=200)
    ib_txt2 = Entry(ib_base, width="50")
    ib_txt2.place(x=470, y=270)
    ib_bn1 = Button(ib_base, text="Issue Book", height=2, width=15, bg="black", foreground="white", font=12,
                    command=event_ib1)
    ib_bn1.place(x=270, y=400)
    ib_bn2 = Button(ib_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12,
                    command=event_ib2)
    ib_bn2.place(x=550, y=400)


    # issue book
    class IssueBook:

        def issue_book_to_student(self):
            self.ib_s1 = str(ib_txt1.get())
            self.ib_s2 = str(ib_txt2.get())
            self.book_num = self.ib_s2
            self.stud_enr = self.ib_s1
            self.idate = str(dt.date.today())
            self.rdate = "NOT"
            self.ret_status = "NO"
            self.exp_rdate = str(dt.date.today() + dt.timedelta(7))
            # setting expected return_date afte 7 days

        def write_issue_data_into_file(self):
            fobj = open("issued_books.txt", "a")
            fobj.write(
                self.book_num + "," + self.stud_enr + "," + self.idate + "," + self.rdate + "," + self.ret_status + "," + self.exp_rdate + "\n")
            fobj.close()








# return book

def event_return_book():
    ib_base.destroy()
    anb_base.destroy()
    ans_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    rb_base.mainloop()


# event for return book button
def event_rb1():
    rb_s1 = str(rb_txt1.get())
    ret_bnum = rb_s1
    fobj = open("issued_books.txt", "r")
    fdata_ls = fobj.readlines()
    fobj.close()

    fobj = open("issued_books.txt", "w")
    for oneline in fdata_ls:
        if oneline.startswith(ret_bnum + ",") and oneline._contains_(",NO,"):
            rdate = str(dt.date.today())
            new_oneline = oneline.replace(",NOT,", "," + rdate + ",")
            new_oneline2 = new_oneline.replace(",NO,", ",YES,")
            fobj.write(new_oneline2)
        else:
            fobj.write(oneline)
    fobj.close()
    temp = Label(rb_base, text="Book returned Successfully!!!", bg="blue", foreground="red", font=16)
    temp.place(x=380, y=470)


def event_rb2():
    rb_txt1.delete(0, END)


# gui for return book
rb_base = Tk()
rb_base.geometry("950x630+370+20")
rb_base.configure(bg="Blue")
rb_base.title("Frame : Return Book")
rb_lb1 = Label(rb_base, text="RETURN BOOK", font=("Arial bold", 19))
rb_lb1.place(x=380, y=50)
rb_lb2 = Label(rb_base, text="Book Number (to return)", font=40, bg="black", foreground="white")
rb_lb2.place(x=250, y=250)
rb_txt1 = Entry(rb_base, width="50")
rb_txt1.place(x=470, y=250)
rb_bn1 = Button(rb_base, text="Return Book", height=2, width=15, bg="black", foreground="white", font=12,
                command=event_rb1)
rb_bn1.place(x=270, y=400)
rb_bn2 = Button(rb_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12)
rb_bn2.place(x=550, y=400)


# add new book

class BookInfo:
    def accept_book_info(self):
        self.bk_num = str(anb_txt1.get())
        self.bk_title = str(anb_txt2.get())
        self.bk_author = str(anb_txt3.get())
        self.bk_publication = str(anb_txt4.get())

    def write_bk_data_into_file(self):
        fobj = open("book_info.txt", "a")
        fobj.write(self.bk_num + "," + self.bk_title + "," + self.bk_author + "," + self.bk_publication + "\n")
        fobj.close()


def event_add_new_book():
    ib_base.destroy()
    rb_base.destroy()
    ans_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    anb_base.mainloop()


# event for add new book button
def event_anb1():
    b = BookInfo()
    b.accept_book_info()
    b.write_bk_data_into_file()
    temp = Label(anb_base, text="Book added!!!", bg="blue", foreground="red", font=16)
    temp.place(x=430, y=470)


def event_anb2():
    anb_txt1.delete(0, END)
    anb_txt2.delete(0, END)
    anb_txt3.delete(0, END)
    anb_txt4.delete(0, END)


# gui for add new book
anb_base = Tk()
anb_base.geometry("950x630+370+20")
anb_base.configure(bg="Blue")
anb_base.title("Frame : Add New Book")
anb_lb1 = Label(anb_base, text="ADD NEW BOOK", font=("Arial bold", 19))
anb_lb1.place(x=350, y=50)
anb_lb2 = Label(anb_base, text="Book Number", font=40, bg="black", foreground="white")
anb_lb2.place(x=300, y=130)
anb_lb3 = Label(anb_base, text="Book Title", font=40, bg="black", foreground="white")
anb_lb3.place(x=323, y=180)
anb_lb4 = Label(anb_base, text="Book Author", font=40, bg="black", foreground="white")
anb_lb4.place(x=313, y=230)
anb_lb5 = Label(anb_base, text="Book Publication", font=40, bg="black", foreground="white")
anb_lb5.place(x=280, y=280)
anb_txt1 = Entry(anb_base, width="50")
anb_txt1.place(x=450, y=130)
anb_txt2 = Entry(anb_base, width="50")
anb_txt2.place(x=450, y=180)
anb_txt3 = Entry(anb_base, width="50")
anb_txt3.place(x=450, y=230)
anb_txt4 = Entry(anb_base, width="50")
anb_txt4.place(x=450, y=280)
anb_bn1 = Button(anb_base, text="Add New Book", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_anb1)
anb_bn1.place(x=270, y=400)
anb_bn2 = Button(anb_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_anb2)
anb_bn2.place(x=550, y=400)


# add new student
class StudentInfo:
    def accept_stud_info(self):
        self.st_enr = str(ans_txt1.get())
        self.st_name = str(ans_txt2.get())
        self.st_email = str(ans_txt3.get())
        self.st_contact = str(ans_txt4.get())
        self.st_class = str(ans_txt5.get())

    def write_st_data_into_file(self):
        fobj = open("stud_info.txt", "a")
        fobj.write(
            self.st_enr + "," + self.st_name + "," + self.st_email + "," + self.st_contact + "," + self.st_class + "\n")
        fobj.close()


def event_add_new_student():
    ib_base.destroy()
    rb_base.destroy()
    anb_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    ans_base.mainloop()


# event for add new student button
def event_ans1():
    s = StudentInfo()
    s.accept_stud_info()
    s.write_st_data_into_file()
    temp = Label(ans_base, text="Student added!!!", bg="blue", foreground="red", font=16)
    temp.place(x=410, y=470)


def event_ans2():
    ans_txt1.delete(0, END)
    ans_txt2.delete(0, END)
    ans_txt3.delete(0, END)
    ans_txt4.delete(0, END)
    ans_txt5.delete(0, END)


# gui for add new student
ans_base = Tk()
ans_base.geometry("950x630+370+20")
ans_base.configure(bg="Blue")
ans_base.title("Frame : Add New Student")
ans_lb1 = Label(ans_base, text="ADD NEW STUDENT", font=("Arial bold", 19))
ans_lb1.place(x=340, y=50)
ans_lb2 = Label(ans_base, text="Enrollment Number", font=40, bg="black", foreground="white")
ans_lb2.place(x=287, y=130)
ans_lb3 = Label(ans_base, text="Student Name", font=40, bg="black", foreground="white")
ans_lb3.place(x=326, y=180)
ans_lb4 = Label(ans_base, text="Student Email", font=40, bg="black", foreground="white")
ans_lb4.place(x=328, y=230)
ans_lb5 = Label(ans_base, text="Student Contact", font=40, bg="black", foreground="white")
ans_lb5.place(x=316, y=280)
ans_lb6 = Label(ans_base, text="Student Class", font=40, bg="black", foreground="white")
ans_lb6.place(x=330, y=330)
ans_txt1 = Entry(ans_base, width="50")
ans_txt1.place(x=450, y=130)
ans_txt2 = Entry(ans_base, width="50")
ans_txt2.place(x=450, y=180)
ans_txt3 = Entry(ans_base, width="50")
ans_txt3.place(x=450, y=230)
ans_txt4 = Entry(ans_base, width="50")
ans_txt4.place(x=450, y=280)
ans_txt5 = Entry(ans_base, width="50")
ans_txt5.place(x=450, y=330)
ans_bn1 = Button(ans_base, text="Add New Student", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_ans1)
ans_bn1.place(x=270, y=400)
ans_bn2 = Button(ans_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_ans2)
ans_bn2.place(x=550, y=400)


# search book
def event_search_book():
    ib_base.destroy()
    rb_base.destroy()
    anb_base.destroy()
    ans_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    sb_base.mainloop()


# event for search button

def search_book_by_book_number():
    bk_no = sb_txt1.get()

    # displaying this book's info searched by book no
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == bk_no:
            sb_s1 = ls[1]
            sb_s2 = ls[2]
            sb_s3 = ls[3]
            sb_lb = Label(sb_base, text="\t\t\t\t\tSearch By Book Number\t\t\t\t\t\t", font=20)
            sb_lb.place(x=0, y=200)
            sb_lb3 = Label(sb_base, text="Book Title :" + sb_s1, font=50, bg="black", foreground="white")
            sb_lb3.place(x=400, y=300)
            sb_lb4 = Label(sb_base, text="Book Author :" + sb_s2, font=50, bg="black", foreground="white")
            sb_lb4.place(x=400, y=350)
            sb_lb5 = Label(sb_base, text="Book Publication :" + sb_s3, font=50, bg="black", foreground="white")
            sb_lb5.place(x=400, y=400)
            sb_btn1.destroy()
            sb_btn2.destroy()
            sb_btn3.destroy()
            sb_btn4.destroy()

    fobj.close()


def search_book_by_book_title():
    bk_title = sb_txt1.get()

    # displaying this book's info searched by book title
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[1] == bk_title:
            sb_s1 = ls[0]
            sb_s2 = ls[2]
            sb_s3 = ls[3]
            sb_lb = Label(sb_base, text="\t\t\t\t\tSearch By Book Title\t\t\t\t\t\t", font=20)
            sb_lb.place(x=0, y=200)
            sb_lb3 = Label(sb_base, text="Book Number :" + sb_s1, font=50, bg="black", foreground="white")
            sb_lb3.place(x=400, y=300)
            sb_lb4 = Label(sb_base, text="Book Author :" + sb_s2, font=50, bg="black", foreground="white")
            sb_lb4.place(x=400, y=350)
            sb_lb5 = Label(sb_base, text="Book Publication :" + sb_s3, font=50, bg="black", foreground="white")
            sb_lb5.place(x=400, y=400)
            sb_btn1.destroy()
            sb_btn2.destroy()
            sb_btn3.destroy()
            sb_btn4.destroy()
            break
    fobj.close()


def search_book_by_book_author():
    bk_author = sb_txt1.get()

    # displaying this book's info searched by book author
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[2] == bk_author:
            sb_s1 = ls[0]
            sb_s2 = ls[1]
            sb_s3 = ls[3]
            sb_lb = Label(sb_base, text="\t\t\t\t\tSearch By Book Title\t\t\t\t\t\t", font=20)
            sb_lb.place(x=0, y=200)
            sb_lb3 = Label(sb_base, text="Book Number :" + sb_s1, font=50, bg="black", foreground="white")
            sb_lb3.place(x=400, y=300)
            sb_lb4 = Label(sb_base, text="Book Title :" + sb_s2, font=50, bg="black", foreground="white")
            sb_lb4.place(x=400, y=350)
            sb_lb5 = Label(sb_base, text="Book Publication :" + sb_s3, font=50, bg="black", foreground="white")
            sb_lb5.place(x=400, y=400)
            sb_btn1.destroy()
            sb_btn2.destroy()
            sb_btn3.destroy()
            sb_btn4.destroy()
            break
    fobj.close()


def search_book_by_book_publication():
    bk_publi = sb_txt1.get()

    # displaying this book's info searched by book title
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[3] == bk_publi:
            sb_s1 = ls[0]
            sb_s2 = ls[1]
            sb_s3 = ls[2]
            sb_lb = Label(sb_base, text="\t\t\t\t\tSearch By Book Publication\t\t\t\t\t\t", font=20)
            sb_lb.place(x=0, y=200)
            sb_lb3 = Label(sb_base, text="Book Number :" + sb_s1, font=50, bg="black", foreground="white")
            sb_lb3.place(x=400, y=300)
            sb_lb4 = Label(sb_base, text="Book title :" + sb_s2, font=50, bg="black", foreground="white")
            sb_lb4.place(x=400, y=350)
            sb_lb5 = Label(sb_base, text="Book Author :" + sb_s3, font=50, bg="black", foreground="white")
            sb_lb5.place(x=400, y=400)
            sb_btn1.destroy()
            sb_btn2.destroy()
            sb_btn3.destroy()
            sb_btn4.destroy()
            break
    fobj.close()


# gui for search book
sb_base = Tk()
sb_base.geometry("950x630+370+20")
sb_base.configure(bg="Blue")
sb_base.title("Frame : Search Book")
sb_lb1 = Label(sb_base, text="SEARCH BOOK", font=("Arial bold", 19))
sb_lb1.place(x=350, y=50)
sb_lb2 = Label(sb_base, text="Enter Value Here ", font=50, bg="black", foreground="white")
sb_lb2.place(x=300, y=140)
sb_txt1 = Entry(sb_base, width="40")
sb_txt1.place(x=450, y=140)
sb_btn1 = Button(sb_base, text="Search by Book Number", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_book_by_book_number)
sb_btn1.place(x=350, y=200)
sb_btn2 = Button(sb_base, text="Search by Book Title", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_book_by_book_title)
sb_btn2.place(x=350, y=270)
sb_btn3 = Button(sb_base, text="Search by Book Author", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_book_by_book_author)
sb_btn3.place(x=350, y=340)
sb_btn4 = Button(sb_base, text="Search by Book Publication", font=40, bg="Black", foreground="white", height=2,
                 width=30, command=search_book_by_book_publication)
sb_btn4.place(x=350, y=410)


# search student
def event_search_student():
    ib_base.destroy()
    rb_base.destroy()
    anb_base.destroy()
    ans_base.destroy()
    sb_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    ss_base.mainloop()


def search_student_by_enrollment_number():
    s_en_num = ss_txt1.get()

    # displaying this student's info searched by enrollmennt number
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == s_en_num:
            ss_s1 = ls[1]
            ss_s2 = ls[2]
            ss_s3 = ls[3]
            ss_s4 = ls[4]
            ss_lb = Label(ss_base, text="\t\t\t\t\tSearch By Student Enrollment number\t\t\t\t\t\t", font=20)
            ss_lb.place(x=0, y=200)
            ss_lb3 = Label(ss_base, text="student Name :" + ss_s1, font=50, bg="black", foreground="white")
            ss_lb3.place(x=350, y=250)
            ss_lb4 = Label(ss_base, text="Student Email :" + ss_s2, font=50, bg="black", foreground="white")
            ss_lb4.place(x=350, y=300)
            ss_lb5 = Label(ss_base, text="Student Contact :" + ss_s3, font=50, bg="black", foreground="white")
            ss_lb5.place(x=350, y=350)
            ss_lb6 = Label(ss_base, text="Student Class :" + ss_s4, font=50, bg="black", foreground="white")
            ss_lb6.place(x=350, y=400)
            ss_btn1.destroy()
            ss_btn2.destroy()
            ss_btn3.destroy()
            ss_btn4.destroy()
            ss_btn5.destroy()
            break
    fobj.close()


def search_student_by_name():
    s_nm = ss_txt1.get()

    # displaying this student's info searched by student name
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[1] == s_nm:
            ss_s1 = ls[0]
            ss_s2 = ls[2]
            ss_s3 = ls[3]
            ss_s4 = ls[4]
            ss_lb = Label(ss_base, text="\t\t\t\t\tSearch By Student Name\t\t\t\t\t\t", font=20)
            ss_lb.place(x=0, y=200)
            ss_lb3 = Label(ss_base, text="student Enrollment Number :" + ss_s1, font=50, bg="black", foreground="white")
            ss_lb3.place(x=350, y=250)
            ss_lb4 = Label(ss_base, text="Student Email :" + ss_s2, font=50, bg="black", foreground="white")
            ss_lb4.place(x=350, y=300)
            ss_lb5 = Label(ss_base, text="Student Contact :" + ss_s3, font=50, bg="black", foreground="white")
            ss_lb5.place(x=350, y=350)
            ss_lb6 = Label(ss_base, text="Student Class :" + ss_s4, font=50, bg="black", foreground="white")
            ss_lb6.place(x=350, y=400)
            ss_btn1.destroy()
            ss_btn2.destroy()
            ss_btn3.destroy()
            ss_btn4.destroy()
            ss_btn5.destroy()
            break
    fobj.close()


def search_student_by_email():
    s_email = ss_txt1.get()

    # displaying this student's info searched by enrollmennt number
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[2] == s_email:
            ss_s1 = ls[0]
            ss_s2 = ls[1]
            ss_s3 = ls[3]
            ss_s4 = ls[4]
            ss_lb = Label(ss_base, text="\t\t\t\t\tSearch By Student Enrollment number\t\t\t\t\t\t", font=20)
            ss_lb.place(x=0, y=200)
            ss_lb3 = Label(ss_base, text="Student Enrollment Number :" + ss_s1, font=50, bg="black", foreground="white")
            ss_lb3.place(x=350, y=250)
            ss_lb4 = Label(ss_base, text="Student name :" + ss_s2, font=50, bg="black", foreground="white")
            ss_lb4.place(x=350, y=300)
            ss_lb5 = Label(ss_base, text="Student Contact :" + ss_s3, font=50, bg="black", foreground="white")
            ss_lb5.place(x=350, y=350)
            ss_lb6 = Label(ss_base, text="Student Class :" + ss_s4, font=50, bg="black", foreground="white")
            ss_lb6.place(x=350, y=400)
            ss_btn1.destroy()
            ss_btn2.destroy()
            ss_btn3.destroy()
            ss_btn4.destroy()
            ss_btn5.destroy()
            break
    fobj.close()


def search_student_by_contact_number():
    s_contact = ss_txt1.get()

    # displaying this student's info searched by Contact number
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[3] == s_contact:
            ss_s1 = ls[0]
            ss_s2 = ls[1]
            ss_s3 = ls[2]
            ss_s4 = ls[4]
            ss_lb = Label(ss_base, text="\t\t\t\t\tSearch By Student Enrollment number\t\t\t\t\t\t", font=20)
            ss_lb.place(x=0, y=200)
            ss_lb3 = Label(ss_base, text="Student Enrollment Number :" + ss_s1, font=50, bg="black", foreground="white")
            ss_lb3.place(x=350, y=250)
            ss_lb4 = Label(ss_base, text="Student name :" + ss_s2, font=50, bg="black", foreground="white")
            ss_lb4.place(x=350, y=300)
            ss_lb5 = Label(ss_base, text="Student Email :" + ss_s3, font=50, bg="black", foreground="white")
            ss_lb5.place(x=350, y=350)
            ss_lb6 = Label(ss_base, text="Student Class :" + ss_s4, font=50, bg="black", foreground="white")
            ss_lb6.place(x=350, y=400)
            ss_btn1.destroy()
            ss_btn2.destroy()
            ss_btn3.destroy()
            ss_btn4.destroy()
            ss_btn5.destroy()
            break
    fobj.close()


def search_student_by_class():
    s_class = ss_txt1.get()

    # displaying this student's info searched by enrollmennt number
    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[4] == s_class:
            ss_s1 = ls[0]
            ss_s2 = ls[1]
            ss_s3 = ls[2]
            ss_s4 = ls[3]
            ss_lb = Label(ss_base, text="\t\t\t\t\tSearch By Student Enrollment number\t\t\t\t\t\t", font=20)
            ss_lb.place(x=0, y=200)
            ss_lb3 = Label(ss_base, text="Student Enrollment Number :" + ss_s1, font=50, bg="black", foreground="white")
            ss_lb3.place(x=350, y=250)
            ss_lb4 = Label(ss_base, text="Student name :" + ss_s2, font=50, bg="black", foreground="white")
            ss_lb4.place(x=350, y=300)
            ss_lb5 = Label(ss_base, text="Student email :" + ss_s3, font=50, bg="black", foreground="white")
            ss_lb5.place(x=350, y=350)
            ss_lb6 = Label(ss_base, text="Student Contact :" + ss_s4, font=50, bg="black", foreground="white")
            ss_lb6.place(x=350, y=400)
            ss_btn1.destroy()
            ss_btn2.destroy()
            ss_btn3.destroy()
            ss_btn4.destroy()
            ss_btn5.destroy()
            break
    fobj.close()


# gui for search student
ss_base = Tk()
ss_base.geometry("950x630+370+20")
ss_base.configure(bg="Blue")
ss_base.title("Frame : Search Student")
ss_lb1 = Label(ss_base, text="SEARCH STUDENT", font=("Arial bold", 19))
ss_lb1.place(x=350, y=50)
ss_lb2 = Label(ss_base, text="Enter Value Here ", font=50, bg="black", foreground="white")
ss_lb2.place(x=300, y=140)
ss_txt1 = Entry(ss_base, width="40")
ss_txt1.place(x=450, y=140)
ss_btn1 = Button(ss_base, text="Search by Enrollment Number", font=40, bg="Black", foreground="white", height=2,
                 width=30, command=search_student_by_enrollment_number)
ss_btn1.place(x=350, y=200)
ss_btn2 = Button(ss_base, text="Search by Student Name", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_student_by_name)
ss_btn2.place(x=350, y=270)
ss_btn3 = Button(ss_base, text="Search by Email Address", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_student_by_email)
ss_btn3.place(x=350, y=340)
ss_btn4 = Button(ss_base, text="Search by Contact Number", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_student_by_contact_number)
ss_btn4.place(x=350, y=410)
ss_btn5 = Button(ss_base, text="Search by Class", font=40, bg="Black", foreground="white", height=2, width=30,
                 command=search_student_by_class)
ss_btn5.place(x=350, y=480)


# check book history
def event_check_book_history():
    ib_base.destroy()
    rb_base.destroy()
    ans_base.destroy()
    anb_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    csh_base.destroy()
    nrb_base.destroy()
    cbh_base.mainloop()


def event_cbh1():
    # i will open issued_book.txt file and print all the lines containing book number as provided in input
    count = 0
    b_num = cbh_txt1.get()

    # displaying this book's info to verify
    fobj = open("book_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == b_num:
            cbh_bktitle = ls[1]
            cbh_bkauthor = ls[2]
            cbh_bkpublication = ls[3]
            break
    fobj.close()

    # displaying book's history
    fobj = open("issued_books.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == b_num:
            cbh_enr = ls[1]
            cbh_issueddate = ls[2]
            cbh_retureneddate = ls[3]
            count = count + 1

    cbh_lb = Label(cbh_base, text="\t\t\t\t\t\tHISTORY\t\t\t\t\t\t\t\t\t", font=50, bg="white", foreground="black")
    cbh_lb.place(x=0, y=200)

    cbh_lb3 = Label(cbh_base, text="Book Title : " + cbh_bktitle, font=50, bg="black", foreground="white")
    cbh_lb3.place(x=200, y=250)

    cbh_lb4 = Label(cbh_base, text="Book Author : " + cbh_bkauthor, font=50, bg="black", foreground="white")
    cbh_lb4.place(x=200, y=300)

    cbh_lb5 = Label(cbh_base, text="Book Publication : " + cbh_bkpublication, font=50, bg="black", foreground="white")
    cbh_lb5.place(x=200, y=350)

    cbh_lb6 = Label(cbh_base, text="Student enrollment : " + cbh_enr, font=50, bg="black", foreground="white")
    cbh_lb6.place(x=560, y=250)

    cbh_lb7 = Label(cbh_base, text="Issued Date : " + cbh_issueddate, font=50, bg="black", foreground="white")
    cbh_lb7.place(x=560, y=300)

    cbh_lb8 = Label(cbh_base, text="Returned date : " + cbh_retureneddate, font=50, bg="black", foreground="white")
    cbh_lb8.place(x=560, y=350)


def event_cbh2():
    cbh_txt1.delete(0, END)


# gui for check book history
cbh_base = Tk()
cbh_base.geometry("950x630+370+20")
cbh_base.configure(bg="Blue")
cbh_base.title("Frame : Check Book History")
cbh_lb1 = Label(cbh_base, text="CHECK BOOK HISTORY", font=("Arial bold", 19))
cbh_lb1.place(x=350, y=50)
cbh_lb2 = Label(cbh_base, text="Book Number to Print History", font=50, bg="black", foreground="white")
cbh_lb2.place(x=250, y=150)
cbh_txt1 = Entry(cbh_base, width="40")
cbh_txt1.place(x=500, y=150)

cbh_bn1 = Button(cbh_base, text="Print", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_cbh1)
cbh_bn1.place(x=270, y=450)
cbh_bn2 = Button(cbh_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_cbh2)
cbh_bn2.place(x=550, y=450)


# check student history

def event_check_student_history():
    ib_base.destroy()
    rb_base.destroy()
    ans_base.destroy()
    anb_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    nrb_base.destroy()
    csh_base.mainloop()


def event_csh1():
    count = 0
    s_enr = csh_txt1.get()

    fobj = open("stud_info.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[0] == s_enr:
            csh_nm = ls[1]
            csh_email = ls[2]
            csh_contact = ls[3]
            csh_class = ls[4]
            break
    fobj.close()

    # displaying student's history
    fobj = open("issued_books.txt", "r")
    fdata_ls = fobj.readlines()

    for oneline in fdata_ls:
        ls = oneline.split(",")
        if ls[1] == s_enr:
            csh_bknum = ls[0]
            csh_issueddate = ls[2]
            csh_returneddate = ls[3]
            count = count + 1

    csh_lb = Label(csh_base, text="\t\t\t\t\t\tHISTORY\t\t\t\t\t\t\t\t\t", font=50, bg="white", foreground="black")
    csh_lb.place(x=0, y=200)

    csh_lb3 = Label(csh_base, text="Name : " + csh_nm, font=50, bg="black", foreground="white")
    csh_lb3.place(x=150, y=250)

    csh_lb4 = Label(csh_base, text="Email : " + csh_email, font=50, bg="black", foreground="white")
    csh_lb4.place(x=150, y=300)

    csh_lb5 = Label(csh_base, text="Contact : " + csh_contact, font=50, bg="black", foreground="white")
    csh_lb5.place(x=150, y=350)

    csh_lb6 = Label(csh_base, text="Class : " + csh_class, font=50, bg="black", foreground="white")
    csh_lb6.place(x=150, y=400)

    csh_lb7 = Label(csh_base, text="Book Number : " + csh_bknum, font=50, bg="black", foreground="white")
    csh_lb7.place(x=560, y=250)

    csh_lb8 = Label(csh_base, text="Issued Date : " + csh_issueddate, font=50, bg="black", foreground="white")
    csh_lb8.place(x=560, y=300)

    csh_lb9 = Label(csh_base, text="Returned date : " + csh_returneddate, font=50, bg="black", foreground="white")
    csh_lb9.place(x=560, y=350)


def event_csh2():
    csh_txt1.delete(0, END)


# gui for check student history
csh_base = Tk()
csh_base.geometry("950x630+370+20")
csh_base.configure(bg="Blue")
csh_base.title("Frame : Check Student History")
csh_lb1 = Label(csh_base, text="CHECK STUDENT HISTORY", font=("Arial bold", 19))
csh_lb1.place(x=350, y=50)
csh_lb2 = Label(csh_base, text="Student Enrollment Number", font=50, bg="black", foreground="white")
csh_lb2.place(x=250, y=150)
csh_txt1 = Entry(csh_base, width="40")
csh_txt1.place(x=500, y=150)
csh_bn1 = Button(csh_base, text="Print", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_csh1)
csh_bn1.place(x=270, y=450)
csh_bn2 = Button(csh_base, text="Reset", height=2, width=15, bg="black", foreground="white", font=12,
                 command=event_csh2)
csh_bn2.place(x=550, y=450)


# not returned books
def event_not_returned_book():
    ib_base.destroy()
    rb_base.destroy()
    ans_base.destroy()
    anb_base.destroy()
    sb_base.destroy()
    ss_base.destroy()
    cbh_base.destroy()
    csh_base.destroy()
    nrb_base.mainloop()

    # i will open issued_book.txt file and print all the books having return status NO and returned date NOT
    fobj = open("issued_books.txt", "r")
    fdata_ls = fobj.readlines()
    for oneline in fdata_ls:
        if oneline._contains(",NOT,") and oneline.contains_(",NO,"):
            # this is the book which is not returned
            ls = oneline.split(",")
            nrb_bknum = ls[0]
            nrb_stenr = ls[1]
            nrb_issuedate = ls[2]
            nrb_expectedreturneddate = ls[5]
            nrb_lb3 = Label(nrb_base,
                            text=nrb_bknum + "\t\t\t" + nrb_stenr + "\t\t\t" + nrb_issuedate + "\t\t\t" + nrb_expectedreturneddate)
            nrb_lb3.place(x=150, y=210)
    fobj.close()


# gui for not returned books
nrb_base = Tk()
nrb_base.geometry("950x630+370+20")
nrb_base.configure(bg="Blue")
nrb_base.title("Frame : Not Returned Books")
nrb_lb1 = Label(nrb_base, text="NOT RETURNED BOOKS", font=("Arial bold", 19))
nrb_lb1.place(x=350, y=50)
nrb_lb2 = Label(nrb_base, text="Book Number\t\t\tEnrollment number\t\t\tIssued Date\t\t\tExpected Returned Date")
nrb_lb2.place(x=150, y=170)


def event_exit():
    exit(0)


# desktop frame gui
mainbase = Tk()
mainbase.geometry("300x630+20+20")
mainbase.title("Desktop frame")
mainbase.configure(bg="Blue")

lb = Label(mainbase, text="LIBRARY MANAGEMENT SYSTEM", font=("Arial bold", 13))
lb.place(x=13, y=20)

bt1 = Button(mainbase, text="Issue Book", bg="Black", height=2, width=30, foreground="White", command=event_issue_book)
bt1.place(x=35, y=100)

bt2 = Button(mainbase, text="Return Book", bg="Black", height=2, width=30, foreground="White",
             command=event_return_book)
bt2.place(x=35, y=150)

bt3 = Button(mainbase, text="Add new Book", bg="Black", height=2, width=30, foreground="White",
             command=event_add_new_book)
bt3.place(x=35, y=200)

bt4 = Button(mainbase, text="Add New Student", bg="Black", height=2, width=30, foreground="White",
             command=event_add_new_student)
bt4.place(x=35, y=250)

bt5 = Button(mainbase, text="Search Book", bg="Black", height=2, width=30, foreground="White",
             command=event_search_book)
bt5.place(x=35, y=300)

bt6 = Button(mainbase, text="Search Student", bg="Black", height=2, width=30, foreground="White",
             command=event_search_student)
bt6.place(x=35, y=350)

bt7 = Button(mainbase, text="Check Book History", bg="Black", height=2, width=30, foreground="White",
             command=event_check_book_history)
bt7.place(x=35, y=400)

bt8 = Button(mainbase, text="Check Student History", bg="Black", height=2, width=30, foreground="White",
             command=event_check_student_history)
bt8.place(x=35, y=450)

bt9 = Button(mainbase, text="Not Returned Book", bg="Black", height=2, width=30, foreground="White",
             command=event_not_returned_book)
bt9.place(x=35, y=500)

bt10 = Button(mainbase, text="EXIT", bg="Black", height=2, width=20, foreground="White", command=event_exit)
bt10.place(x=65, y=550)

mainbase.mainloop()