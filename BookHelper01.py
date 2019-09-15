#First, place this text file in a folder, by using it, it will generate 2 text files that must be in the
#same directory for it to function correctly.
#Second, go to https://www.python.org/downloads/ and download the latest version of Python 2.7 (currently 2.7.14)
#After you do this, go back to the file and attempt to run it, it should greet you by asking whether you want to use
#the book helper or annotation helper. If it does this, it means that it worked.
#Right now the annotation section is the most updated, so I would use that, but the book helper has limited functionality too.


#Currently running on Python 2.7.14

import os.path
import os
import datetime
from collections import Counter
###################################################################################################
class AnnotationHelper():
    def enterAnnotationInfo(self):
        bookName= raw_input("Insert name of book. ")
        chName = raw_input("Insert name of chapter. ")
        page = raw_input("Page of the annotation. ")
        pageLoc = raw_input("Location on the page (top, mtop, mid, mbot, bot). ")
        category = raw_input("Category of the annotation. ")
        annotation = raw_input("Insert annotation. ")
        curDate = datetime.date.today()
        curDate1 = str(curDate).split("-")
        simpCurDate = ""
        for info in curDate1:
            simpCurDate += info
        curTime = datetime.datetime.now().time()
        curTime1 = str(curTime).split(":")
        simpCurTime = curTime1[0] + curTime1[1] + (curTime1[2].split("."))[0]
        infoList = bookName + ";" + chName + ";" + page + ";" + pageLoc + ";" + category + ";" + annotation + ";" + simpCurDate + ";" + simpCurTime
        print ("--------------------------------------------------------------------------------")
        return infoList
 
    def addAnnotation(self, args):
        with open('annotations.txt', 'a') as f:
            f.write(args + "\n")
 
    def loadAnnotation(self, fName):
        with open(fName, 'r') as f:
            content = f.readlines()
            if content != "":
                content = [x.strip() for x in content]
        return content
 
    def displayAnnotation(self, entry):
        print ("Book: " + entry[0])
        print ("Chapter Number: " + entry[1])
        print ("Page: " + entry[2])
        print ("Location on the page: " + entry[3])
        print ("Category: " + entry[4])
        print ("Annotation: " + entry[5])
        print ("--------------------------------------------------------------------------------")
 
    def filterAnnotation(self, content):
        print ("\n" * 100)
        searchBy = raw_input("Search by\n1 - Book\n2 - Chapter\n3 - Range of page "+
        "numbers\n4 - Page location\n5 - Category\n6 - Time of day\n7 - Range of days\n8 - Most recent\n9 - All parameters\n")
        print ("--------------------------------------------------------------------------------")
        allData = []
        matches = []
        index1 = 0
        index2 = 0
        for line in content:
                addition = (line.split(";"))
                allData.append(addition)
        books = []
        chapters = []
        pages = []
        pageLocs = []
        categories = []

        times = []
        days = []
        
        for i in allData:
            isInBooks = 0
            isInChapters = 0
            isInPages = 0
            isInPageLocs = 0
            isInCategories = 0
            isInTimes = 0
            isInDays = 0
            
            for book in books:
                if (book.lower() == (i[0]).lower()):
                    isInBooks += 1
            if isInBooks == 0:
                books.append(allData[index1][0])

            for chapter in chapters:
                if (chapter.lower() == (i[1]).lower()):
                    isInChapters += 1
            if isInChapters == 0:
                chapters.append(allData[index1][1])
            for page in pages:
                if (page == i[2]):
                    isInPages += 1
            if isInPages == 0:
                pages.append(int(allData[index1][2]))

            for pageLoc in pageLocs:
                if (pageLoc.lower() == (i[3]).lower()):
                    isInPageLocs += 1
            if isInPageLocs == 0:
                pageLocs.append(allData[index1][3])
            for category in categories:
                if (category.lower() == (i[4]).lower()):
                    isInCategories += 1
            if isInCategories == 0:
                categories.append(allData[index1][4])
            for time in times:
                if (time == i[7]):
                    isInTimes += 1
            if isInTimes == 0:
                    times.append(allData[index1][7])
            if isInDays == 0:
                days.append(allData[index1][6])
            index1 += 1
        if (searchBy == "1"):
            print("List of books in the database: ")
            print ("\n" * 100)
            for i in books:
                print (i)
            print ("--------------------------------------------------------------------------------")
            searchTerm = raw_input("Search by book: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            newTerms = searchTerm.split(",")
            for i in allData:
                index3 = 0
                for term in newTerms:
                    if ((newTerms[index3]).strip()).lower() == (allData[index2][0]).lower():
                        matches.append(allData[index2])
                    index3 += 1
                index2 += 1
            return matches
        
        if (searchBy == "2"):
            print("List of chapters in the database: ")
            print ("\n" * 100)
            for i in chapters:
                print (i)
            print ("--------------------------------------------------------------------------------")
            searchTerm = raw_input("Search by chapter: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            newTerms = searchTerm.split(",")
            for i in allData:
                index3 = 0
                for term in newTerms:
                    if ((newTerms[index3]).strip()).lower() == (allData[index2][1]).lower():
                        matches.append(allData[index2])
                    index3 += 1
                index2 += 1
            return matches
        
        if (searchBy == "3"):
            print ("\n" * 100)
            print("List of pages in the database: ")
            pages.sort()
            for i in pages:
                print (i)
            print ("--------------------------------------------------------------------------------")
            searchTerm1 = raw_input("Starting page: ")
            searchTerm2 = raw_input("Ending page: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            for i in allData:
                if int(searchTerm1) <= int(allData[index2][2]) <= int(searchTerm2):
                    matches.append(allData[index2])
                index2 += 1
            return matches
        
        if (searchBy == "4"):
            print ("\n" * 100)
            print("List of page locations in the database: ")
            for i in pageLocs:
                print (i)
            print ("--------------------------------------------------------------------------------")
            searchTerm = raw_input("Search by page location: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            newTerms = searchTerm.split(",")
            for i in allData:
                index3 = 0
                for term in newTerms:
                    if ((newTerms[index3]).strip()).lower() == (allData[index2][3]).lower():
                        matches.append(allData[index2])
                    index3 += 1
                index2 += 1
            return matches

        if (searchBy == "5"):
            print ("\n" * 100)
            print("List of categories in the database: ")
            for i in categories:
                print (i)
            print ("--------------------------------------------------------------------------------")
            searchTerm = raw_input("Search by categories: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            newTerms = searchTerm.split(",")
            for i in allData:
                index3 = 0
                for term in newTerms:
                    if ((newTerms[index3]).strip()).lower() == (allData[index2][4]).lower():
                        matches.append(allData[index2])
                    index3 += 1
                index2 += 1
            return matches

        if (searchBy == "6"):
            print ("\n" * 100)
            print("List of times in the database: ")
            for i in times:
                print (i[0:2] + ":" + i[2:4])
            print ("--------------------------------------------------------------------------------")
            searchTerm1 = raw_input("Starting time (in HHMM): ")
            searchTerm2 = raw_input("Ending time (in HHMM): ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            for i in allData:
                if (int(searchTerm1) <= (int((allData[index2][7])[0:4])) <= int(searchTerm2)) or (int(searchTerm1) >= (int((allData[index2][7])[0:4])) >= int(searchTerm2)):
                    matches.append(allData[index2])
                index2 += 1
            return matches

        if (searchBy == "7"):
            print ("\n" * 100)
            annotationDays = dict(Counter(days))
            for i in annotationDays:
                repeatedDays = annotationDays.get(i)
                year = i[0:4]
                month1 = i[4:6]
                day = i[6:8]
                month2 = self.numToMonth(month1)
                entry = ""
                if repeatedDays == 1:
                    entry = "entry"
                else:
                    entry = "entries"
                formatted = month2 + " " + day + ", " + year + ": " + str(repeatedDays) + " " + entry
                print (formatted)
            print ("--------------------------------------------------------------------------------")
            searchTerm = raw_input("1 - View annotations from today.\n2 - View them from yesterday.\n3 - View them "+
            "from the past week.\n4 - View them from the past month.\n5 - View them from the past three months.\n6 - "+
            "View any older than three months ago.\n")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            daysAgo1 = 0
            daysAgo2 = 0
            if (searchTerm == "1"):
                daysAgo1 = 0
            if (searchTerm == "2"):
                daysAgo1 = 1
            if (searchTerm == "3"):
                daysAgo1 = 7
            if (searchTerm == "4"):
                daysAgo1 = 30
            if (searchTerm == "5"):
                daysAgo1 = 90
            if (searchTerm == "6"):
                daysAgo1 = 91
            else:
                pass
            curDate = datetime.date.today()
            curDate1 = str(curDate).split("-")
            simpCurDate = ""
            for info in curDate1:
                simpCurDate += info

            for i in allData:
                if (searchTerm == "1" or searchTerm == "3" or searchTerm == "4" or searchTerm == "5"):
                    if (int(simpCurDate) - daysAgo1 <= int(allData[index2][6])):
                        matches.append(allData[index2])
                    index2 += 1
                if (searchTerm == "2"):
                    if (int(simpCurDate) - daysAgo1 == int(allData[index2][6])):
                        matches.append(allData[index2])
                    index2 += 1
                if (searchTerm == "6"):
                    if (int(simpCurDate) - daysAgo1 >= int(allData[index2][6])):
                        matches.append(allData[index2])
                    index2 += 1
            return matches
        
        if (searchBy == "8"):
            print ("\n" * 100)
            multipleEntries = []
            recentTimes = []
            recentDayIndex = days.index(max(days))
            recentDay = days[recentDayIndex]
            
            for day in days:
                if day == days[recentDayIndex]:
                    multipleEntries.append(index2)
                index2 += 1
            for i in multipleEntries:
                recentTimes.append(allData[i][7])
            recentEntryIndex = times.index(max(recentTimes)) 
            print ("Info from most recent entry\n")
            print ("Date: " + self.dateConversion(allData[recentEntryIndex][6]) +  " " +\
            "at " + allData[recentEntryIndex][7][0:2] + ":" + allData[recentEntryIndex][7][2:4])
            
            matches.append(allData[recentEntryIndex])
            return matches
        if (searchBy == "9"):
            searchTerm = raw_input("Search through all entries: ")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            for i in allData:
                if any((searchTerm).lower() in s for s in (allData[index2])) or any((searchTerm) in s for s in allData[index2]):
                    matches.append(allData[index2])

                index2 += 1
            return matches
        else:
            return matches
    def dateConversion(self, num):
        year = num[0:4]
        month1 = num[4:6]
        day = num[6:8]
        month2 = self.numToMonth(month1)
        formatted = month2 + " " + day + ", " + year
        return formatted
    def numToMonth(self, month1):
        month2 = ""
        if ((month1) == "01"):
            month2 = "January"
        elif ((month1) == "02"):
            month2 = "February"
        elif ((month1) == "03"):
            month2 = "March"
        elif ((month1) == "04"):
            month2 = "April"
        elif ((month1) == "05"):
            month2 = "May"
        elif ((month1) == "06"):
            month2 = "June"
        elif ((month1) == "07"):
            month2 = "July"
        elif ((month1) == "08"):
            month2 = "August"
        elif ((month1) == "09"):
            month2 = "September"
        elif ((month1) == "10"):
            month2 = "October"
        elif ((month1) == "11"):
            month2 = "November"
        elif ((month1) == "12"):
            month2 = "December"
        return month2
    def main(self):
        startVar = 0
        while startVar == 0:
            inputMenu = raw_input("1 - Add an annotation\n2 - View all annotations\n3 - Search with"+
            " parameters\n4 - Exit\n")
            print ("\n" * 100)
            print ("--------------------------------------------------------------------------------")
            self.processUserChoice(inputMenu)
            if inputMenu == "4":
                startVar = 1
    def processUserChoice(self, num):
        if (num == "1"):
            print ("\n" * 100)
            self.addAnnotation(self.enterAnnotationInfo())
        elif (num == "2"):
            print ("\n" * 100)
            content = self.loadAnnotation('annotations.txt')
            for line in content:
                a = line.split(";")
                if a != "":
                    self.displayAnnotation(a)
        elif (num == "3"):
            for entry in (self.filterAnnotation(self.loadAnnotation('annotations.txt'))):
                if entry != "":
                    self.displayAnnotation(entry)
                else:
                    print("Your search did not match any entries.")
        elif (num == "4"):
            print ("Thanks for using the program!")
annotationHelper = AnnotationHelper()
print ("Welcome to BACKER - The all in one Book Tracker app!")
begin = raw_input("Press enter to begin.")
annotationHelper.main()

