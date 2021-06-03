import datetime
import collections
import subprocess
import sys


class SupahandsBadger:
    def __init__(self, timestamps=None):
        self.timestamps = timestamps
        if self.timestamps is None:
            self.timestamps = self.generateSeed()
        
    def generateSeed(self):
        # run seed.py to get random timestamps
        result = subprocess.run(['python', "seed.py"], capture_output=True, text=True)

        # O(1) post process output to form timestamps array 
        for char in ['[', ']' , '\n', "'"]:
            result.stdout = result.stdout.replace(char,"")
        print("stdout:",result.stdout.split(','))
        return result.stdout.split(',')

    def getUniqueLoginDates(self, timestamps):
        timestampLoginCountMap = []
        for timestamp in timestamps:
            date = timestamp.strip().split(' ')[0]

            dateStamp = datetime.datetime.strptime(date, "%Y-%m-%d")

            if dateStamp not in timestampLoginCountMap:
                timestampLoginCountMap.append(dateStamp)
        return timestampLoginCountMap

    def calculateConsecutiveLogins(self, sortedLoginDates, loginCountMap):
        consecutiveDatesCountMap = {}
        endDate    = str(sortedLoginDates[0])  
        startDate  = ""
        count      = 1

        for idx in range(len(sortedLoginDates)):
            currentDate = sortedLoginDates[idx]
            expectedPreviousDay = sortedLoginDates[idx] - datetime.timedelta(days=1)

            if idx + 1 < len(sortedLoginDates):
                actualPreviousDay = sortedLoginDates[idx+1]
            else:
                actualPreviousDay = sortedLoginDates[idx]

            print('\ncurrentDate: ',currentDate,'expectedPreviousDay: ',expectedPreviousDay,'startDate: ',startDate,'endDate: ',endDate)
            if actualPreviousDay == expectedPreviousDay:
                count += 1
                print(' matching: ',endDate,startDate,count)
            
            else:
                startDate = str(currentDate)
                print(' NOT matching: ',currentDate,expectedPreviousDay,actualPreviousDay,count)
                timeline = startDate.split(' ')[0] + " - " + endDate.split(' ')[0]
                consecutiveDatesCountMap[timeline] = count
                print(' new input: ','startDate: ',startDate,'endDate: ',endDate,count)

                # reset 
                count = 1
                endDate = str(actualPreviousDay)
                startDate = ""

        # Example:
        # [datetime.datetime(2021, 3, 23, 0, 0), datetime.datetime(2021, 3, 18, 0, 0), datetime.datetime(2021, 3, 17, 0, 0), datetime.datetime(2021, 3, 16, 0, 0), datetime.datetime(2021, 3, 13, 0, 0)]
        # loop1 
        # curr = 2021, 3, 23, prev = 2021, 3, 22, not matching with + 1, new input, count = 1, start = 18
        # curr = 2021, 3, 18, prev = 2021, 3, 17, matching with + 1, count = 2
        # curr = 2021, 3, 17, prev = 2021, 3, 16, matching with + 1, count = 3
        # curr = 2021, 3, 16, prev = 2021, 3, 13, not matching with + 1, new input, count = 1, start = 13
        # if last element start and end and this element              
        
        return consecutiveDatesCountMap

    def sortLogins(self, consecutiveDatesCountMap):
        return dict(sorted(consecutiveDatesCountMap.items(), key=lambda item: item[1],reverse=True))
        # return sortedConsecutiveDatesCountMap

    def displayTable(self, consecutiveLogins):
        print('| START      | END        | LENGTH |', end='\n')
        print('|------------|------------|--------|', end='\n')

        for login in consecutiveLogins.keys():
            endDate, startDate = login.split(' - ')
            length = consecutiveLogins[login]
            print('| {} | {} |      {} |'.format(startDate, endDate, length), end='\n')

    def calculateBadges(self):
        #time complexity: O(n)
        loginCountMap = self.getUniqueLoginDates(self.timestamps)  
        
        #time complexity: O(nlogn)
        sortedLoginDates = sorted(loginCountMap, reverse=True) 

        print('sortedLoginDates: ',sortedLoginDates, end='\n')
        #time complexity: O(n)
        consecutiveDatesCountMap = self.calculateConsecutiveLogins(sortedLoginDates, loginCountMap) 
        print('consecutiveDatesCountMap: ',consecutiveDatesCountMap)
        #time complexity: O(nlogn)
        sortedLoginsMap = self.sortLogins(consecutiveDatesCountMap) 

        #time complexity: O(m)
        self.displayTable(sortedLoginsMap) 

        return sortedLoginsMap

        




# new = SupahandsBadger()
# new.calculateBadges()

# what needs to be done
# convert to date time so we can compare + 1 day 
# when forming dict we form a data time dict that way everything else is easier