#defining class
class ThisIsProtect:
    #defining both variables
    def __init__(self):
        self._iAmProtected = 0
        self.__superProtected = 7
    def getPrivate(self):
        print(self.__superProtected)

    def setToPrivate(self, private):
        self.__superProtected = private


    
#obtaining lesser protected variable
object = ThisIsProtect()
object._iAmProtected = 5
print(object._iAmProtected)

#obtaining more protected variable
object = ThisIsProtect()
object.getPrivate()
object.setToPrivate(25)
object.getPrivate()
