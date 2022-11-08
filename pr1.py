import csv
import pandas as pd
while True:
      print('Welcome to this library management program')
      print("  MAIN NENU")
      print("1. Dispay Books")
      print("2. Issue Books")
      print("3. Search Books")
      print("4. Add Books")
      print("5.Return books")
      print("6. Delete Books record")
      print("7. Exit")
      ch=int(input("Enter your choice   "))
           
            
      if ch==1:
           df=pd.read_csv("libdata.csv")
           print("The Books available are:-     ")
           print(df)
           
      elif ch==2:
            r=input("Enter Book name  ")
            n=input("Enter Author's name  ")
            d=input("enter date of issue(DD-MM-YYYY) ")
            t=input("Enter Book code no.: ")
            s=input("Enter Subject  ")
            p=int(input("Enter Price   "))
            df=pd.DataFrame({'Book Name':[r],'Author Name':[n],' date of issue':[d],'Code No':[t],'Subject':[s],'Price':[p]})
            df.loc[len(df.index)]=[r,n,d,t,p,s]
            df.to_csv("libdata.csv",index=False)
            print("Record added sucessfully")
      elif ch==3:
            print("1. Search by Book Name:")
            print("2. Search by Author Name:")
            print("3. Search by Subject:")
            ans=int(input("enter your choice:  "))
            if ans==1:
                  r=input("Enter the name of book which  you want to search: ")
                  df=pd.read_csv("libdata.csv")
                  src=df[df[r]].index
                  print(df.loc[src])
            elif ans==2:
                  n=input("Enter the ename which record you want to search:   ")
                  df=pd.read_csv("lib.csv")
                  src=df[df["ename"]==n].index
                  print(df.loc[src])
            elif ans==3:
                  d=input("Enter the Department which record you want to search:   ")
                  df=pd.read_csv("libdata.csv")
                  src=df[df["Department"]==d].index
                  print(df.loc[src])
                  
      elif ch==4:
            print("1. Modify emp_id")
            print("2. Modify ename")
            print("3. Modify DOJ")
            print("4. Modify DOB")
            print("5. Modify Department")
            print("6. Modify Salary")
            ans=int(input("Enter your choice:   "))
            if ans==1:
                  e=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==e].index
                  e_id=int(input("Enter the new emp_id of the employee:   "))
                  df.loc[chn,"emp_id"]=e_id
                  df.to_csv("lib.csv",index=False)
                  print("emp_id modified sucessfully")
            if ans==2:
                  e=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==e].index
                  ename=input("Enter the new ename of the employee:   ")
                  df.loc[chn,"ename"]=ename
                  df.to_csv("lib.csv",index=False)
                  print("Name modified sucessfully")
            if ans==3:
                  e=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==e].index
                  d=input("Enter the new DOJ of the employee(DD-MM-YY):   ")
                  df.loc[chn,"DOJ"]=d
                  df.to_csv("lib.csv",index=False)
                  print("DOJ modified sucessfully")
            if ans==4:
                  e=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==e].index
                  db=input("Enter the new DOB of the employee(DD-MM-YY):   ")
                  df.loc[chn,"DOB"]=db
                  df.to_csv("lib.csv",index=False)
                  print("DOB modified sucessfully")
            if ans==5:
                  d=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==d].index
                  dt=input("Enter the new department of the employee:   ")
                  df.loc[chn,"Department"]=dt
                  df.to_csv("lib.csv",index=False)
                  print("Department modified sucessfully")
            if ans==6:
                  d=int(input("Enter the emp_id which record you want to modify:   "))
                  df=pd.read_csv("lib.csv")
                  chn=df[df["emp_id"]==d].index
                  s=int(input("Enter the new salary of the employee:   "))
                  df.loc[chn,"Salary"]=s
                  df.to_csv("lib.csv",index=False)
                  print("Salary modified sucessfully")
      elif ch==6:
            D=int(input("Enter the  name of book which  you want to delete:   "))
            df=pd.read_csv("libdata.csv")
            dlt=df[df["Book"]==D].index
            df.drop(dlt,inplace=True)
            df.to_csv("libdata.csv",index=False)
            print("data deleted sucessfully")
               
      elif ch==7:
            print("Thanks.........................visit again")
            break
print(df)

