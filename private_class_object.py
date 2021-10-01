class ThisIsProtect:
    def __init__(self):
        self._iAmProtected = 0
        self.__superProtected = 7

    def getPrivate(self):
        print(self.__superProtected)

    def setToPrivate(self, private):
        self.__superProtected = private


    

object = ThisIsProtect()
object._iAmProtected = 5

#object.__superProtected = 5


print(object._iAmProtected)

object = ThisIsProtect()
object.getPrivate()
object.setToPrivate(25)
object.getPrivate()
