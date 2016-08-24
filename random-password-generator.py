# -*- coding: utf-8 -*-
import random
import pyperclip
print "\n\n\n[================================================]"
print "[Random password generator by Jayaram Yalla      ]"
print "[================================================]\n\n\n"           

def one():
    ca=random.choice('abcdefghijklmnopqrstuvwxyz')
    return ca


def two():
    sm=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return sm

def three():
    sp1=r'~@#$%^&*()_+{}[]|,.'
    spr=random.choice(sp1)
    return spr

def four():
    n=random.choice("0123456789")
    return n
    

ram=[one,two,three,four]

ps=""
for i in range(2):
    ps+=random.choice(ram)()+random.choice(ram)()+random.choice(ram)()+random.choice(ram)()


f=open("randpassword.txt","a")
print "\n\n"
print ps
pyperclip.copy(ps)
print "\n\n"
ps=ps+",\n"
f.writelines(ps)
f.close()

print "coded by jayaram Yalla"
#coded and designed by jayaram Yalla
