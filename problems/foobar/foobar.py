# 1. read number from console
# 2. if number is divisible by 3 then print "foo" to console
# 3. if number is divisible by 5 then print "bar" to console
# 4. if number is divisible by 3 and 5 then print "foobar" to console
# 5. else print number to console

number = int(input("enter a number")) 
if number%3==0 and number%5==0:
    print("foobar")
elif number%3==0:
    print("foo")
elif number%5==0:
    print("bar")
else:
    print(number)