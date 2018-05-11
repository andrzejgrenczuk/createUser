import random

imie = raw_input("Firstname: ")

nazwisko = raw_input("Lastname: ")

def user(imie,nazwisko):
    user = nazwisko[:5] + imie[:2]
    if len(nazwisko) <= 2:
        user = nazwisko[:2] + imie[:5]
    print(user)

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
passlen = 14
p =  "".join(random.sample(s,passlen ))

print'Genereated user name is:' , user(imie,nazwisko)
print'User password is:' , p