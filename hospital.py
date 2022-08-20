import datetime
import mysql.connector
import random
db=mysql.connector.connect(host="localhost", user="root", password="", database="hospital")
c=db.cursor()
c.execute("create table if not exists patient(p_id int primary key, p_name text, p_age int, p_gender text, p_contact text, p_bg text) ")
c.execute("create table if not exists family(f_name text, p_id int, f_contact text, f_add text, f_bg text)")

# author :- omkargaikwad1221
while True:
    print("1.Patient Registration\n2.Patient Family Details\n3. Display the patient details\n4. Display fmaily details\n5. Display doctor Details \n6.Display Services\n7.For Checkup\n8.Exit")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        p_id=int(input("Enter Patient ID: "))
        p_name=input("Enter Patient Name: ")
        p_age=int(input("Enter Patient age: "))
        p_gender=input("Enter Gender of Patient[M/F]: ")
        p_contact=input("Enter Patient Contact No.: ")
        print("Blood group:(A+,B+,O+,AB+,A-,B-,O-,AB-)")
        p_bg=input("Enter Blood Group: ")
        

        mysql="insert into patient values(%s,%s,%s,%s,%s,%s)"
        v=(p_id,p_name,p_age,p_gender,p_contact,p_bg)
        c.execute(mysql,v)
        db.commit()
        print("---Data inserted successfully---")
    elif ch==2:
        f_name=input("Enter Family Member Name: ")
        p_id=int(input("Enter Patient id:"))
        f_contact=input("Enter contact No.: ")
        f_add=input("Enter Address: ")
        print("Blood group:(A+,B+,O+,AB+,A-,B-,O-,AB-)")
        f_bg=input("Enter Blood Group: ")
        

        mysql1="insert into family values(%s,%s,%s,%s,%s)"
        v1=(f_name,p_id,f_contact,f_add,f_bg)
        c.execute(mysql1,v1)
        db.commit()
        print("---Data inserted successfully---")
    elif ch==3:
        p_id=int(input("Enter Id to diplay details of patient: "))
        c.execute("select * from patient where p_id=(%s);",(p_id,))
        b=c.fetchall()
        for i in b:
            print("""     Id no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
    elif ch==4:
        print("Search For Patient's Family Details")
        p_id=int(input("Enter Patient id: "))
        c.execute("select * from family where p_id=(%s);",(p_id,))
        b=c.fetchall()
        for i in b:
            print("""     Name:-""",i[0])
            print('''     p_id:-''',i[1])
            print('''     contact number-''',i[2])
            print('''     Address-''',i[3])
            print('''     Blood Group-''',i[4])
    elif ch==5:
        print("Name of Doctors:")
        print("                          ")
        print("\tDr. Varun--> Cardiologist\tDr. Hrithik--> Psychitrist\tDr. Salman--> Cardiologist")
        print("\tDr. Shahrukh--> Neurologist\tDr. Akshay--> Psychitrist\tDr. Amir--> Rheumatologist")
        print("\tDr. Abhishek--> Neurologist\tDr. Ajay--> Psychitrist\tDr. Ranveer--> Cardiologist")
        print("\tDr. John--> Rheumatologist \tDr. Sanjay--> Cardiologist \tDr. Shahid--> Neurologist")

    elif ch==6:
        print("SERVICES:-")
        print("1.X-Ray\n2. MRI\n3. CT Scan\n4. Endoscopy\n5. Dialysis\n6. Ultrasound\n7. EEG\n8. ECG")
        ser=int(input("Enter Service Required: "))
        if ser==1:
            print("Go to Room No. 101")
            print("X-ray charges are 500/-" )
        elif ser==2:
            print("Go to Room No. 102")
            print("MRI charges are 1200/-")
        elif ser==3:    
            print("Go to Room No. 103")
            print("CT Scan charges are 1500/-")
        elif ser==4:
            print("Go to Room No. 201")
            print("Endoscopy charges are 1200/-")
        elif ser==5:
            print("Go to Room No. 202")
            print("Dialysis Charges are 5000/-")
        elif ser==6:
            print("Go to Room No. 203")
            print("Ultrasound charges are 500/-")
        elif ser==7:
            print("Go to Room No. 301")
            print("EEG charges are 800/-")
        elif ser==8:
            print("Go to Room No.303")
            print("ECG charges are 1000/-")
        else:
            print("Invalid")
    elif ch==7:
        while True:
                print('''
          
                           
      SELECT DEPARTMENT:-   
                           
      1.Cardiologist       
      2.Rheumatologist     
      3.Psychitrist        
      4.Neurologist        
      5.Otolaryngonologist 
      6.MI Room            
      7.Back               

                 ''')
                
                x=int(input("Enter choice:-"))
                
                if x==1:
                    i=("Dr. Varun \nRoom no:- 201")
                    j=("Dr. Hrithik \nRoom no:- 202")
                    q=(i,j)
                    h=random.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==2:
                    i=("Dr. Sidharth \nRoom no. 207")
                    j=("Dr. Abhishek \nRoom no. 208")
                    q=(i,j)
                    h=random.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=5))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-",o)
                    break
               
                elif x==3:
                    i=("Dr. Salman \nRoom no. 203")
                    j=("Dr. Shahrukh \nRoom no. 204")
                    q=(i,j)
                    h=random.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==4:
                    i=("Dr. Ajay, \nRoom no. 209")
                    j=("Dr. Ranveer \nRoom no. 200")
                    q=(i,j)
                    h=random.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=6))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==5:
                    i=("Dr. Akshay \nRoom no. 205")
                    j=("Dr. Amir \nRoom no. 206")
                    q=(i,j)
                    h=random.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=4))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-:",o)
                    break
                elif x==6:
                    i=("Dr. Irfan \nRoom no. 001")
                    j=("Dr. John \nRoom no. 002")
                    k=("Dr. Sanjay \nRoom no. 003")
                    l=("Dr. Shahid \nRoom no. 004")
                    q=(i,j,k,l)
                    h=random.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=1))
                    u=(12,43,54,71,32,65)
                    o=random.choice(u)
                    print("Appointment no:-",o)
                    break
                
                elif x==7:
                    break
                else:
                  print("~WRONG OPTION PLEASE ENTER VALID VALUE~")
                  
    elif ch==8:        
        print("you are exit now.")
        break

