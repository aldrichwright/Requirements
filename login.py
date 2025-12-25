import hyperdiv as hd
import sqlite3
import globalstate

def checkUser(user_name,password):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     sql ="SELECT count(*) from User where UserNo = ? and PassWord=?"
     cur.execute(sql, (user_name,password))  
     x =  cur.fetchone()
     q = x[0]
     print(q)
     con.commit()
     con.close()
     if q == 1:
           return True
     else:
           return False
     
def getUserCat(user_name,password):
     con = sqlite3.connect("requirements.db") 
     cur = con.cursor()  
     sql ="SELECT UserId, UserCat from User where UserNo = ? and PassWord=?"
     cur.execute(sql, (user_name,password))  
     x =  cur.fetchone()
     con.commit()
     con.close()
     return x            


def login():

    hd.markdown("### Login")
    text = hd.text("")
    

    #    )
      
    with hd.form(
                    width=30,
                    padding=2,
                    background_color="gray-50",
                    border_radius="large",
                ) as form:
                    Error = hd.text("")
                    user_name = form.text_input("User Name", required=True)
                    
                    password = form.text_input(
                        "Password", input_type="password", required=True                        
		    )  
                    form.submit_button("Log In", variant="primary")	              
    if form.submitted:
        if checkUser(user_name.value,password.value) == True:
            state = globalstate.globalstate.User=user_name.value
            UserInfo=getUserCat(user_name.value,password.value)
            globalstate.globalstate.Category= UserInfo[1]

            hd.location().go(path="/")
        if checkUser(user_name.value,password.value) == False:
            user_name.placeholder="User/Password Incorrect"    
            password.placeholder="User/Password Incorrect" 
            form.reset()


    #failure_alert.collect = True
    #failure_alert.opened = True


