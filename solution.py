
import subprocess
import sys


class supahandsBadger:
    def __init__(self):
        self.timestamps = self.generateSeed()

    def generateSeed(self):
        # # run seed.py to get random timestamps
        # result = subprocess.run(['python', "seed.py"], capture_output=True, text=True)

        # # (constant time loop) post process output to form timestamps array 
        # for char in ['[', ']' , '\n', "'"]:
        #     result.stdout = result.stdout.replace(char,"")
        # print("stdout:",result.stdout.split(','))
        # return result.stdout.split(',')

        return ['2021-06-29 20:00:34', ' 2021-07-05 08:00:34', ' 2021-07-26 06:00:34', ' 2021-07-01 03:00:34', ' 2021-06-12 11:00:34', ' 2021-07-10 11:00:34', ' 2021-07-04 10:00:34', ' 2021-06-16 11:00:34', ' 2021-07-09 10:00:34', ' 2021-07-24 20:00:34', ' 2021-06-28 18:00:34', ' 2021-06-26 14:00:34', ' 2021-07-17 18:00:34', ' 2021-06-21 21:00:34', ' 2021-06-21 08:00:34', ' 2021-06-18 06:00:34', ' 2021-06-02 17:00:34', ' 2021-07-23 02:00:34', ' 2021-06-27 08:00:34', ' 2021-07-14 03:00:34', ' 2021-07-19 12:00:34', ' 2021-07-28 11:00:34', ' 2021-06-08 10:00:34', ' 2021-07-03 01:00:34', ' 2021-07-06 00:00:34', ' 2021-07-30 20:00:34', ' 2021-07-08 01:00:34', ' 2021-07-30 01:00:34', ' 2021-06-05 21:00:34', ' 2021-07-27 02:00:34', ' 2021-06-14 19:00:34', ' 2021-06-22 19:00:34', ' 2021-06-18 14:00:34', ' 2021-06-09 13:00:34', ' 2021-07-20 14:00:34', ' 2021-06-25 04:00:34', ' 2021-07-29 00:00:34', ' 2021-07-16 02:00:34', ' 2021-06-27 23:00:34', ' 2021-07-13 14:00:34', ' 2021-06-13 07:00:34', ' 2021-07-16 21:00:34', ' 2021-06-11 09:00:34', ' 2021-07-25 15:00:34', ' 2021-07-01 21:00:34', ' 2021-06-04 04:00:34', ' 2021-06-07 10:00:34', ' 2021-06-23 14:00:34', ' 2021-07-11 18:00:34', ' 2021-08-01 15:00:34', ' 2021-06-19 08:00:34']

    def calculateBadges(self):
        timestamp_map = {}
        import datetime
        for timestamp in self.timestamps:
            date = timestamp.strip().split(' ')[0]

            dateStamp = datetime.datetime.strptime(date, "%Y-%m-%d")

            if dateStamp not in timestamp_map:
                timestamp_map[dateStamp] = 0
            timestamp_map[dateStamp] += 1     

        sortedDateStamps = sorted(timestamp_map)
        print(timestamp_map)
        print(sortedDateStamps)
        
        badgeCountMap = {}
        badgeCount = 0
        startDate  = str(sortedDateStamps[0])
        endDate    = ""
        
        for idx in range(len(sortedDateStamps)-1):
            targetDate = sortedDateStamps[idx]
            nextDay = targetDate + datetime.timedelta(days=1)
            print(targetDate, nextDay, timestamp_map[targetDate])

            if sortedDateStamps[idx+1] == nextDay:
                badgeCount += timestamp_map[targetDate]
            else:
                badgeCount += timestamp_map[targetDate]
                endDate = str(sortedDateStamps[idx])
                timeline = startDate + "-" + endDate
                badgeCountMap[timeline] = badgeCount
                print('new input: ',startDate,endDate,badgeCount,'\n')

                # reset 
                badgeCount = 0
                startDate  = str(sortedDateStamps[idx+1])
                endDate    = ""                

            
# loop 1 (2021, 6, 2, 0, 0) , next (2021, 6, 3, 0, 0), actual (2021, 6, 4, 0, 0), count 0 -> 2, reset count start and end date run agian


