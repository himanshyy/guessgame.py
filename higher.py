from game_data import data
import random
score=0
acc_B=random.choice(data)
continue_game=True
while continue_game:
 acc_A=acc_B#random.choice(data)
 acc_B=random.choice(data)
 while acc_A==acc_B:
   acc_B=random.choice(data)

 def formate_data(account):
  acc_name=account["name"]
  acc_description=account["description"]
  acc_nation=account["nation"]  
  return f"{acc_name},{acc_description},{acc_nation}"

 print(f"compare A :{formate_data(acc_A)}")   
 print(f"compare B: {formate_data(acc_B)}")  

 guess=input("which one have higher follower 'A' OR 'B' :").lower()

 A_followers_count=acc_A["followers"]  
 B_followers_count=acc_B["followers"]  

 def checking_answer(guess,a_follower,b_follower):
   #IF USER CHOOSE A 
    if a_follower > b_follower :
      return guess=="a"
    else:
      return guess=="b"

 Is_correct=checking_answer(guess,A_followers_count,B_followers_count) 
 if Is_correct:
   score+=1
   print(f"you are right, current score:{score}")
 else :  
     continue_game=False  
     print(f"wrong , final score is {score}")
    
