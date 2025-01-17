import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from solution import SupahandsBadger


def testcase1():
    data = ['2021-06-29 20:00:34', ' 2021-07-05 08:00:34', ' 2021-07-26 06:00:34', ' 2021-07-01 03:00:34', ' 2021-06-12 11:00:34', ' 2021-07-10 11:00:34', ' 2021-07-04 10:00:34', ' 2021-06-16 11:00:34', ' 2021-07-09 10:00:34', ' 2021-07-24 20:00:34', ' 2021-06-28 18:00:34', ' 2021-06-26 14:00:34', ' 2021-07-17 18:00:34', ' 2021-06-21 21:00:34', ' 2021-06-21 08:00:34', ' 2021-06-18 06:00:34', ' 2021-06-02 17:00:34', ' 2021-07-23 02:00:34', ' 2021-06-27 08:00:34', ' 2021-07-14 03:00:34', ' 2021-07-19 12:00:34', ' 2021-07-28 11:00:34', ' 2021-06-08 10:00:34', ' 2021-07-03 01:00:34', ' 2021-07-06 00:00:34', ' 2021-07-30 20:00:34', ' 2021-07-08 01:00:34', ' 2021-07-30 01:00:34', ' 2021-06-05 21:00:34', ' 2021-07-27 02:00:34', ' 2021-06-14 19:00:34', ' 2021-06-22 19:00:34', ' 2021-06-18 14:00:34', ' 2021-06-09 13:00:34', ' 2021-07-20 14:00:34', ' 2021-06-25 04:00:34', ' 2021-07-29 00:00:34', ' 2021-07-16 02:00:34', ' 2021-06-27 23:00:34', ' 2021-07-13 14:00:34', ' 2021-06-13 07:00:34', ' 2021-07-16 21:00:34', ' 2021-06-11 09:00:34', ' 2021-07-25 15:00:34', ' 2021-07-01 21:00:34', ' 2021-06-04 04:00:34', ' 2021-06-07 10:00:34', ' 2021-06-23 14:00:34', ' 2021-07-11 18:00:34', ' 2021-08-01 15:00:34', ' 2021-06-19 08:00:34']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()
    expected = {
            '2021-07-23 - 2021-07-30': 8,
            '2021-06-25 - 2021-06-29': 5,
            '2021-07-08 - 2021-07-11': 4,
            '2021-07-03 - 2021-07-06': 4, 
            '2021-06-11 - 2021-06-14': 4,
            '2021-06-21 - 2021-06-23': 3,
            '2021-06-07 - 2021-06-09': 3,
            '2021-07-19 - 2021-07-20': 2,
            '2021-07-16 - 2021-07-17': 2,
            '2021-07-13 - 2021-07-14': 2,    
            '2021-06-18 - 2021-06-19': 2,
            '2021-06-04 - 2021-06-05': 2,
            '2021-08-01 - 2021-08-01': 1,
            '2021-07-01 - 2021-07-01': 1,
            '2021-06-16 - 2021-06-16': 1,
            '2021-06-02 - 2021-06-02': 1
        }

    assert (result == expected),"Test case 1 failed!"
    print("Test case 1 Success!")


def testcase2():
    data = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()

    expected = {'2021-03-16 - 2021-03-18': 3, '2021-03-13 - 2021-03-13': 1}

    if result != expected:
        print('result: ',result)
        print('expected: ',expected)

    assert (result == expected),"Test case 2 failed!"
    print("Test case 2 Success!")

def testcase3():
    data = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05', '2021-03-23 15:13:05']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()

    expected = {'2021-03-16 - 2021-03-18': 3, '2021-03-23 - 2021-03-23': 1, '2021-03-13 - 2021-03-13': 1}

    if result != expected:
        print('result: ',result)
        print('expected: ',expected)

    assert (result == expected),"Test case 3 failed!"
    print("Test case 3 Success!")

def testcase4():
    data = ['2021-03-13 15:13:05', '2021-03-20 23:13:05']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()

    expected = {'2021-03-20 - 2021-03-20': 1, '2021-03-13 - 2021-03-13': 1}

    if result != expected:
        print('result: ',result)
        print('expected: ',expected)

    assert (result == expected),"Test case 4 failed!"
    print("Test case 4 Success!")    

def testcase5():
    data = ['2021-03-13 15:13:05', '2021-03-14 23:13:05','2021-03-15 23:13:05','2021-03-20 23:13:05','2021-03-21 23:13:05']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()

    expected = {'2021-03-13 - 2021-03-15': 3, '2021-03-20 - 2021-03-21': 2}

    if result != expected:
        print('result: ',result)
        print('expected: ',expected)

    assert (result == expected),"Test case 5 failed!"
    print("Test case 5 Success!")       

def testcase6():
    data = ['2021-03-13 15:13:05', '2021-03-14 23:13:05','2021-03-15 23:13:05','2021-03-20 23:13:05','2021-03-25 23:13:05']

    new = SupahandsBadger(data)
    result = new.calculateBadgesToAward()

    expected = {'2021-03-13 - 2021-03-15': 3, '2021-03-25 - 2021-03-25': 1, '2021-03-20 - 2021-03-20': 1}

    if result != expected:
        print('result: ',result)
        print('expected: ',expected)

    assert (result == expected),"Test case 6 failed!"
    print("Test case 6 Success!")   

testcase1()
testcase2()
testcase3()
testcase4()
testcase5()
testcase6()
