def weekdayChecker(_month_, _day_):
    m = [i for i in range(1, 13)]
    d = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    dooms = dict(zip(m, d))
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    weekday = 1
    tmp = _day_ - dooms[_month_]
    if tmp >= 0 :
        weekday += tmp % 7
    else :
        weekday -= abs(tmp) % 7 - 7
        weekday %= 7

    return weekdays[weekday-1]


n = int(input())
for i in range(n):
    m, d = map(int, input().split(' '))
    print(weekdayChecker(m, d))
