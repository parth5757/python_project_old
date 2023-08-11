from time import *
import random as ra
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except :
            error = error + 1
    return error
def speeed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R  = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__':
    while True:
        ck = input("ready to test: yes/no: ")
        if ck == "yes":
            t = ["Parth is best python developer.", "Parth is working at Coupon Exchange.com.", "Parth is an good investor also."]
            t1 = ra.choice(t)
            print("*****typing speed*****")
            print(t1)
            print()
            print()
            time_1 = time()
            tinput = input("Enter : ")
            time_2 = time()
            p1 = speeed_time(time_1,time_2,tinput)
            print('Speed: ', p1, "word/second")
            p2 = mistake(t1,tinput)
            print("Error :" , p2)
            
        else:
            
            print("byy")
