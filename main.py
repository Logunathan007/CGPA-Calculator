import sys
from sqlite3 import connect
from pandas import DataFrame,read_sql,Series
from tabulate import tabulate
conn = connect("new.db")
cur = conn.cursor();

class Storage:
    def __init__(self):
        self.gra21 = {}
        self.gra17 = {}
        self.sem1_credit = {}
        self.sem2_credit = {}
        self.sem3_credit = {}
        self.sem4_credit = {}
        self.extra = []
        self.default();   
    def default(self):
##        self.gra21 = {'O':10,'A+':9,'A':8,'B+':7,'B':6,'C':5,'U':0}
##        self.gra17 = {'O':10,'A+':9,'A':8,'B+':7,'B':6,'U':0}
##    def sem_credit(self):

##            
##            cur.execute("create table sem1_credit_points_17 ('HS8151' Integer, 'MA8151' Integer, 'PH8151' Integer, 'CY8151' Integer, 'GE8151' Integer, 'GE8152' Integer, 'GE8161'Integer, 'BS8161' Integer);")
##            cur.execute("create table sem2_credit_points_17 ('HS8251' Integer, 'MA8251' Integer, 'PH8253' Integer, 'BE8254' Integer, 'EC8251' Integer, 'EC8252' Integer, 'EC8261'Integer, 'GE8261' Integer);")
##            cur.execute("create table sem3_credit_points_17 ('MA8352' Integer, 'EC8393' Integer, 'EC8351' Integer, 'EC8352' Integer, 'EC8392' Integer, 'EC8391' Integer, 'EC8381'Integer, 'EC8361' Integer,'HS8381' Integer);")
##            cur.execute("create table sem4_credit_points_17 ('MA8451' Integer, 'EC8452' Integer, 'EC8491' Integer, 'EC8451' Integer, 'EC8453' Integer, 'GE8291' Integer, 'EC8461'Integer, 'EC8462' Integer);")
##            cur.execute("create table sem5_credit_points_17 (EC8501 Integer,EC8553 Integer,EC8552 Integer,EC8551 Integer,EC8562 Integer,EC8561 Integer,EC8563 Integer);");
##            cur.execute("create table sem6_credit_points_17 (EC8691 Integer,EC8095 Integer,EC8652 Integer,MG8591 Integer,EC8651 Integer,EC8681 Integer,EC8661 Integer,EC8611 Integer,HS8581 Integer);");
##            cur.execute("create table sem7_credit_points_17 (EC8701 Integer,EC8751 Integer,EC8791 Integer,EC8702 Integer,EC8711 Integer,EC8761 Integer);")
##            cur.execute("create table sem8_credit_points_17 (EC8811 Integer)");
##
##            cur.execute("insert into sem1_credit_points_17 values (4, 4, 3, 3, 3, 4, 2, 2);")
##            cur.execute("insert into sem2_credit_points_17 values (4, 4, 3, 3, 4, 3, 2, 2);")
##            cur.execute("insert into sem3_credit_points_17 values (4, 3, 3, 4, 3, 3, 2, 2, 1);")
##            cur.execute("insert into sem4_credit_points_17 values (4, 3, 3, 4, 3, 3, 2, 2);")
##            cur.execute("insert into sem5_credit_points_17 values(3,4,3,3,2,2,2);")
##            cur.execute("insert into sem6_credit_points_17 values(3,3,3,3,3,2,2,1,1);")
##            cur.execute("insert into sem7_credit_points_17 values(3,3,3,3,2,2);")
##            cur.execute("insert into sem8_credit_points_17 values(10);")
##                    
##            cur.execute("create table sem1_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,'HS8151' varchar, 'MA8151' varchar, 'PH8151' varchar, 'CY8151' varchar, 'GE8151' varchar, 'GE8152' varchar, 'GE8161'varchar, 'BS8161' varchar);")
##            cur.execute("create table sem2_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,'HS8251' varchar, 'MA8251' varchar, 'PH8253' varchar, 'BE8254' varchar, 'EC8251' varchar, 'EC8252' varchar, 'EC8261'varchar, 'GE8261' varchar);")
##            cur.execute("create table sem3_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,'MA8352' varchar, 'EC8393' varchar, 'EC8351' varchar, 'EC8352' varchar, 'EC8392' varchar, 'EC8391' varchar, 'EC8381'varchar, 'EC8361' varchar,'HS8381' varchar);")
##            cur.execute("create table sem4_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,'MA8451' varchar, 'EC8452' varchar, 'EC8491' varchar, 'EC8451' varchar, 'EC8453' varchar, 'GE8291' varchar, 'EC8461'varchar, 'EC8462' varchar);")
##            cur.execute("create table sem5_credits_17(Sem varchar(20),Regno varchar(20) primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8501 varchar(20),EC8553 varchar(20),EC8552 varchar(20),EC8551 varchar(20),EC8562 varchar(20),EC8561 varchar(20),EC8563 varchar(20));")
##            cur.execute("create table sem6_credits_17(Sem varchar(20),Regno varchar(20) primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8691 varchar(20),EC8095 varchar(20),EC8652 varchar(20),MG8591 varchar(20),EC8651 varchar(20),EC8681 varchar(20),EC8661 varchar(20),EC8611 varchar(20),HS8581 varchar(20));")
##            cur.execute("create table sem7_credits_17(Sem varchar(20),Regno varchar(20) primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8701 varchar(20),EC8751 varchar(20),EC8791 varchar(20),EC8702 varchar(20),EC8711 varchar(20),EC8761 varchar(20));")
##            cur.execute("create table sem8_credits_17(Sem varchar(20),Regno varchar(20) primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8811 varchar(20));")
##    
##            conn.commit()
##        res = cur.execute("select * from default_credit_17")
##        val = res.fetchall()
##        col = res.description
##        for i in range(len(col)):
##            self.gra17[col[i][0]] = val[0][i]

        res = cur.execute("select tbl_name from sqlite_master where type='table'")
        if(res.fetchall() == []):
            cur.execute("create table default_credit_17('O' Integer,'A+' Integer,'A' Integer, 'B+' Integer,'B' Integer ,'U' Integer)")
            cur.execute("insert into default_credit_17 values (10, 9, 8, 7, 6, 0);")

            cur.execute("create table default_credit_21('O' Integer,'A+' Integer,'A' Integer, 'B+' Integer,'B' Integer ,'C' Integer, 'U' Integer)")
            cur.execute("insert into default_credit_21 values (10, 9, 8, 7, 6, 5, 0);")

            cur.execute("create table sem1_credit_points_17 (CY8151 integer, GE8151 integer, GE8152 integer, HS8151 integer, MA8151 integer, PH8151 Integer, BS8161 Integer, GE8161 Integer)")
            cur.execute("insert into sem1_credit_points_17 values (3,3,4,4,4,3,2,2)")
            cur.execute("create table sem2_credit_points_17 (BE8254 integer, EC8251 integer, EC8252 integer, HS8251 integer, MA8251 integer, PH8253 Integer, EC8261 Integer, GE8261 Integer)")
            cur.execute("insert into sem2_credit_points_17 values (3,4,3,4,4,3,2,2)");
            cur.execute("create table sem3_credit_points_17 (EC8391 integer, HS8381 integer, MA8352 integer, EC8381 integer, EC8351 integer, EC8352 Integer, EC8392 Integer, EC8393 Integer, EC8361 Ineteger)")
            cur.execute("insert into sem3_credit_points_17 values (3,1,4,2,3,4,3,3,2)");
            cur.execute("create table sem4_credit_points_17 (EC8453 integer, EC8452 integer, GE8291 integer, EC8461 integer, EC8491 integer, MA8451 Integer, EC8451 Integer, EC8462 Integer)")
            cur.execute("insert into sem4_credit_points_17 values (3,3,3,2,3,4,4,2)");
            cur.execute("create table sem5_credit_points_17 (EC8553 integer, EC8551 integer, EC8501 integer, EC8563 integer, EC8561 integer, EC8552 Integer, EC8562 Integer)")
            cur.execute("insert into sem5_credit_points_17 values (4,3,3,2,2,3,2)");
            cur.execute("create table sem6_credit_points_17 (EC8681 integer, HS8581 integer, EC8611 integer, EC8651 integer, EC8095 integer, EC8652 Integer, MG8591 Integer, EC8661 Integer, EC8691 Integer)")
            cur.execute("insert into sem6_credit_points_17 values (2,1,1,3,3,3,3,2,3)");
            cur.execute("create table sem7_credit_points_17 (EC8701 integer, EC8702 integer, EC8751 integer, EC8791 integer, EC8711 integer, EC8761 Integer)")
            cur.execute("insert into sem7_credit_points_17 values (3,3,3,3,2,2)");            
            cur.execute("create table sem8_credit_points_17 (EC8811 Integer)")
            cur.execute("insert into sem8_credit_points_17 values (10)");

            cur.execute("create table sem1_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,CY8151 varchar(2), GE8151 varchar(2), GE8152 varchar(2), HS8151 varchar(2), MA8151 varchar(2), PH8151 varchar(2), BS8161 varchar(2), GE8161 varchar(2))")
            cur.execute("create table sem2_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,BE8254 varchar(2), EC8251 varchar(2), EC8252 varchar(2), HS8251 varchar(2), MA8251 varchar(2), PH8253 varchar(2), EC8261 varchar(2), GE8261 varchar(2))")
            cur.execute("create table sem3_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8391 varchar(2), HS8381 varchar(2), MA8352 varchar(2), EC8381 varchar(2), EC8351 varchar(2), EC8352 varchar(2), EC8392 varchar(2), EC8393 varchar(2), EC8361 varchar(2))")
            cur.execute("create table sem4_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8453 varchar(2), EC8452 varchar(2), GE8291 varchar(2), EC8461 varchar(2), EC8491 varchar(2), MA8451 varchar(2), EC8451 varchar(2), EC8462 varchar(2))")
            cur.execute("create table sem5_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8553 varchar(2), EC8551 varchar(2), EC8501 varchar(2), EC8563 varchar(2), EC8561 varchar(2), EC8552 varchar(2), EC8562 varchar(2))")
            cur.execute("create table sem6_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8681 varchar(2), HS8581 varchar(2), EC8611 varchar(2), EC8651 varchar(2), EC8095 varchar(2), EC8652 varchar(2), MG8591 varchar(2), EC8661 varchar(2), EC8691 varchar(2))")
            cur.execute("create table sem7_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8701 varchar(2), EC8702 varchar(2), EC8751 varchar(2), EC8791 varchar(2), EC8711 varchar(2), EC8761 varchar(2))")
            cur.execute("create table sem8_credits_17 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,EC8811 varchar(2))")

            cur.execute("create table sem1_credit_points_21 ('BS3171' Integer,'CY3151' Integer,'GE3151' Integer,'GE3171' Integer,'HS3151' Integer,'MA3151' Integer,'PH3151' Integer)")
            cur.execute("insert into sem1_credit_points_21 values (2,3,3,2,3,4,3)")
