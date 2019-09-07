def conversion(s):
    a = ""
    if s[-2:] == "AM":
        if s[:2] == "12":
            a = str("00" + s[2:8])
        else:
            a = str(s[:8])
    elif s[-2:] == "PM":
        if s[:2] == "12":
            a = str(s[:8])
        else:
            a = str (12 + int(s[:2]) ) + s[2:8]
    return a

    print(a)

s = "07:00:00PM"
print(conversion(s))
def conversion(s):
    a = ""
    if s[-2:] == "AM":
        if s[:2] == "12":
            a = str("00" + s[2:8])
        else:
            a = str(s[:8])
    elif s[-2:] == "PM":
        if s[:2] == "12":
            a = str(s[:8])
        else:
            a = str (12 + int(s[:2]) ) + s[2:8]
    return a

    print(a)

s = "07:00:00PM"
print(conversion(s))
