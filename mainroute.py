import hyperdiv as hd	
import login 
import reqEntry 
import UserEntry
import reqCat
import reqInit
import reqRisk
import reqRepCat
import reqUserCat
import reqPrior
import globalstate
import repChartTableCat
import repChartTablePrior
import repChartTableInit
import repChartTableRisk
import repChartTableBy
import os
import subprocess
import asyncio




mainrouter = hd.router()

@mainrouter.route("/login")
def mainRoute():
   login.login()


@mainrouter.route("/")
def mainRoute():
  #proc = subprocess.Popen(["python -m http.server"])
   pass

@mainrouter.route("/UserEntry")
def mainroute(): 
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login") 
   print(globalstate.globalstate().getCategory())   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/")         
   UserDict = {"UserId": [],
               "UserNo": [] ,
               "Password": [],
               "Category": [],}
   types = ["number","text","text","text"]
   UserEntry.addTable(UserDict, 3,True,"User","primary","bottom",types)

@mainrouter.route("/ReqUserCat")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"UserCat": [],
               "UserCatDesc": [] ,}
   types = ["text","text"]
   reqUserCat.addTable(UserDict, 3,True,"User Category","primary","bottom",types)   


   
@mainrouter.route("/ReqEntry")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login") 
   print(globalstate.globalstate().getCategory())   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'user':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"ReqId": [],
               "Req Description": [] ,
               "Req Cat Type": [],
               "Req Prior": [],
               "Req Initiative": [],
               "Req Risk": [],
               "Req Date": [],
               "Req By": [],
               }
   types = ["number","text","text","text","text","text","text","text","text"]
   reqEntry.addTable(UserDict, 3,True,"Requirements","primary","bottom",types)   

@mainrouter.route("/ReqCat")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"CatType": [],
               "CatTypeDesc": [], }
   types = ["text","text"]
   reqCat.addTable(UserDict, 3,True,"Category","primary","bottom",types)   

@mainrouter.route("/ReqPrior")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"Priority": [],
               "PriorityDesc": [] ,}
   types = ["text","text"]
   reqPrior.addTable(UserDict, 3,True,"Priority","primary","bottom",types)   

@mainrouter.route("/ReqInit")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"Initiative": [],
               "Init Desc": [] ,}
   types = ["text","text"]
   reqInit.addTable(UserDict, 3,True,"Initiative","primary","bottom",types)   

@mainrouter.route("/ReqRisk")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'admin':
      pass
   else:
      globalstate.globalstate().Category = "Empty"
      hd.location().go("/login") 
   UserDict = {"Risk": [],
               "Risk Desc": [] ,
                        }
   types = ["text","text"]
   reqRisk.addTable(UserDict, 3,True,"Risk","primary","bottom",types)  

@mainrouter.route("/repChartTableCat")
def mainProj():
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'user':
      pass
   else:
      if globalstate.globalstate().getCategory() == 'report' :
         pass
      else:
         if globalstate.globalstate().Category == "Empty":
            hd.location().go("/login") 
   repChartTableCat.TableReport()     

@mainrouter.route("/repChartTablePrior")
def mainProj():
   print(globalstate.globalstate().getCategory())
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'user':
      pass
   else:
      if globalstate.globalstate().getCategory() == 'report' :
         pass
      else:
         if globalstate.globalstate().Category == "Empty":
            hd.location().go("/login") 
   repChartTablePrior.TableReport()  

@mainrouter.route("/repChartTableInit")
def mainProj():
   print(globalstate.globalstate().getCategory())
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'user':
      pass
   else:
      if globalstate.globalstate().getCategory() == 'report' :
         pass
      else:
         if globalstate.globalstate().Category == "Empty":
            hd.location().go("/login") 
   repChartTableInit.TableReport()  


@mainrouter.route("/repChartTableBy")
def mainProj():
   print(globalstate.globalstate().getCategory())
   if globalstate.globalstate().getCategory is None:
      hd.location().go("/login")   
   if globalstate.globalstate().getCategory() == 'Empty':
      hd.location().go("/login") 
   if globalstate.globalstate().getCategory() == 'user':
      pass
   else:
      if globalstate.globalstate().getCategory() == 'report' :
         pass
      else:
         if globalstate.globalstate().Category == "Empty":
            hd.location().go("/login") 
   repChartTableBy.TableReport()