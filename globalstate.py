import hyperdiv as hd

#@hd.global_state
#class globalstate():
class globalstate(hd.BaseState):    
    User = hd.Prop(hd.String,"Empty")
    Category = hd.Prop(hd.String,"Empty")

    def getUser(self):
        return self.User
    def getCategory(self):
        return self.Category
 
        
