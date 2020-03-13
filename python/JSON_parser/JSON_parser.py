import requests

class ToDo:
    completedtotal = 0
    notcompletedtotal= 0
    completedlist = list()
    notcompletedlist= list()
    def __init__(self, userid):
        self.userid = userid
        self.completedlist = []
        self.notcompletedlist = []
<<<<<<< HEAD
    def printCompletedList(self):
        print("User: "+str(self.userid))
        print("Completed:")
        print(self.completedlist)
        print("\n")
    def printNotCompletedList(self):
        print("User: "+str(self.userid))
        print("Not completed:")
        print(self.notcompletedlist)
        print("\n")
    def printTotalCounts(self):
        print("User: "+str(self.userid))
        print("Completed: "+str(self.completedtotal))
        print("Not completed: "+str(self.notcompletedtotal))
        print("\n")
=======
>>>>>>> Solution commit corrected python tasks

    def getCompletedList(self):
        return self.completedlist
    def getNotCompletedList(self):
        return self.notcompletedlist
    def getCountCompleted(self):
        return self.completedtotal
    def getCountNotCompleted(self):
        return self.notcompletedtotal

def createUsersToDoList(link):
        r = requests.get(link)
        dicts = list(r.json())
        userIDs = set()
        userstodolist = list()

        for item in dicts:
            userIDs.add(item['userId'])
        for id in userIDs:
            userstodolist.append(ToDo(id))
        for item in dicts:
            for userstodo in userstodolist:
                if userstodo.userid == item['userId']:
                    if item['completed']==0:
                        userstodo.notcompletedtotal+=1
                        userstodo.notcompletedlist.append(item)
                    elif item['completed']==1:
                        userstodo.completedtotal+=1
                        userstodo.completedlist.append(item)
        return userstodolist

<<<<<<< HEAD
def getUsersToDoCompletedListByUserId(userstodolist,userId):
    for userstodo in userstodolist:
        if userstodo.userid == userId:
            return userstodo.getCompletedList()

def getUsersToDoNotCompletedListByUserId(userstodolist,userId):
    for userstodo in userstodolist:
        if userstodo.userid == userId:
            return userstodo.getNotCompletedList()

def getCountCompletedByUserId(userstodolist,userId):
    for userstodo in userstodolist:
        if userstodo.userid == userId:
            return userstodo.getCountCompleted()

def getCountNotCompletedByUserId(userstodolist,userId):
    for userstodo in userstodolist:
        if userstodo.userid == userId:
            return userstodo.getCountNotCompleted()

def getCompletedList(link,userId):
    return getUsersToDoCompletedListByUserId(createUsersToDoList(link),userId)

def getNotCompletedList(link,userId):
    return getUsersToDoNotCompletedListByUserId(createUsersToDoList(link),userId)

def getToDoList(link,userId,completed):
    if completed:
        return getCompletedList(link,userId)
    else:
        return getNotCompletedList(link,userId)
=======
def getToDoListByUser(link,userId):
    userstodolist = createUsersToDoList(link)
    for userstodo in userstodolist:
        if userstodo.userid == userId:
            return [userstodo.userid]+userstodo.getCompletedList()+userstodo.getNotCompletedList()

def getToDoList(link):
    resultlist = []
    userstodolist = createUsersToDoList(link)
    for userstodo in userstodolist:
        resultlist+= [getToDoListByUser(link,userstodo.userid)]
    return resultlist

link = 'https://jsonplaceholder.typicode.com/todos'
userId = 2


>>>>>>> Solution commit corrected python tasks


