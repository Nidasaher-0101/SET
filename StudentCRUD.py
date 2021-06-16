from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import cx_Oracle
import os


root=Tk()
root.title("TYCSE Class")
root.geometry("400x400")


con = cx_Oracle.connect('U2018BCGRP12/2425@localhost:1521/XEPDB1')

#create table
'''
CREATE TABLE TYCSE (
	PRN VARCHAR2(10) ,
 	NAME VARCHAR2(20),
 	BATCH VARCHAR2(10),
)'''





#create function to delete a record
def delete():
	con = cx_Oracle.connect('U2018BCGRP12/2425@localhost:1521/XEPDB1')
	c= con.cursor()
	
	# delete a record
	c.execute("DELETE from TYCSE WHERE PRN= :PRN",{'PRN':delete_box.get()})
	if(c.rowcount>0):
		messagebox.showinfo("Delete","Successfully Deleted")
	else:
		messagebox.showerror("Failed","Delete operation Failed / Record doesn't exist!")

	#commit changes
	con.commit()
	#close connection
	con.close()
	


# create submit function
def submit():

	con = cx_Oracle.connect('U2018BCGRP12/2425@localhost:1521/XEPDB1')
	c= con.cursor()
	try:
		#insert into table
		c.execute("INSERT INTO TYCSE values(:PRN,:NAME, :BATCH)",
			{
				'PRN':PRN.get(),
				'NAME':NAME.get(),
				'BATCH':BATCH.get()
			})


		#commit changes
		con.commit()
		#close connection
		con.close()
		messagebox.showinfo("Add details","Details added Successfully")
		#clear the text boxes
		PRN.delete(0, END)
		NAME.delete(0, END)
		BATCH.delete(0, END)
	except:
		messagebox.showerror("Failed","Please Enter details")

#create query function
def query():
	con = cx_Oracle.connect('U2018BCGRP12/2425@localhost:1521/XEPDB1')
	c= con.cursor()
	#insert into table
	c.execute("SELECT * FROM TYCSE")
	records=c.fetchall()
	print(records)

	print_records=''
	for record in records:
		print_records+= str(record[0])+"\t"+ str(record[1]) + "\t" + str(record[2]) + "\n"

		
	if(len(records)!=0):
		query_label= Label(root, text=print_records)
		query_label.grid(row=6, column=0,columnspan=2)
	else:
		messagebox.showinfo("No Records","0 records in list")

	
	#commit changes
	con.commit()
	#close connection
	con.close()


#create text boxes
PRN = Entry(root,width=30)
PRN.grid(row=1,column=1,padx=20, pady=(10,0))
NAME = Entry(root,width=30)
NAME.grid(row=2,column=1,padx=20,pady=(10,0))
BATCH = Entry(root,width=30)
BATCH.grid(row=3,column=1,padx=20,pady=(10,0))
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1,pady=5)


#create text box labels
l=Label(root,text="Welcome To TYCSE",bg="white")
l.grid(row=0,column=0,pady= 14,columnspan=2)
PRN_label=Label(root, text="PRN")
PRN_label.grid(row=1,column=0)
NAME_label = Label(root, text="NAME")
NAME_label.grid(row=2,column=0)
BATCH_label = Label(root, text="BATCH")
BATCH_label.grid(row=3,column=0)
delete_box_label = Label(root, text = "Enter PRN to delete details")
delete_box_label.grid(row=8,column=0,pady=5)

#create submit button
submit_btn= Button(root,text="Add details of student", command=submit, fg="white",bg="black")
submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=130)

#create a query button
query_btn= Button(root, text="Show List of students", command =query,fg="white",bg="black")
query_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=133)

#create a delete button
delete_btn= Button(root, text="Delete details of students", command =delete, fg="white",bg="black")
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=123)


#commit changes
con.commit()
#close connection
con.close()

root.mainloop()