##            cur.execute("create table sem2_credit_points_21 (checks integer)")
####            cur.execute("insert into sem2_credit_points_17 values (3,4,3,4,4,3,2,2)");
##            cur.execute("create table sem3_credit_points_21 (checks integer)")
####            cur.execute("insert into sem3_credit_points_17 values (3,1,4,2,3,4,3,3,2)");
##            cur.execute("create table sem4_credit_points_21 (checks integer)")
########            cur.execute("insert into sem4_credit_points_17 values (3,3,3,2,3,4,4,2)");
##            cur.execute("create table sem5_credit_points_21 (checks integer)")
####            cur.execute("insert into sem5_credit_points_17 values (4,3,3,2,2,3,2)");
##            cur.execute("create table sem6_credit_points_21 (checks integer)")
####            cur.execute("insert into sem6_credit_points_17 values (2,1,1,3,3,3,3,2,3)");
##            cur.execute("create table sem7_credit_points_21 (checks integer)")
####            cur.execute("insert into sem7_credit_points_17 values (3,3,3,3,2,2)");            
##            cur.execute("create table sem8_credit_points_21 (checks integer)")
##            cur.execute("insert into sem8_credit_points_17 values (10)");
            
            cur.execute("create table sem1_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar,'BS3171' varchar,'CY3151' varchar,'GE3151' varchar,'GE3171' varchar,'HS3151' varchar,'MA3151' varchar,'PH3151' varchar)");
