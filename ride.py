print("HI, You have to just enter your rides i'll calculate your bonus")
earning = int(input("Enter your total Earnings in a day"))
 
bonus = 0
if(earning>8000):
    print("Congrats! you've just unlock the bonus!")
    bonus = earning*0.5
    print("Your b=calculated bonus is:",bonus)
    total_earning = bonus+earning
    print("Your Total earning is:", total_earning, " Enjoy the moment!")
else:
    print("sorrry! ur not eligible for bonus.. next time")