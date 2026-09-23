# questionnare = ["1.What is the capital of france","2.what is the most  expensive coffee in the world","3.name the first man to climb mount everest"]

# print("Press Enter to Start The Game")

lis1= [[1,'a'],[2,'b'],[3,'c']]


# for i in lis1:
#    ans=input("enter answer:")
#    if(ans==i[1]):
#       print("correct answer added 1 rupee")
      
      
        
        
#    else:
#         print("wrong answer")
#         break

count=0
for i in lis1:
   option = input("enter choice")
   if(option==i[1]):
      print("correct answer added 1 rupee")
      count+=1
      print("your win this much:",count)
   else:
      print("wrong answer")
      break   

if(count==len(lis1)):
   print("you won the game and won",count,'rupees')
   