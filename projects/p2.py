messy_guests = ["  alice ", "bob", "   CHARLIE  ", "david smith"]
clean_guests=[]
for name in messy_guests:
    y=name.strip().title()
    clean_guests.append(y)


print(clean_guests)