##            cur.execute("create table sem2_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem3_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem4_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem5_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem6_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem7_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
##            cur.execute("create table sem8_credits_21 ('Sem' varchar,'Regno' varchar primary key,'Total' varchar,'Sum' varchar,'GPA' varchar)");
            
            conn.commit();
        res = cur.execute("select * from default_credit_17")
        val = res.fetchall()
        col = res.description
        for i in range(len(col)):
            self.gra17[col[i][0]] = val[0][i]
        res = cur.execute("select * from default_credit_21")
        val = res.fetchall()
        col = res.description
        for i in range(len(col)):
            self.gra21[col[i][0]] = val[0][i]
                    
        self.extra = ['Sem','Regno','Total','Sum','GPA']
##        self.sem1_credit = {'HS8151':4,'MA8151':4,'PH8151':3,'CY8151':3,'GE8151':3,'GE8152':4,'GE8161':2,'BS8161':2}
##        self.sem2_credit = {'HS8251':4,'MA8251':4,'PH8253':3,'BE8254':3,'EC8251':4,'EC8252':3,'EC8261':2,'GE8261':2}
##        self.sem3_credit = {'MA8352':4,'EC8393':3,'EC8351':3,'EC8352':4,'EC8392':3,'EC8391':3,'EC8381':2,'EC8361':2,'HS8381':1}
##        self.sem4_credit = {'MA8451':4,'EC8452':3,'EC8491':3,'EC8451':4,'EC8453':3,'GE8291':3,'EC8461':2,'EC8462':2}

