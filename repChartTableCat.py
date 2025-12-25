import hyperdiv as hd
import itertools
import sqlite3
import numpy as np
import array


#mainrouter = hd.router()
foundIt = True
foundDialog = True
listkeys = []
listvalues = []
listdialog = []

def getCategories(cat):
     catDesc = cat
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     cur.execute("SELECT reqId, reqDesc, ReqPrior from Requirements where reqCatType=?",(cat,))  
     userall =  cur.fetchall()
     con.commit()
     con.close()
     return userall
     return userListAll
def getRequirements():
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     cur.execute("SELECT reqCatType, count(*) from Requirements group by reqCatType")  
     userall =  cur.fetchall()
     con.commit()
     con.close()
     return userall
     #return userListAll


#UserDict, 3,True,"User","primary","bottom",types
def TableReport():
  cats = getRequirements()
  catArrayDesc = []
  catArrayType = []

  for x in range(0,len(cats)):
      catItem = cats[x]
      catArrayDesc.append(catItem[0])
      catArrayType.append(catItem[1])
   
  catTuple = cats[0]
  catLists = np.asarray(cats)


 


  #catLists = array('w',cats[0])
  catType = catLists[:, 1]
  catDesc = catLists[:, 0]

  x=[]
  y=[]
 

      

  axis = {}

  exec_string_bar = "hd.bar_chart("
  for i in range(0,len(catType)):
      exec_string_bar= exec_string_bar+"catType["+str(i)+"],"
  exec_string_bar=exec_string_bar+"labels=("
  for i in range(0,len(catDesc)):
      exec_string_bar= exec_string_bar+"catDesc["+str(i)+"],"
  exec_string_bar=exec_string_bar+"),show_x_tick_labels=False)"    
  
  
  exec_string_pie = "hd.pie_chart(("
  for i in range(0,len(catType)):
      exec_string_pie= exec_string_pie+"catType["+str(i)+"],"
  exec_string_pie=exec_string_pie+"),labels=("
  for i in range(0,len(catDesc)):
      exec_string_pie= exec_string_pie+"catDesc["+str(i)+"],"
  exec_string_pie=exec_string_pie+"),doughnut=False)"    
  with hd.tab_group() as tabs:
      t1 = hd.tab("bar")
      t2 = hd.tab("pie")
      t3 = hd.tab("report")

  if t1.active: 
    exec(exec_string_bar)
  if t2.active:
    exec(exec_string_pie)  
  if t3.active:  
    j=0
    for i in range(0,len(catDesc)):
      with hd.scope(i):
        hd.markdown("### Category: "+catDesc[i])
        catTypeDesc = getCategories(catDesc[i])
        idArray = []
        idDesc = []
        idPrior=[]
        for k in range(0,len(catTypeDesc)):
                      catTypeItem= catTypeDesc[k]                      
                      idArray.append(catTypeItem[0])                    
                      idDesc.append(catTypeItem[1])   
                      idPrior.append(catTypeItem[2]) 
        hd.data_table (dict(Id=(idArray),Description=(idDesc),Prior=(idPrior)))
        

    

