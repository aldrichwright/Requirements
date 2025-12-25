import hyperdiv as hd
import itertools
import sqlite3
import globalstate

#mainrouter = hd.router()
foundIt = True
foundDialog = True
listkeys = []
listvalues = []
listdialog = []


  
def deleteUser(id):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "DELETE FROM User where UserId = ?"
        cur.execute(sql, (id,))  
     except sqlite3.OperationalError as e:
          print(e) 
     finally:       
        con.commit()
        con.close()

def getUsers():
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     cur.execute("SELECT UserId, UserNo, PassWord,UserCat from User")  
     userall =  cur.fetchall()
     con.commit()
     con.close()
     return userall



def insertUser(UserId, UserNo,PassWord, Category):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "INSERT INTO User VALUES( ?,?,?,?)"
        cur.execute(sql, (UserId, UserNo,PassWord, Category ))  
     except sqlite3.OperationalError as e:
          print(e) 
     finally:       
        con.commit()
        con.close()

def UpdateUser(UserNo,PassWord, UserId):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "Update User  set UserNo=?, Password = ? WHERE UserId = ?"
        cur.execute(sql, (UserNo, PassWord,UserId,))  
     except sqlite3.OperationalError as e:
          print(e) 
     finally:       
        con.commit()
        con.close()

def Editaction(idName):
     Editdialog = hd.dialog("Edit "+ Title)

     merged2 = []


     with Editdialog:
              ErrorArray = []
              ErrorArray.clear()
              merged = listvalues
              index = 0
              index = listvalues[0].index(idName)   

              loop = 0
             
              with hd.form( ) as form:    
                        for i in range(len(listkeys)):
                             with hd.scope(i):                
                                form.text_input(listkeys[i], value=listvalues[i][index] )
                        with hd.hbox(gap=1):
                            form.submit_button(variant="primary")
                            form.reset_button()
                        if form.submitted:  
                            if len(ErrorArray) == 0:   
                                for i in range(len(listkeys)):
                                    with hd.scope(i):               
                                         listvalues[i][index]  = form.form_data[listkeys[i]]                      
                                         datatabledict.update({listkeys[i]:listvalues[i]})   
                                #print(listvalues[0][index])         
                                UpdateUser( listvalues[1][index],listvalues[2][index],listvalues[0][index] )         
                                Editdialog.opened = False
                            else:
                                Editdialog.opened = True 
              
     
     with hd.hbox(padding=0.3, gap=0.3):
        with hd.tooltip(f"Edit {idName}"):
            edit=hd.button(
                prefix_icon="pencil",
                size="small",
                outline=True
            )
        with hd.tooltip(f"Delete {idName}"):
            trash= hd.button(
                prefix_icon="trash",
                size="small",
                outline=True
            )
        if edit.clicked:
            Editdialog.opened = True  
        if trash.clicked:
               index = listvalues[0].index(idName)
               try: 
                 for i in range(len(listkeys)):
                             with hd.scope(i):
                                    del listvalues[i][index]
                                    datatabledict.update({listkeys[i]:listvalues[i] })    
               except:
                   None 

               try:
                  deleteUser(idName)  
                  datatable.next_page()

               except:
                   None  

def TableValidation(value):

     if value == "":
          ErrorArray.append("Error") 
          return "please enter a value"
     

def getMaxUser():
     max_id = 0
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     cur.execute("SELECT max(UserId) FROM User")  
     max_id_list =  cur.fetchone()
     max_id = max_id_list[0]   
     con.commit()
     con.close()
     if max_id is None:
                max_id = 1
     else:
                max_id = max_id + 1       
     return max_id

     