class display:
    def __init__(self):
        self.regulation = 0;
        self.semester = 0;
        self.gear_val = 0;
        
    def gear(self):
        print("""\n----- Settings ----- \n\n 1)Add New Subject \t2)Remove Subject \t3)Remove Student \t4)Display All Subjects \n\n 5)Display Stored Details \t6)Display Mark Details \t7)Go Back""")
        try:
            self.gear_val = int(input("\nEnter the number : "))
        except ValueError:
            print("\n***** Wrong Input *****")
            self.gear();
        if(self.gear_val == 1):
            se.add_new_sub();
        elif(self.gear_val == 2):
            se.remove_sub();
        elif(self.gear_val == 3):
            se.remove_student();
        elif(self.gear_val == 4):
            se.display_all_sub();
        elif(self.gear_val == 5):
            se.display_all();
            self.gear();
        elif(self.gear_val == 6):
            se.display_mark();
            self.gear();
        elif(self.gear_val == 7):
            dis.paths();
        else:
            print("\n***** Invalid Number *****")
            self.gear();
            
    def Regulation_select(self):
        print("\n----- Choose Regulation ----- \n\n\t1) 2017 \t2) 2021 \t3) Exit")
        try:
            val = int(input("\nEnter the number : "))
            if(val == 3):
                sys.exit();
        except ValueError:
            print("\n***** Wrong Input *****")
            self.Regulation_select();
        if(val == 1):
            print("\n ----- 2017 Regulation -----")
            dis.regulation = 17;
            dis.paths()
        elif(val == 2):
            dis.regulation = 21;
            dis.paths()
        else:
            print("\n***** Wrong Input *****")
            self.Regulation_select();
            
    def semester_select(self):
        print("\n----- Enter the Semester Number ----- \n\n 1,2,3,...,8 \t 9)Go Back")
        try:
            val = int(input("\nEnter the number : "))
        except ValueError:
            val = 100
        if(val == 1):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 2):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 3):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 4):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 5):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 6):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 7):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 8):
            self.semester = val;
            dis.grade_select(val)
            self.semester_select();
        elif(val == 9):
            self.paths();
        else:
            print("\n ***** Wrong Input *****")
            self.semester_select();

    def cgpa_calc(self,name =""):
        if(name == ""):
            print("\n ----- CGPA CALCULATOR ----- ")
            name = input("\n Enter the Roll number or exit:").upper()
            s = 0;
            tot = 0;
            if name == "":
                print("\n ***** Invalid Number *****")
                return;
        if name == "EXIT":
            return;
        else:
            ls = []
            cgpa_total=0
            cgpa_sum=0
            res = cur.execute("select tbl_name from sqlite_master where type = 'table'")
            for i in res.fetchall():
                if(i[0].endswith("credits_"+str(dis.regulation))):
                    ls.append(i[0]);
            for i in ls:
                ans = cur.execute("select Total,Sum,GPA from {} where Regno = '{}'".format(i,name))
                temp = ans.fetchall()
                if(temp != []):
                    cgpa_total += int(temp[0][0])
                    cgpa_sum += int(temp[0][1])
            if(cgpa_total == 0 or cgpa_sum == 0):
                print("\n ***** Roll Number not found *****")
            else:
                print("\n CGPA for "+ name +" is : %.2f" %(cgpa_sum/cgpa_total))
        
    def paths(self):
        print("\n 1)GPA Calculation \t 2)CGPA Calculation \t 3)Settings \n\n 4)Arrear Updation \t 5)Go Back")
        try:
            way = int(input("\n Enter the number: "))
        except ValueError:
            way = 100
        if(way == 1):
            dis.semester_select()
        elif(way == 2):
            self.cgpa_calc("")
            self.paths();
        elif(way == 3):
            dis.gear();
        elif(way == 4):
            self.a_update();
        elif(way == 5):
            self.Regulation_select()
        else:
            print("\n***** Wrong Input *****")
            self.paths();
        
    def grade_select(self,val):
        credit_points = 0
        gra_points = 0
        
        name = input("\n Enter the Roll number (or) exit: ").upper()
        if name == "":
            print("\n***** Invalid Number *****")
            self.grade_select(val);
        elif(name == 'EXIT'):
            self.semester_select();
        else:
            tb_name = "sem{}_credits_{}".format(self.semester,self.regulation);
            temp = cur.execute("Select Regno from {}".format(tb_name))
            fl = True
            for i in temp.fetchall():
                if i[0] == name:
                    fl = False
                    break;
            if(fl):
                res = cur.execute("select * from sem{}_credit_points_{}".format(self.semester,self.regulation))
                value = res.fetchall();
