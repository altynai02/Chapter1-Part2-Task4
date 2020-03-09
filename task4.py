# 4. A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. ( 6, 1, 30, 6, 2, 10 result 40 sec.)

first_hour = int(input("Enter the first timestamp' hour: "))
first_minute = int(input("Enter the first timestamp' minute: "))
first_second = int(input("Enter the first timestamp' second: "))

second_hour = int(input("Enter the second timestamp' hour: "))
second_minute = int(input("Enter the second timestamp' minute: "))
second_second = int(input("Enter the second timestamp' second: "))

first_timestamp = ((first_hour * 360) + (first_minute*60) + first_second)
second_timestamp = ((second_hour * 360)+ (second_minute * 60 ) + second_second)

print(second_timestamp - first_timestamp)