#UserDict, 3,True,"User","primary","bottom",types
def addTable(dict, perpage,action,Subject,addtype,placement,types):
    global dataTypes
    global datatabledict
    datatabledict = dict
    global Title
    Title = Subject
    hd.h3(Title)
    maxid =  getMaxUser()
    listvalues.clear()
    listkeys.clear()
    tempvaluesuser = []
    tempvaluesuserNo = []
    tempvaluespassword = []
    tempvaluesCategory = []
    with hd.button_group():
        hd.button(
                "Pdf",
                variant="primary",
                prefix_icon="file-pdf",
                size="medium",
                outline=True
            )
        hd.button(
                "Word",
                variant="primary",
                prefix_icon="filetype-docx",
                size="medium",
                outline=True
            )
        hd.button(
                "Spreadsheet",
                variant="primary",
                prefix_icon="file-spreadsheet",
                size="medium",
                outline=True
            )
        hd.button(
                "Text File",
                variant="primary",
                prefix_icon="file-earmark-text",
                size="medium",
                outline=True
            )
        
    x= getUsers()

    for rows in x: 
         tempvaluesuser.append(rows [0]) 
         datatabledict.update({"UserId":tempvaluesuser}) 
         tempvaluesuserNo.append(rows [1]) 
         datatabledict.update({"UserNo":tempvaluesuserNo}) 
         tempvaluespassword.append(rows [2]) 
         datatabledict.update({"Password":tempvaluespassword}) 
         tempvaluesCategory.append(rows [3]) 
         datatabledict.update({"Category":tempvaluesCategory}) 
        
    
    for key in datatabledict.keys():
        listkeys.append(key)
    for value in datatabledict.values():    
        listvalues.append(value)
    idName = listkeys[0]
    

    global ErrorArray

    
    global datatable
    dataTypes = types    
    Adddialog = hd.dialog("Add "+ Title) 
    with Adddialog:
              global orgs
              orgs = []          
              ErrorArray = []  
              ErrorArray.clear()
              with hd.form() as form: 
                    hd.text(listkeys[0],background_color="gray-100") 
                    hd.text(maxid)               
                    for i in range(1,len(listkeys)):
                             with hd.scope(i):
                                try:
                                    hd.text(listkeys[i],background_color="gray-100") 
                                    form.text_input(name=listkeys[i],minlength=1,input_type=dataTypes[i], validation=TableValidation )                
                                except:
                                     None    

                    with hd.hbox(gap=1):
                            form.submit_button(variant="primary")
                            form.reset_button()
                    if form.submitted:
                      if len(ErrorArray) == 0:
                            listvalues[0].append(maxid)
                            datatabledict.update({listkeys[0]:listvalues[0]}) 
                            for i in range(1, len(listkeys)):
                                with hd.scope(i):
                                    listvalues[i].append(form.form_data[listkeys[i]])
                                    datatabledict.update({listkeys[i]:listvalues[i]}) 
                            insertUser(maxid,form.form_data[listkeys[1]], form.form_data[listkeys[2]],form.form_data[listkeys[3]])
                            Adddialog.opened = False
                      else:
                         Adddialog.opened = True    

                             
  
     
    Editdialog = hd.dialog("Edit "+ Subject)   
    if placement == "top":
        with hd.button_group():
            with hd.button("add", variant=addtype, outline=True) as addbutton:
                hd.icon("plus", slot=addbutton.prefix)
            with hd.button("cancel", variant=addtype, outline=True) as cancelbutton:
                hd.icon("fullscreen-exit", slot=cancelbutton.prefix)        
        if addbutton.clicked:
            Adddialog.opened = True 
    if action == True:
        try:
            datatable = hd.data_table(datatabledict, rows_per_page =perpage,id_column_name=idName, row_actions = Editaction)
             
        except:
             None    
    else:
        try:
            datatable = hd.data_table(datatabledict, rows_per_page =perpage)
        except:
             None    
    if placement == "bottom":
        with hd.button_group():
            with hd.button("add", variant=addtype, outline=True) as addbutton:
                hd.icon("plus", slot=addbutton.prefix)
            with hd.button("cancel", variant=addtype, outline=True) as cancelbutton:
                hd.icon("fullscreen-exit", slot=cancelbutton.prefix)        
        
        if addbutton.clicked:
            Adddialog.opened = True  
    return dict 