from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as m
import os
import mysql.connector 
from operator import itemgetter
from pathlib import Path
current_dir = Path(__file__).parent
global UsrnamE;global PassworD;global i
i = 0
j = 1
# ===========================================================================================================
class start:
        def __init__(self,root):
                self.root=root
                self.root.title("Web Based Psychological Assessment")
                self.root.geometry("1300x700+0+0")
                self.root.resizable(False,False)

                # design 1st window of gui here,, something like welcome start here...
                image=Image.open(current_dir / "images" / "basket.png")
                image=image.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc=ImageTk.PhotoImage(image)
                self.bg_inc_img=Label(self.root,image=self.bg_inc).place(x=0,y=0)

                image1=Image.open(current_dir / "images" / "pa.png")
                image1=image1.resize((1200,320), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=50,y=50)

                self.start_btn=Button(self.root,text='Next',font=('Arial',50,'bold'),bd=0,fg='black',bg='gold',command=self.login).place(x=900,y=550,width=350,height=110)
# ===========================================================================================================
# Clearing Screen
        def clr_scr(self):
                for widgets in self.root.winfo_children():
                        widgets.destroy()
# ===========================================================================================================
        def login(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "psyc.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                global UsrnamE;global PassworD;global Incog
                UsrnamE=StringVar();PassworD=StringVar();Incog = StringVar()
                self.p_label=Label(self.root,bg='#6A6B7D',).place(x=700,y=0,width=10,height=700)
                self.p_label=Label(self.root,bg='#6A6B7D',).place(x=680,y=0,width=10,height=700)
                self.p_label=Label(self.root,bg='#C04341',).place(x=690,y=0,width=10,height=700)
                
                # =================creating login frame=============
                self.frame_login=Frame(self.root,bg='gold')
                self.frame_login.place(x=100,y=60,width=540,height=400)
                # ============all about login side  =============
                
                
                self.login_lb=Label(self.frame_login,text='Login',fg='#0832FF',bg='gold',font=('Arial',40,'bold')).place(x=30,y=10,width=200,height=70)

                self.Create=Button(self.frame_login,text='Create Account/ Sign up.',command=self.signup,cursor='hand2',bg='gold',bd=0,font=(12)).place(x=50,y=80)
                
                self.usr=Label(self.frame_login,text='Username',fg='#3A083E',bg='gold',font=('Arial',20,'bold')).place(x=50,y=120)
                self.usr_entry=Entry(self.frame_login,bg='white',textvariable=UsrnamE,font=('Arial',15))
                self.usr_entry.place(x=60,y=160,width=350,height=50)

                self.pas=Label(self.frame_login,text='Password',fg='#3A083E',bg='gold',font=('Arial',20,'bold')).place(x=50,y=220)
                self.pas_entry=Entry(self.frame_login,bg='white',textvariable=PassworD,show='*',font=('Arial',15))
                self.pas_entry.place(x=60,y=260,width=350,height=50)

                self.forget=Label(self.frame_login,text='Forget Password/Username?',bg='gold',font=(12)).place(x=50,y=320)

                self.login_btn=Button(self.root,text="Login",cursor='hand2',command=self.check,bd=1,bg='#F71C63',fg='#07004F',font=('Arial',40,'bold')).place(x=100,y=430,height=70,width=240)
                self.login_btn=Label(self.root,text="Or",bd=1,bg='#07004F',fg='#F71C63',font=('Arial',30,'bold')).place(x=340,y=430,height=70,width=60)
                self.login_btn=Button(self.root,text="Signup",cursor='hand2',command=self.signup,bd=1,bg='#3A083E',fg='gold',font=('Arial',35,'bold')).place(x=400,y=430,height=70,width=240)
                # =====================incognito frame===============
                self.frame_inc=Frame(self.root,bg='#C04341')
                self.frame_inc.place(x=750,y=60,width=400,height=400)

                image=Image.open(current_dir / "images" / "p_eye.png")
                image=image.resize((420, 350), Image.Resampling.LANCZOS)
                self.bg_inc=ImageTk.PhotoImage(image)
                self.bg_inc_img=Label(self.frame_inc,image=self.bg_inc).place(x=-5,y=-34)

                self.inc=Label(self.frame_inc,text='                    User                        ',fg='gold',bg='#3A083E',font=('Arial',20,'bold')).place(x=0,y=260)
                self.inc_entry=Entry(self.frame_inc,bg='white',textvariable=Incog,font=('Arial',15)).place(x=0,y=300,width=400,height=50)
                self.cont_btn=Button(self.root,text="Continue Privately",cursor='hand2',command=self.condition,bd=1,bg='#F71C63',fg='#07004F',font=('Arial',30,'bold')).place(x=750,y=415,height=70,width=400)
        def condition(self):
                if Incog.get() == "":
                        m.showerror("Error","Enter any radnom/madeup name.")
                else:
                        self.tests()       
        def check(self):
                conn1 = mysql.connector.connect(host="localhost",username='root',password="Pass@7276",database="akshaydb1")
                cursor1 = conn1.cursor()
                conn2 = mysql.connector.connect(host="localhost",username='root',password="Pass@7276",database="akshaydb1")
                cursor2 = conn2.cursor()
                sqlcmd1="select Username from signup"
                sqlcmd2="select Password from signup"

                cursor1.execute(sqlcmd1)
                cursor2.execute(sqlcmd2)

                user = UsrnamE.get()
                pass1 = PassworD.get()
                u = []; p = []
                for i in cursor1:
                        u.append(i)
                for j in cursor2:
                        p.append(j)
                res=list(map(itemgetter(0),u))
                res1=list(map(itemgetter(0),p))
                k = len(res)
                s = 0
                while s<k:
                        if res[s]==user and res1[s]==pass1:
                                self.tests()
                                m.showinfo("Logged in",f"        Welcome {user}        ")
                                break
                        s += 1
                else:
                        m.showerror("Invalid","Please Enter correct username and password.")
                print(u)
                print(res)
        def signup(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "beach.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                global Usrname;global Password;global agevar;global Profvar;global MobNo;global AdressVar;global GenderVar;global cityVar
                Usrname=StringVar();Password=StringVar();agevar=StringVar();Profvar=StringVar();MobNo=StringVar();AdressVar=StringVar()
                GenderVar=StringVar();cityVar=StringVar()

                self.usrname=Label(self.root,text="  Name : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=80)
                self.usrnameE=Entry(self.root,bg='#F8A95C',textvariable=Usrname,font=(40))
                self.usrnameE.place(x=400,y=80,height=35)

                self.Pass=Label(self.root,text="  Password : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=130)
                self.PassE=Entry(self.root,bg='#F8A95C',show='*',textvariable=Password,font=(40))
                self.PassE.place(x=400,y=130,height=35)
                

                self.Age=Label(self.root,text="  Age : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=180)
                self.AgE=Entry(self.root,bg='#F8A95C',textvariable=agevar,font=(40))
                self.AgE.place(x=400,y=180,width=50,height=35)

                self.Gender=Label(self.root,text="  Gender : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=230)
                self.GendeR=Radiobutton(self.root,text="Male",variable=GenderVar,value="Male",bg='#F8A95C',fg='#48478B',font=(30)).place(x=400,y=230,height=35)
                self.GendeR=Radiobutton(self.root,text="Female",variable=GenderVar,value="Female",bg='#F8A95C',fg='#48478B',font=(30)).place(x=480,y=230,height=35)

                self.Profession=Label(self.root,text="  Profession : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=280)
                self.ProffessioN=Entry(self.root,bg='#F8A95C',textvariable=Profvar,font=(40))
                self.ProffessioN.place(x=400,y=280,height=35)

                self.Mobile_no=Label(self.root,text="  Mobile No. : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=330)
                self.Mobile_nO=Entry(self.root,bg='#F8A95C',textvariable=MobNo,font=(40))
                self.Mobile_nO.place(x=400,y=330,height=35)

                self.city=Label(self.root,text=" City & State : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=380)
                self.citY=Entry(self.root,bg='#F8A95C',textvariable=cityVar,font=(40))
                self.citY.place(x=400,y=380,height=35)

                # back button
                self.b_btn=Button(self.root,text='Back',command=self.login,cursor='hand2',font=('Arial',22,'bold'),fg='black',bg='gold').place(x=30,y=500,width=100,height=50)

                self.submit=Button(self.root,text='Submit',font=('Arial',25,'bold'),bg='gold',command=lambda: [self.signup_check(),self.DB()]).place(x=400,y=500,height=60,width=220)          
        def signup_check(self):
                li=[Usrname.get(),Password.get(),GenderVar.get(),Profvar.get(),MobNo.get(),cityVar.get()]
                try:
                        if type(int(MobNo.get()))!=int:
                                print(type(int(MobNo.get())),int)
                                m.showerror("Error","Enter Mobile No. in Numeric format.")
                except:
                        m.showerror("Error","Enter Mobile No. in Numeric format.")
                try:
                        if type(int(agevar.get()))!=int:
                                print(type(int(agevar.get())),int)
                                m.showerror("Error","Enter Age in Numeric format.")  
                except:
                        m.showerror("Error","Enter Age in Numeric format.")
                if i in li == "":
                        m.showerror("Error","All Fields are Necessary")
                elif len(MobNo.get())!=10:
                        m.showerror("Error","Enter correct Mobile No.")
                
                else:
                        self.login()
        def DB(self):
                if Usrname.get() == "" or Password.get() == "" or agevar.get() == "" or Profvar.get() == "" or MobNo.get() == "":
                        m.showerror("Error","All Fields Required")
                else:
                        conn = mysql.connector.connect(host="localhost",username='root',password="Pass@7276",database="akshaydb1")
                        my_cursor = conn.cursor()
                        my_cursor.execute("insert into signup values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        Usrname.get(),
                                                                                        Password.get(),
                                                                                        agevar.get(),
                                                                                        GenderVar.get(),
                                                                                        Profvar.get(),
                                                                                        MobNo.get(),
                                                                                        cityVar.get()
                                                                                        ))
                        conn.commit()
                        conn.close()     
        def tests(self):
                self.count = 0
                self.clr_scr()
                image=Image.open(current_dir / 'images' / 'sky.png')
                image=image.resize((1300, 700), Image.Resampling.LANCZOS)
                self.bg=ImageTk.PhotoImage(image)
                self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

                # back button
                self.b_btn=Button(self.root,text='Back',command=self.login,cursor='hand2',font=('Arial',22,'bold'),fg='black',bg='gold').place(x=30,y=500,width=100,height=50)

                # TEST 1
                self.test1=Label(self.root,text="Test 1",bg='gold',fg='gray',font=('Arial',20,'bold')).place(x=80,y=50,width=100,height=80)
                self.tesT1=Button(self.root,text="Beck's Depression Inventory",command=self.test_page,cursor='hand2',font=('Arial',20),bg='gray',fg='gold').place(x=200,y=50,width=950,height=80)
                # TEST 2
                self.test1=Label(self.root,text="Test 2",bg='gold',fg='gray',font=('Arial',20,'bold')).place(x=80,y=150,width=100,height=80)
                self.tesT1=Button(self.root,text="The Big Five Personality Test",command=self.test_page2,cursor='hand2',font=('Arial',20),bg='gray',fg='gold').place(x=200,y=150,width=950,height=80)
                # TEST 3
                self.test1=Label(self.root,text="Test 3",bg='gold',fg='gray',font=('Arial',20,'bold')).place(x=80,y=250,width=100,height=80)
                self.tesT1=Button(self.root,text="Locus of Control",command=self.test_page3,cursor='hand2',font=('Arial',20),bg='gray',fg='gold').place(x=200,y=250,width=950,height=80)
        def test_page(self):
                self.clr_scr()
                image=Image.open(current_dir / 'images' / 'black page.png')
                image=image.resize((1300, 700), Image.Resampling.LANCZOS)
                self.bg=ImageTk.PhotoImage(image)
                self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

                self.info=Label(self.root,text="Beck's Depression Inventory",bg='#1C1C1C',fg='white',font=('Arial',40,'bold')).place(x=250,y=40)
                self.info=Label(self.root,text="The Beck Depression Inventory (BDI) is a 21-item, \n self-report rating inventory that measures characteristic \n attitudes and symptoms of depression. \n The BDI has been developed in different forms, \n including several computerized forms, \n a card form, the 13-item short form \n and the more recent BDI-II by Beck, Steer & Brown, 1996. \n The BDI takes approximately 10 minutes \n to complete, although clients require a fifth sixth grade \n reading level to adequately understand the questions.",bg='#C8B7A5',borderwidth=4,fg='#745721',font=('Arial',18,'bold')).place(x=290,y=120)
                self.startbtn=Button(self.root,text='Proceed',cursor='hand2',font=('Arial',22,'bold'),command=self.test_start,bd=0,fg='black',bg='gold').place(x=940,y=500,width=250,height=80)
                # back button
                self.b_btn=Button(self.root,text='Back',command=self.tests,cursor='hand2',font=('Arial',22,'bold'),fg='black',bg='gold').place(x=30,y=500,width=100,height=50)
        def test_page2(self):
                self.clr_scr()
                image=Image.open(current_dir / 'images' / 'black page.png')
                image=image.resize((1300, 700), Image.Resampling.LANCZOS)
                self.bg=ImageTk.PhotoImage(image)
                self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

                self.info=Label(self.root,text="The Big Five Personality Test",bg='#1C1C1C',fg='white',font=('Arial',40,'bold')).place(x=250,y=40)
                self.info=Label(self.root,text="The Big Five personality test measures the five personality factors \n that psychologists have determined are core to our personality \n makeup. The Five Factors of personality are:\n Openness - How open a person is to new ideas and experiences\n Conscientiousness - How goal-directed, persistent, and organized a person is\n Extraversion - How much a person is energized by the outside world\n Agreeableness - How much a person puts others' interests\n  and needs ahead of their own\n Neuroticism - How sensitive a person is to stress and negative emotional triggers\n The Big Five model of personality is widely considered to be the most scientifically \n robust way to describe personality differences. It is the basis \n of most modern personality research.",bg='#C8B7A5',borderwidth=4,fg='#745721',font=('Arial',18,'bold')).place(x=290,y=120)
                self.startbtn=Button(self.root,text='Proceed',cursor='hand2',font=('Arial',22,'bold'),command=self.test_start2,bd=0,fg='black',bg='gold').place(x=940,y=500,width=250,height=80)
                # back button
                self.b_btn=Button(self.root,text='Back',command=self.tests,cursor='hand2',font=('Arial',22,'bold'),fg='black',bg='gold').place(x=30,y=500,width=100,height=50)
        def test_page3(self):
                self.clr_scr()
                image=Image.open(current_dir / 'images' / 'black page.png')
                image=image.resize((1300, 700), Image.Resampling.LANCZOS)
                self.bg=ImageTk.PhotoImage(image)
                self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

                self.info=Label(self.root,text="Locus of Control",bg='#1C1C1C',fg='white',font=('Arial',40,'bold')).place(x=250,y=40)
                self.info=Label(self.root,text="Locus of control is a psychological concept that refers \n to how strongly people believe they have control over \n the situations and experiences that affect their lives. \n In education, locus of control typically refers to how students \n perceive the causes of their academic success or failure in school. \n Students with an “internal locus of control” generally believe that their success or \n failure is a result of the effort and hard work they invest in \n their education. Students with an “external locus of control” generally \n believe that their successes or failures result from external \n factors beyond their control, such as luck, fate, circumstance, injustice, \n bias, or teachers who are unfair, prejudiced, or unskilled. For example, students with \n an internal locus of control might blame poor grades on their \n failure to study, whereas students with an external locus of control \n may blame an unfair teacher or test for their poor performance.",bg='#C8B7A5',borderwidth=4,fg='#745721',font=('Arial',18,'bold')).place(x=250,y=120)
                self.startbtn=Button(self.root,text='Proceed',cursor='hand2',font=('Arial',22,'bold'),command=self.age_gender,bd=0,fg='black',bg='gold').place(x=940,y=560,width=250,height=80)
                # back button
                self.b_btn=Button(self.root,text='Back',command=self.tests,cursor='hand2',font=('Arial',22,'bold'),fg='black',bg='gold').place(x=30,y=500,width=100,height=50)  
        def test_start(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "test_bg.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                myfile = open( current_dir / "project.txt" , "r")
                myline = myfile.readlines()
                self.que=Label(self.root,text='Select the appropriate option based on your current situation.',bg="#636363",fg='white',font=('Arial',20,'bold')).place(x=20,y=20,width=1100,height=80)
                global i
                if i < 84:
                        Button(self.root,text=myline[i],font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Count(0),self.test_start()]).place(x=300,y=200)
                        Button(self.root,text=myline[i+1],font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Count(1),self.test_start()]).place(x=300,y=300)
                        Button(self.root,text=myline[i+2],font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Count(2),self.test_start()]).place(x=300,y=400)
                        Button(self.root,text=myline[i+3],font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Count(3),self.test_start()]).place(x=300,y=500)   
                        i = i + 4
                        print('line no:',i)
                else:
                        self.result()
        def test_start2(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "test_bg.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                myfile = open( current_dir / "project_2.txt" , "r")
                myline = myfile.readlines()
                global i
                if i < 50:
                        self.que=Label(self.root,text=myline[i],bg="#636363",fg='white',font=('Arial',20,'bold')).place(x=20,y=80,width=1100,height=80)
                        Button(self.root,text="Disagree",font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Alter(1),self.test_start2()]).place(x=300,y=200)
                        Button(self.root,text="Slightly Disagree",font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Alter(2),self.test_start2()]).place(x=300,y=300)
                        Button(self.root,text="Neutral",font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Alter(3),self.test_start2()]).place(x=300,y=400)
                        Button(self.root,text="Slightly Agree",font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Alter(4),self.test_start2()]).place(x=300,y=500)   
                        Button(self.root,text="Agree",font=('Arial',15,'bold'),bg="#E6E6E6",command=lambda: [self.Alter(5),self.test_start2()]).place(x=300,y=600)   
                        i = i + 1
                        print('line no:',i)
                else:
                        self.result_2()
        def test_start3(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "test_bg.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                myfile = open( current_dir / "project_3.txt" , "r")
                myline = myfile.readlines()
                global i  
                global j
                if i < 58:
                        li = [0,1,7,8,13,14,18,19,23,24,26]
                        if i in li: 
                                self.que=Label(self.root,text=j,bg="#1D2123",fg="white",font=('Arial',40,'bold')).place(x=30,y=200,width=140,height=151)
                                Button(self.root,text=myline[i],font=('Arial',13,'bold'),bg="#E6E6E6",command=lambda: [self.test_start3()]).place(x=180,y=200)
                                Button(self.root,text=myline[i+1],font=('Arial',13,'bold'),bg="#E6E6E6",command=lambda: [self.test_start3()]).place(x=180,y=300)                
                        else:
                                self.que=Label(self.root,text=j,bg="#1D2123",fg="white",font=('Arial',40,'bold')).place(x=30,y=200,width=140,height=151)
                                h = i
                                Button(self.root,text=myline[h],font=('Arial',13,'bold'),bg="#E6E6E6",command=lambda: [self.Count1(int(h)),self.test_start3()]).place(x=180,y=200)
                                Button(self.root,text=myline[h+1],font=('Arial',13,'bold'),bg="#E6E6E6",command=lambda: [self.Count1(int(h+1)),self.test_start3()]).place(x=180,y=300)      
                        j+=1
                        i += 2             
                else:
                        self.result_3() 
        def age_gender(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "test_bg.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                global GenderVar1;global agevar1
                GenderVar1=StringVar();agevar1=StringVar()
                self.Age=Label(self.root,text="  Age : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=180,height=50,width=200)
                self.AgE=Entry(self.root,bg='#F8A95C',textvariable=agevar1,font=(40))
                self.AgE.place(x=420,y=180,height=50,width=300)

                self.Gender=Label(self.root,text="  Gender : ",font=('Arial',20),fg='#DACDBD',bg='#362A2A').place(x=200,y=320,height=50,width=200)
                self.GendeR=Radiobutton(self.root,text="Male",variable=GenderVar1,value="Male",bg='#F8A95C',fg='#48478B',font=(30)).place(x=420,y=320,height=50)
                self.GendeR=Radiobutton(self.root,text="Female",variable=GenderVar1,value="Female",bg='#F8A95C',fg='#48478B',font=(30)).place(x=500,y=320,height=50)
                self.submit=Button(self.root,text='Submit',font=('Arial',25,'bold'),bg='gold',command=lambda: [self.gender_check()]).place(x=400,y=500,height=60,width=220)          

        def gender_check(self):
                if agevar1.get() == "":
                        m.showerror("error","Enter age.")
                try:
                        if type(int(agevar1.get()))!=int:
                                print(type(int(MobNo.get())),int)
                                m.showerror("Error","Enter Age in Numeric format.")
                except:
                        m.showerror("Error","Enter Age in Numeric format.")
                else:
                        self.test_start3()
        global E,A,C,N,O
        E,A,C,N,O=20,14,14,38,8
        def Alter(self,n): 
                global E,A,C,N,O              
                if i == 0 or i == 10 or i == 20 or i == 30 or i == 40:
                        E+=n
                elif i == 5 or i == 15 or i == 25 or i == 35 or i == 45:
                        E-=n
                if i == 6 or i == 16 or i == 26 or i == 36 or i == 46:
                        A+=n
                elif i == 1 or i == 11 or i == 21 or i == 31 or i == 41:
                        A-=n 
                if i == 2 or i == 12 or i == 22 or i == 32 or i == 42:
                        C+=n
                elif i == 7 or i == 17 or i == 27 or i == 37 or i == 47:
                        C-=n
                if i == 8 or i == 18 or i == 28 or i == 38 or i == 48:
                        N+=n
                elif i == 3 or i == 13 or i == 23 or i == 33 or i == 43:
                        N-=n
                if i == 4 or i == 14 or i == 24 or i == 34 or i == 44:
                        O+=n
                elif i == 9 or i == 19 or i == 29 or i == 39 or i == 49:
                        O-=n
        count = 0
        def Count(self,n):
                self.count += n
        def Count1(self,i):
                li=[2,5,7,9,11,12,16,19,21,23,25,29,31,32,34,38,40,43,44,48,51,52,53,54,55,56]
                if i in li:               
                        self.count += 1                    
        def result(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "dark_beach.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                self.res=Label(self.root,text='Based on your responses, your result is :',font=('Arial',30,'bold')).place(x=80,y=50,width=1100,height=50)
        
                if self.count <= 13:
                        Result = 'Minimal Depression'
                        self.res=Label(self.root,text='Minimal Depression',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)
                elif self.count <= 19:
                        Result = 'Mild Depression'
                        self.res=Label(self.root,text='Mild Depression',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)   
                elif self.count <= 28:
                        Result = 'Moderate Depression'
                        self.res=Label(self.root,text='Moderate Depression',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)
                else:
                        Result = 'Severe Depression'
                        self.res=Label(self.root,text='Severe Depression',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)
                self.startbtn=Button(self.root,text='Tests',cursor='hand2',font=('Arial',42,'bold'),bd=0,fg='black',bg='gold',command=lambda: [self.tests()]).place(x=800,y=420,width=350,height=110)

                conn4 = mysql.connector.connect(host="localhost",username='root',password="Pass@7276",database="akshaydb1")
                my_cursor4 = conn4.cursor()
                if UsrnamE.get()!="":
                        my_cursor4.execute("insert into depression_result values(%s,%s)",(
                                                                        UsrnamE.get(),
                                                                        Result                                      
                                                                ))
                else:
                        my_cursor4.execute("insert into incognito_depression_result values(%s,%s)",(
                                                                        Incog.get(),
                                                                        Result                                      
                                                                ))
                conn4.commit()
                conn4.close()
        def result_2(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "dark_beach.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                self.res=Label(self.root,text='Based on your responses, your result is :',font=('Arial',30,'bold')).place(x=80,y=50,width=1100,height=50)
        
                self.lb=Label(self.root,text='''Extroversion (E) is the personality trait of seeking fulfillment from sources outside the self or
in community. High scorers tend to be very social while low scorers prefer to work on their
projects alone.''',font=('Arial',14,'bold')).place(x=80,y=130,width=900)
                self.lb1=Label(self.root,text=f"Score: {E}",font=('Arial',32,'bold')).place(x=980,y=130,height=72)

                self.lb=Label(self.root,text='''Agreeableness (A) reflects much individuals adjust their behavior to suit others. High scorers
are typically polite and like people. Low scorers tend to 'tell it like it is'.''',font=('Arial',14,'bold')).place(x=80,y=220,width=900,height=72)
                self.lb1=Label(self.root,text=f"Score: {A}",font=('Arial',32,'bold')).place(x=980,y=220,height=72)

                self.lb=Label(self.root,text='''Conscientiousness (C) is the personality trait of being honest and hardworking. High scorers
tend to follow rules and prefer clean homes. Low scorers may be messy and cheat others.''',font=('Arial',14,'bold')).place(x=80,y=310,width=900,height=72)
                self.lb1=Label(self.root,text=f"Score: {C}",font=('Arial',32,'bold')).place(x=980,y=310,height=72)

                self.lb=Label(self.root,text='''Neuroticism (N) is the personality trait of being emotional.''',font=('Arial',14,'bold')).place(x=80,y=400,width=900,height=72)
                self.lb1=Label(self.root,text=f"Score: {N}",font=('Arial',32,'bold')).place(x=980,y=400,height=72)

                self.lb=Label(self.root,text='''Openness to Experience (O) is the personality trait of seeking new experience and intellectual
pursuits. High scores may day dream a lot. Low scorers may be very down to earth.''',font=('Arial',14,'bold')).place(x=80,y=490,width=900,height=72)
                self.lb1=Label(self.root,text=f"Score: {O}",font=('Arial',32,'bold')).place(x=980,y=490,height=72)

                self.startbtn=Button(self.root,text='Tests',cursor='hand2',font=('Arial',42,'bold'),bd=0,fg='black',bg='gold',command=lambda: [self.tests()]).place(x=900,y=570,width=350,height=110)

                conn4 = mysql.connector.connect(host="localhost",username='root',password="Pass@7276",database="akshaydb1")
                my_cursor4 = conn4.cursor()
                if UsrnamE.get()!="":
                        my_cursor4.execute("insert into personality_result values(%s,%s,%s,%s,%s,%s)",(
                                                                                        UsrnamE.get(),
                                                                                        E,
                                                                                        A,
                                                                                        C,
                                                                                        N,
                                                                                        O                                      
                                                                                ))
                else:
                        my_cursor4.execute("insert into incognito_personality_result values(%s,%s,%s,%s,%s,%s)",(
                                                                                                        Incog.get(),
                                                                                                        E,
                                                                                                        A,
                                                                                                        C,
                                                                                                        N,
                                                                                                        O                                        
                                                                                                ))
                conn4.commit()
                conn4.close()
        def result_3(self):
                self.clr_scr()
                image1=Image.open(current_dir / "images" / "dark_beach.jpg")
                image1=image1.resize((1300,700), Image.Resampling.LANCZOS)
                self.bg_inc1=ImageTk.PhotoImage(image1)
                self.bg_inc_img1=Label(self.root,image=self.bg_inc1).place(x=0,y=-5)
                self.res=Label(self.root,text='Based on your responses, your result is :',font=('Arial',30,'bold')).place(x=80,y=50,width=1100,height=50)
                
                if self.count >= 10 and GenderVar1.get()== "Male":
                        Result = 'External Locus of Control'
                        self.res=Label(self.root,text='External Locus of Control',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)
                        self.res=Label(self.root,text="External locus of control is the belief that one's \n behavior will not lead to valued reinforcement that \n is available in the environment and therefore \n not under one's control. The occurrence of reinforcement is \n believed to be a function of factors out of one's \n control such as luck, chance, or randomness.",font=('Arial',20,'bold')).place(x=80,y=250,width=1100,height=300)  
                elif self.count < 10 and GenderVar1.get()== "Male":
                        Result = 'Internal Locus of Control'
                        self.res=Label(self.root,text='Internal Locus of Control',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90) 
                        self.res=Label(self.root,text='People who develop an internal locus of control believe \n that they are responsible for their own success. \n Those with an external locus of control believe \n that external forces, like luck, determine their outcomes.',font=('Arial',20,'bold')).place(x=80,y=250,width=1100,height=300)  
                elif self.count >= 12 and GenderVar1.get()== "Female":
                        Result = 'External Locus of Control'
                        self.res=Label(self.root,text='External Locus of Control',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90)
                        self.res=Label(self.root,text="External locus of control is the belief that one's \n behavior will not lead to valued reinforcement that \n is available in the environment and therefore \n not under one's control. The occurrence of reinforcement is \n believed to be a function of factors out of one's \n control such as luck, chance, or randomness.",font=('Arial',20,'bold')).place(x=80,y=250,width=1100,height=300)  
                elif self.count < 12 and GenderVar1.get()== "Female":
                        Result = 'Internal Locus of Control'
                        self.res=Label(self.root,text='Internal Locus of Control',font=('Arial',60,'bold')).place(x=80,y=120,width=1100,height=90) 
                        self.res=Label(self.root,text='People who develop an internal locus of control believe \n that they are responsible for their own success. \n Those with an external locus of control believe \n that external forces, like luck, determine their outcomes.',font=('Arial',20,'bold')).place(x=80,y=250,width=1100,height=300)  
                conn4 = mysql.connector.connect(host="localhost",username='root',password="SomePass",database="akshaydb1")
                my_cursor4 = conn4.cursor()
                if UsrnamE.get()!="":
                        my_cursor4.execute("insert into LOC_result values(%s,%s)",(
                                                                        UsrnamE.get(),
                                                                        Result                                      
                                                                ))
                else:
                        my_cursor4.execute("insert into incognito_LOC_result values(%s,%s)",(
                                                                        Incog.get(),
                                                                        Result                                      
                                                                ))
                conn4.commit()
                conn4.close()  
# ===========================================================================================================
root=Tk()
obj=start(root)
root.mainloop()
