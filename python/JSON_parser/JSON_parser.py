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
