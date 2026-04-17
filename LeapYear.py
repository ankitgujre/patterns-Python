'''
year = int(input("Enter year: "))

DayInYear = 365
ExtraHoursPerYear = 5
ExtraMinutesPerYear = 48
ExtraSecondsPerYear = 47.5

TotalExtraHours = ExtraHoursPerYear * 4
TotalExtraMinutes = ExtraMinutesPerYear * 4
TotalExtraPerSeconds = ExtraSecondsPerYear * 4

# convert extra times to day

ExtraHooursToDays = TotalExtraHours//24
ExtraMinutesToDays = TotalExtraMinutes // (24*60)
ExtraSecondsToDays = TotalExtraPerSeconds // (24*60*60)

# total extra daya added in 4 years

TotalExtraDays = ExtraHooursToDays + ExtraMinutesToDays + ExtraSecondsToDays

# leap year logic

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"Year is a leap year")
        else:
            print(year, "is not leap year")
    else:
        print(year,"Is not leap year")

else:
    print(year, "is not leap year")

'''

# year = int(input("Enter year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# 6. Leap Year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