##                print(res.description)
                sc = {}
                for i in range(len(res.description)):
                    sc[res.description[i][0]] = value[0][i];
                print("\n Credit points are :",sc)
                if(self.regulation == 17):
                    gp = st.gra17
                elif(self.regulation == 21):
                    gp = st.gra21
                ls = []
                ls.append(str(self.regulation)+"_SEM_"+str(self.semester))
                ls.append(name);
                val = gp.keys();
                for i in sc.keys():
                    gra = input("\n Enter the Grade for {} : ".format(i))
                    gra = gra.upper().strip()
                    if(gra not in val):
                        print("\n***** Wrong Input *****")
                        self.grade_select(val);
                        return;
                    else:
                        if(gra != 'U'):
                            credit_points += sc[i];
                            gra_points += (gp[gra]*sc[i]);
                        ls.append(gra)
                gpa = (gra_points/credit_points)
                ls.insert(2,gpa)
                ls.insert(2,gra_points)
                ls.insert(2,credit_points)
                ls = tuple(ls)
                cur.execute("insert into {} values {};".format(tb_name,ls))
                conn.commit();
                print("\n\tGPA is : %.3f"%gpa)
                self.cgpa_calc(name);
            else:
                print("\n ----- Name Already Found -----")
                self.grade_select(val);

    def a_update(self):
        print("\n ----- Arrear Updation -----")
        try:
            print("\n 1,2,3,.... 8  9) Go Back ")
            num = int(input("\n Enter the Semester number : "))
        except ValueError:
            print("\n***** Wrong Input *****")
            self.a_update();
        if(num > 9 or num < 1):
            print("\n***** Wrong Input *****")
            self.a_update();            
        elif(num == 9):
            dis.paths();
        else:
            rollno = input("\n Enter the Roll Number (or) exit: ").upper().strip();
            if (rollno != "EXIT"):
                res = cur.execute("select * from sem{}_credits_{} where Regno = '{}'".format(num,dis.regulation,rollno))
            if(rollno == ""):
                print("\n***** Wrong Input *****")
                self.a_update();
            elif(rollno == "EXIT"):
                dis.paths();
            elif(res.fetchall() == []):
                print("\n***** Roll Number Not Found *****")
                self.a_update();
            else:
                self.printer("select * from sem{}_credits_{} where Regno = '{}'".format(num,dis.regulation,rollno))
                name = input("\n Enter the subject code (or) exit: ").upper().strip();
                res = cur.execute("select * from sem{}_credit_points_{}".format(num,dis.regulation));
                ls = []
                for i in res.description:
                    ls.append(i[0])
                if(name == ""):
                    print("\n***** Wrong Input *****")
                    self.a_update();
                elif(name == "EXIT"):
                    dis.paths();
                elif(name not in ls):
                    print("\n *****Subject code not found*****")
                    self.a_update();
                else:
                    res = cur.execute("select * from default_credit_{}".format(dis.regulation))
                    ls = []
                    for i in res.description:
                        ls.append(i[0])
                    gra = input("\n Enter the Grade or exit: ").strip().upper()
                    if(gra not in ls):
                        print("\n***** Wrong Input *****")
                        self.a_update();
                    elif(gra == ""):
                        print("\n***** Wrong Input *****")
                        self.a_update();
                    elif(gra == "EXIT"):
                        dis.paths();                        
                    else:
                        temp = cur.execute("select Total,Sum from sem{0}_credits_{1} where Regno = '{2}'".format(num,dis.regulation,rollno))
                        ls = list(temp.fetchall()[0])
                        tb_name = "sem{}_credits_{}".format(self.semester,self.regulation);
                        res = cur.execute("select * from sem{}_credit_points_{}".format(num,self.regulation))
                        value = res.fetchall();
                        sc = {}
                        tot1 = 0;
                        sum1 = 0;
                        for i in range(len(res.description)):
                            sc[res.description[i][0]] = value[0][i];
                        print(sc)
                        if(dis.regulation == 17):
                            tot1 = int(ls[0])+sc[name]
                            sum1 = int(ls[1])+(st.gra17[gra]*sc[name])
                        elif(dis.regulation == 21):
                            tot1 = int(ls[0]) + st.gra21[gra]
                            sum1 = int(ls[1]) + (st.gra21[gra]*sc[name])
                        cur.execute("update sem{0}_credits_{1} set Total = '{2}',Sum = '{3}',GPA = '{4}',{5}='{6}' where Regno = '{7}'".format(num,dis.regulation,tot1,sum1,(sum1/tot1),name,gra,rollno))
                        conn.commit();
                        self.printer("select * from sem{0}_credits_{1} where Regno = '{2}'".format(num,dis.regulation,rollno))
                        print("\n Successfully Updated...")
                        print("\n After updation GPA is %.2f" %(sum1/tot1))
                        self.cgpa_calc(rollno)
                        self.a_update();    
    
    def printer(self,content):
        dp = read_sql(content,conn);
        print(tabulate(dp,headers = 'keys',tablefmt = 'psql'))

    def print_series(self,ls,no):
        print("\n")
        s = DataFrame(ls)
        print(tabulate(s,tablefmt = 'psql'))
        
