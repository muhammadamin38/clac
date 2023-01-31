def fn():
    c = input("Amalni kiriting: ")
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))

    if c == "+":
        print(a + b)
    elif c =="-":
        print(a - b)
    elif c =="*":
        print(a * b) 
    elif c =="/":
        print(a / b)

fn()

