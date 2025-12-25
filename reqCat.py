import hyperdiv as hd
import itertools
import sqlite3

#mainrouter = hd.router()
foundIt = True
foundDialog = True
listkeys = []
listvalues = []
listdialog = []


  
def deleteReqCat(id):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "DELETE FROM reqCatType where CatType = ?"
        cur.execute(sql, (id,))  
     except sqlite3.OperationalError as e:
          print(e) 
     finally:       
        con.commit()
        con.close()

def getPriorities():
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     cur.execute("SELECT CatType,CatTypeDesc from reqCatType")  
     userall =  cur.fetchall()
     con.commit()
     con.close()
     return userall



def insertreqCatType(CatType, CatTypeDesc):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "INSERT INTO reqCatType VALUES( ?,?)"
        cur.execute(sql, (CatType, CatTypeDesc ))  
     except sqlite3.OperationalError as e:
          print(e) 
     finally:       
        con.commit()
        con.close()

def UpdatePriority(CatType, CatTypeDesc):

     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()
     try:
        sql = "Update reqCatType  set CatTypeDesc = ? WHERE CatType = ?"
        cur.execute(sql, (CatTypeDesc, CatType,))  
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
                        hd.text(listvalues[0][0])
                        for i in range(1,len(listkeys)):                           
                             with hd.scope(i):                
                                form.text_input(listkeys[i], value=listvalues[i][index] )
                        with hd.hbox(gap=1):
                            form.submit_button(variant="primary")
                            form.reset_button()
                        if form.submitted:  
                            if len(ErrorArray) == 0:   
                                #print(listvalues[0][index]) 
                                for i in range(1,len(listkeys)):
                                    with hd.scope(i):               
                                         listvalues[i][index]  = form.form_data[listkeys[i]]                      
                                         datatabledict.update({listkeys[i]:listvalues[i]})   
                                #print(listvalues[0][index])         
                                UpdatePriority(listvalues[0][index], listvalues[1][index] )         
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
                  deleteReqCat(idName)  
                  datatable.next_page()

               except:
                   None  

def TableValidation(value):

     if value == "":
          ErrorArray.append("Error") 
          return "please enter a value"
     

     




#UserDict, 3,True,"User","primary","bottom",types
def addTable(dict, perpage,action,Subject,addtype,placement,types):
    global dataTypes
    global datatabledict
    global Title
    Title = Subject
    hd.h3(Title)
    datatabledict = dict
    listvalues.clear()
    listkeys.clear()
    tempvaluesCatType = []
    tempvaluesCatTypeDesc = []

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
        
    x= getPriorities()
    for rows in x: 
         tempvaluesCatType.append(rows [0]) 
         datatabledict.update({"CatType":tempvaluesCatType}) 
         tempvaluesCatTypeDesc.append(rows [1]) 
         datatabledict.update({"CatTypeDesc":tempvaluesCatTypeDesc}) 


        
    
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
                    for i in range(0,len(listkeys)):
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
                            datatabledict.update({listkeys[0]:listvalues[0]}) 
                            for i in range(1, len(listkeys)):
                                with hd.scope(i):
                                    listvalues[i].append(form.form_data[listkeys[i]])
                                    datatabledict.update({listkeys[i]:listvalues[i]}) 
                            insertreqCatType(form.form_data[listkeys[0]], form.form_data[listkeys[1]])
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