class settings:
    def display_all_sub(self):
        print("\n----- Display All Subjects -----")
        print("\n 1,2,3,....8 \t 9)Go Back")
        try:
            sem_no = int(input("\n Enter the number : "))
        except ValueError:
            sem_no = 100
        if(sem_no > 9 or sem_no <= 0):
            print("\n***** Wrong Input *****")
            self.display_all_sub();
        elif(sem_no == 9):
            dis.gear();
        else:
            res = cur.execute("select tbl_name from sqlite_master where type = 'table'")
            for i in res.fetchall():
##                print(i,"sem"+str(sem_no)+"_credits_"+str())
                if(i[0] == "sem"+str(sem_no)+"_credits_"+str(dis.regulation)):
                    ls = []
                    temp = cur.execute("select * from {}".format(i[0]))
                    for j in temp.description:
                        if j[0] not in st.extra:
                            ls.append(j[0])
                    dis.print_series(ls,sem_no);
            self.display_all_sub()
            
    def display_all(self):
        res = cur.execute("select tbl_name from sqlite_master where type = 'table'")
        for i in res.fetchall():
            print("\n\nTable name is "+i[0])
            dis.printer("select * from {}".format(i[0]))
            
    def remove_sub(self):
        print("\n----- Remove option -----")
        print("\n1,2,3,....8 \t 9)Go Back")
        global st;
        try:
            num = int(input("\nEnter the Semester Number : "))
        except ValueError:
            num = 100
        ls = []      
        if(num > 9 or num < 0):
            print("\n***** Wrong Input *****")
            self.remove_sub();
        elif(num == 9):
            dis.gear();
            return;
        else:
            res = cur.execute("select * from sem{}_credit_points_{}".format(num,dis.regulation))
            for i in res.description:
                ls.append(i[0])
            print("\nSubjects are :",ls)
            col_name = input("\n Enter the subject code or exit: ").upper()
            if(col_name == "EXIT"):
                dis.gear();
                return;
            elif(col_name in ls):
                str1 = "sem{}_credit_points_{}".format(num,dis.regulation);
                str2 = "sem{}_credits_{}".format(num,dis.regulation);
                cur.execute("alter table {} drop column '{}'".format(str1,col_name));                
                cur.execute("alter table {} drop column '{}'".format(str2,col_name));
                print("\n----- Subject is deleted -----")
                st = Storage();
                self.remove_sub();
            else:
                print("\n No such subject present in DataBase");
                self.remove_sub();
                
    def add_new_sub(self):
        global st;
        print("\n ----- Enroll new subject -----")
        try:
            print("\n 1,2,3,.... 8  9) Go Back ")
            num = int(input("\n Enter the Semester number : "))
        except ValueError:
            print("\n***** Wrong Input *****")
            self.add_new_sub()
        if(num > 9 or num < 1):
            print("\n***** Wrong Input *****")
            self.add_new_sub()                
        elif(num == 9):
            dis.gear();
        else:
            ls = []
            res = cur.execute("Select * from sem{}_credit_points_{}".format(num,dis.regulation))
            for i in res.description:
                ls.append(i[0])
            print("\n Existing subjects are :",ls)
            name = input("\n Enter the subject code (or) exit: ").upper()
            if(name == ""):
                print("\n***** Wrong Input *****")
                self.add_new_sub();
            elif(name == "EXIT"):
                dis.gear();
            elif(name in ls):
                print("\n *****Subject already Exit*****")
                self.add_new_sub();
            else:
                cs = 0;
                try:
                    print("\n \t 11)Go back")
                    cs = int(input("\n Enter the credit score : "))
                except ValueError:
                    print("\n***** Wrong Input *****")
                    self.add_new_sub();
                if(cs == 11):
                    dis.gear();
                else:
                    cur.execute("alter table sem{0}_credit_points_{1} add '{2}' Integer".format(num,dis.regulation,name))
                    cur.execute("update sem{0}_credit_points_{1} set '{2}' = {3};".format(num,dis.regulation,name,cs))
                    
                    cur.execute("alter table sem{0}_credits_{1} add {2} varchar".format(num,dis.regulation,name));
                    conn.commit();
                    st = Storage();
                    print("\n Stored successfully")
                    dis.printer("select * from sem{0}_credit_points_{1}".format(num,dis.regulation))
                    dis.printer("select * from sem{0}_credits_{1}".format(num,dis.regulation))
                    self.add_new_sub();
                    
    def display_mark(self):
        print("\n ----- Display all mark Details ----- ")
        ls = []
        res = cur.execute("select tbl_name from sqlite_master where type = 'table'")
        for i in res.fetchall():
            if(i[0].endswith("credits_"+str(dis.regulation))):
                ls.append(i[0]);
        name = input("\n Enter the Roll number (or) exit: ").upper()
        if name == "":
            print("\n***** Invalid Number *****")
            self.display_mark(val);
        elif(name == 'EXIT'):
            dis.gear();
        else:
            fl = False;
            for i in ls:
                temp = cur.execute("Select * from {} where Regno = '{}'".format(i,name))
                if(temp.fetchall() != []):
                    dis.printer("select * from {} where Regno = '{}'".format(i,name))
                    fl = True;
            if(not fl):
                print("\n ***** No Data Found *****");
            self.display_mark();

    def remove_student(self):
        print("\n----- Remove Student -----")
        print("\n 1)Remove from all Semester \t2)Remove from particular Semester \t3)Go Back")
        try:
            num = int(input("\n Enter the number : "))
        except ValueError:
            print("\n***** Wrong Input *****")
            self.remove_student()
            return;
        if(num == 1):
            name = input("\n Enter the Roll number (or) exit: ").upper()
            if name == "":
                print("\n***** Invalid Number *****")
                self.remove_student();
            elif(name == 'EXIT'):
                dis.gear();
            else:
                res = cur.execute("select tbl_name from sqlite_master where type = 'table'")
                for i in res.fetchall():
                    if(i[0].endswith("credits_"+str(dis.regulation))):
                        cur.execute("delete from {} where Regno = '{}'".format(i[0],name))
                print("\n Deleted Successfully.... ")
                self.remove_student();
        elif(num == 2):
            try:
                print("\n 1,2,3,.... 8  9) Go Back ")
                num = int(input("\n Enter the Semester number : "))
            except ValueError:
                print("\n***** Wrong Input *****")
                self.remove_student()
                return;
            if(num <= 0 or num >=10):
                print("\n***** Invalid Input *****")
                self.remove_student()
            elif(num == 9):
                dis.gear();
            else:
                name = input("\n Enter the Roll number (or) exit: ").upper()
                if name == "":
                    print("\n***** Invalid Number *****")
                    self.remove_student();
                elif(name == 'EXIT'):
                    dis.gear();
                else:
                    cur.execute("delete from {} where Regno = '{}'".format('sem{}_credits_{}'.format(num,dis.regulation),name))
                    conn.commit();
                    print("\n Deleted Successfully.... ")
            self.remove_student();
        elif(num == 3):
            dis.gear();
        else:
            print("\n***** Wrong Input *****")
            self.remove_student();
        
        
se = settings()
dis = display()
st = Storage()
##print(st.gra17)
##print(st.sem1_credit)
##print(st.sem2_credit)
##print(st.sem3_credit)
##print(st.sem4_credit)

def start():
    dis.Regulation_select()

start();
  
##dis.printer("select * from sem1_credits_17")
##dis.printer("select * from sem2_credits_17")
##dis.printer("select * from sem2_credits_17")
##dis.printer("select * from sem2_credits_17")
