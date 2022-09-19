n = int(input())                 
if 1<= n <=100:                  
  if n % 2 != 0 or n % 2 == 0 and 6 <= n <= 20 :  #Checks for two actions whose output should be weird              
    print ("Weird")
  elif n % 2 == 0 and 2<=n<=5 or n>=20:           #Checks for two actions whose output should be not weird    
    print("Not Weird")
