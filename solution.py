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

        # O(n) post process output to form timestamps array 
        for char in ['[', ']' , '\n', "'"]:
            result.stdout = result.stdout.replace(char,"")
        print("stdout:",result.stdout.split(','))
        return result.stdout.split(',')

    def calculateLoginsPerDate(self, timestamps):
        timestampLoginCountMap = {}
        for timestamp in timestamps:
            date = timestamp.strip().split(' ')[0]

            dateStamp = datetime.datetime.strptime(date, "%Y-%m-%d")

            if dateStamp not in timestampLoginCountMap:
                timestampLoginCountMap[dateStamp] = 0
            timestampLoginCountMap[dateStamp] += 1   

        return timestampLoginCountMap

    def calculateConsecutiveLoginDates(self, sortedLoginDates, loginCountMap):
        consecutiveDatesCountMap = {}
        startDate  = str(sortedLoginDates[0])  
        endDate    = ""
        count      = 0

        for idx in range(len(sortedLoginDates)-1):
            currentDate = sortedLoginDates[idx]
            nextDay = currentDate + datetime.timedelta(days=1)
            print(currentDate, nextDay, loginCountMap[currentDate])

            if sortedLoginDates[idx+1] == nextDay:
                count += loginCountMap[currentDate]
            else:
                count += loginCountMap[currentDate]
                endDate = str(sortedLoginDates[idx])
                timeline = startDate.split(' ')[0] + " - " + endDate.split(' ')[0]
                consecutiveDatesCountMap[timeline] = count
                print('new input: ',startDate,endDate,count,'\n')

                # reset 
                count = 0
                startDate  = str(sortedLoginDates[idx+1])
                endDate    = "" 
        return consecutiveDatesCountMap

    def sortLongestPeriodByDescending(self, consecutiveDatesCountMap):
        return dict(sorted(consecutiveDatesCountMap.items(), key=lambda item: item[1],reverse=True))
        # return sortedConsecutiveDatesCountMap

    def displayTable(self, consecutiveLogins):
        print('| START      | END        | LENGTH |', end='\n')
        print('|------------|------------|--------|', end='\n')

        for login in consecutiveLogins.keys():
            startDate, endDate = login.split(' - ')
            length = consecutiveLogins[login]
            print('| {} | {} |      {} |'.format(startDate, endDate, length), end='\n')

    def calculateBadges(self):
        #time complexity: O(n)
        loginCountMap = self.calculateLoginsPerDate(self.timestamps)  
        
        print(loginCountMap)

        #time complexity: O(nlogn)
        sortedLoginDates = sorted(loginCountMap) 

        print(sortedLoginDates)

        #time complexity: O(n)
        consecutiveDatesCountMap = self.calculateConsecutiveLoginDates(sortedLoginDates, loginCountMap) 

        #time complexity: O(nlogn)
        sortLongestPeriodByDescending = self.sortLongestPeriodByDescending(consecutiveDatesCountMap) 

        #time complexity: O(m)
        self.displayTable(sortLongestPeriodByDescending) 

        print(loginCountMap)
        print(sortLongestPeriodByDescending)

        return sortLongestPeriodByDescending

        

        # badgeCountMap = {}
        # badgeCount = 0
        # startDate  = str(sortedLoginDates[0])
        # endDate    = ""
        
        # for idx in range(len(sortedLoginDates)-1):
        #     targetDate = sortedLoginDates[idx]
        #     nextDay = targetDate + datetime.timedelta(days=1)
        #     print(targetDate, nextDay, loginCountMap[targetDate])

        #     if sortedLoginDates[idx+1] == nextDay:
        #         badgeCount += loginCountMap[targetDate]
        #     else:
        #         badgeCount += loginCountMap[targetDate]
        #         endDate = str(sortedLoginDates[idx])
        #         timeline = startDate + "-" + endDate
        #         badgeCountMap[timeline] = badgeCount
        #         print('new input: ',startDate,endDate,badgeCount,'\n')

        #         # reset 
        #         badgeCount = 0
        #         startDate  = str(sortedLoginDates[idx+1])
        #         endDate    = ""                

            
# loop 1 (2021, 6, 2, 0, 0) , next (2021, 6, 3, 0, 0), actual (2021, 6, 4, 0, 0), count 0 -> 2, reset count start and end date run agian


