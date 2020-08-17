
class Mammal(object):
    def __init__(self, mammalName):
        #print(mammalName, 'is a warm-blooded animal.')
        self.has_hair = "Yes"
        self.warm_blooded = "Yes"
        self.human_is = "Yes"
    
    def sound(self):
        print("The sound of a mammels make is different.")  
 
    def is_warm_blood(self):
        print(self.warm_blooded)
 
    
Lion = Mammal()


Lion.is_warm_blood()