# [datetime.datetime(2021, 6, 2, 0, 0), datetime.datetime(2021, 6, 4, 0, 0), datetime.datetime(2021, 6, 5, 0, 0), datetime.datetime(2021, 6, 7, 0, 0), datetime.datetime(2021, 6, 8, 0, 0), datetime.datetime(2021, 6, 9, 0, 0), datetime.datetime(2021, 6, 11, 0, 0), datetime.datetime(2021, 6, 12, 0, 0), datetime.datetime(2021, 6, 13, 0, 0), datetime.datetime(2021, 6, 14, 0, 0), datetime.datetime(2021, 6, 16, 0, 0), datetime.datetime(2021, 6, 18, 0, 0), datetime.datetime(2021, 6, 19, 0, 0), datetime.datetime(2021, 6, 21, 0, 0), datetime.datetime(2021, 6, 22, 0, 0), datetime.datetime(2021, 6, 23, 0, 0), datetime.datetime(2021, 6, 25, 0, 0), datetime.datetime(2021, 6, 26, 0, 0), datetime.datetime(2021, 6, 27, 0, 0), datetime.datetime(2021, 6, 28, 0, 0), datetime.datetime(2021, 6, 29, 0, 0), datetime.datetime(2021, 7, 1, 0, 0), datetime.datetime(2021, 7, 3, 0, 0), datetime.datetime(2021, 7, 4, 0, 0), datetime.datetime(2021, 7, 5, 0, 0), datetime.datetime(2021, 7, 6, 0, 0), datetime.datetime(2021, 7, 8, 0, 0), datetime.datetime(2021, 7, 9, 0, 0), datetime.datetime(2021, 7, 10, 0, 0), datetime.datetime(2021, 7, 11, 0, 0), datetime.datetime(2021, 7, 13, 0, 0), datetime.datetime(2021, 7, 14, 0, 0), datetime.datetime(2021, 7, 16, 0, 0), datetime.datetime(2021, 7, 17, 0, 0), datetime.datetime(2021, 7, 19, 0, 0), datetime.datetime(2021, 7, 20, 0, 0), datetime.datetime(2021, 7, 23, 0, 0), datetime.datetime(2021, 7, 24, 0, 0), datetime.datetime(2021, 7, 25, 0, 0), datetime.datetime(2021, 7, 26, 0, 0), datetime.datetime(2021, 7, 27, 0, 0), datetime.datetime(2021, 7, 28, 0, 0), datetime.datetime(2021, 7, 29, 0, 0), datetime.datetime(2021, 7, 30, 0, 0), datetime.datetime(2021, 8, 1, 0, 0)]

new = supahandsBadger()
new.calculateBadges()


# ['2021-07-30 05:24:44', ' 2021-07-25 16:24:44', ' 2021-06-15 16:24:44', ' 2021-06-11 05:24:44', ' 2021-07-11 10:24:44', ' 2021-06-06 21:24:44', ' 2021-06-08 05:24:44', ' 2021-07-16 23:24:44', ' 2021-06-22 18:24:44', ' 2021-07-09 17:24:44', ' 2021-07-06 03:24:44', ' 2021-07-21 19:24:44', ' 2021-07-28 01:24:44', ' 2021-07-22 13:24:44', ' 2021-07-15 22:24:44', ' 2021-06-20 04:24:44', ' 2021-06-30 16:24:44', ' 2021-07-01 21:24:44', ' 2021-07-12 15:24:44', ' 2021-06-12 15:24:44', ' 2021-06-27 13:24:44', ' 2021-07-20 21:24:44', ' 2021-07-07 07:24:44', ' 2021-06-19 07:24:44', ' 2021-07-08 03:24:44', ' 2021-07-12 02:24:44', ' 2021-07-23 17:24:44', ' 2021-06-25 12:24:44', ' 2021-08-01 12:24:44', ' 2021-06-23 15:24:44', ' 2021-07-31 08:24:44', ' 2021-07-18 19:24:44', ' 2021-06-16 23:24:44', ' 2021-07-23 00:24:44', ' 2021-06-14 12:24:44', ' 2021-06-29 04:24:44', ' 2021-06-20 17:24:44', ' 2021-06-17 21:24:44', ' 2021-07-15 01:24:44', ' 2021-06-05 07:24:44', ' 2021-07-05 01:24:44', ' 2021-06-02 16:24:44', ' 2021-07-27 05:24:44', ' 2021-06-26 03:24:44', ' 2021-06-09 06:24:44', ' 2021-06-25 05:24:44', ' 2021-06-24 06:24:44', ' 2021-06-21 19:24:44', ' 2021-06-29 18:24:44', ' 2021-07-03 08:24:44', ' 2021-06-13 14:24:44', ' 2021-07-13 20:24:44', ' 2021-07-02 13:24:44']
#  this is the output of seed.py

# what needs to be done
# convert to date time so we can compare + 1 day 
# when forming dict we form a data time dict that way everything else is easier