# [datetime.datetime(2021, 6, 2, 0, 0), datetime.datetime(2021, 6, 4, 0, 0), datetime.datetime(2021, 6, 5, 0, 0), datetime.datetime(2021, 6, 7, 0, 0), datetime.datetime(2021, 6, 8, 0, 0), datetime.datetime(2021, 6, 9, 0, 0), datetime.datetime(2021, 6, 11, 0, 0), datetime.datetime(2021, 6, 12, 0, 0), datetime.datetime(2021, 6, 13, 0, 0), datetime.datetime(2021, 6, 14, 0, 0), datetime.datetime(2021, 6, 16, 0, 0), datetime.datetime(2021, 6, 18, 0, 0), datetime.datetime(2021, 6, 19, 0, 0), datetime.datetime(2021, 6, 21, 0, 0), datetime.datetime(2021, 6, 22, 0, 0), datetime.datetime(2021, 6, 23, 0, 0), datetime.datetime(2021, 6, 25, 0, 0), datetime.datetime(2021, 6, 26, 0, 0), datetime.datetime(2021, 6, 27, 0, 0), datetime.datetime(2021, 6, 28, 0, 0), datetime.datetime(2021, 6, 29, 0, 0), datetime.datetime(2021, 7, 1, 0, 0), datetime.datetime(2021, 7, 3, 0, 0), datetime.datetime(2021, 7, 4, 0, 0), datetime.datetime(2021, 7, 5, 0, 0), datetime.datetime(2021, 7, 6, 0, 0), datetime.datetime(2021, 7, 8, 0, 0), datetime.datetime(2021, 7, 9, 0, 0), datetime.datetime(2021, 7, 10, 0, 0), datetime.datetime(2021, 7, 11, 0, 0), datetime.datetime(2021, 7, 13, 0, 0), datetime.datetime(2021, 7, 14, 0, 0), datetime.datetime(2021, 7, 16, 0, 0), datetime.datetime(2021, 7, 17, 0, 0), datetime.datetime(2021, 7, 19, 0, 0), datetime.datetime(2021, 7, 20, 0, 0), datetime.datetime(2021, 7, 23, 0, 0), datetime.datetime(2021, 7, 24, 0, 0), datetime.datetime(2021, 7, 25, 0, 0), datetime.datetime(2021, 7, 26, 0, 0), datetime.datetime(2021, 7, 27, 0, 0), datetime.datetime(2021, 7, 28, 0, 0), datetime.datetime(2021, 7, 29, 0, 0), datetime.datetime(2021, 7, 30, 0, 0), datetime.datetime(2021, 8, 1, 0, 0)]

# new = SupahandsBadger()
# new.calculateBadges()


# ['2021-07-30 05:24:44', ' 2021-07-25 16:24:44', ' 2021-06-15 16:24:44', ' 2021-06-11 05:24:44', ' 2021-07-11 10:24:44', ' 2021-06-06 21:24:44', ' 2021-06-08 05:24:44', ' 2021-07-16 23:24:44', ' 2021-06-22 18:24:44', ' 2021-07-09 17:24:44', ' 2021-07-06 03:24:44', ' 2021-07-21 19:24:44', ' 2021-07-28 01:24:44', ' 2021-07-22 13:24:44', ' 2021-07-15 22:24:44', ' 2021-06-20 04:24:44', ' 2021-06-30 16:24:44', ' 2021-07-01 21:24:44', ' 2021-07-12 15:24:44', ' 2021-06-12 15:24:44', ' 2021-06-27 13:24:44', ' 2021-07-20 21:24:44', ' 2021-07-07 07:24:44', ' 2021-06-19 07:24:44', ' 2021-07-08 03:24:44', ' 2021-07-12 02:24:44', ' 2021-07-23 17:24:44', ' 2021-06-25 12:24:44', ' 2021-08-01 12:24:44', ' 2021-06-23 15:24:44', ' 2021-07-31 08:24:44', ' 2021-07-18 19:24:44', ' 2021-06-16 23:24:44', ' 2021-07-23 00:24:44', ' 2021-06-14 12:24:44', ' 2021-06-29 04:24:44', ' 2021-06-20 17:24:44', ' 2021-06-17 21:24:44', ' 2021-07-15 01:24:44', ' 2021-06-05 07:24:44', ' 2021-07-05 01:24:44', ' 2021-06-02 16:24:44', ' 2021-07-27 05:24:44', ' 2021-06-26 03:24:44', ' 2021-06-09 06:24:44', ' 2021-06-25 05:24:44', ' 2021-06-24 06:24:44', ' 2021-06-21 19:24:44', ' 2021-06-29 18:24:44', ' 2021-07-03 08:24:44', ' 2021-06-13 14:24:44', ' 2021-07-13 20:24:44', ' 2021-07-02 13:24:44']
#  this is the output of seed.py

# what needs to be done
# convert to date time so we can compare + 1 day 
# when forming dict we form a data time dict that way everything else is easier