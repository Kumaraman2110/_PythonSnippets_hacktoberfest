# find the L.C.M. of two input no.

def compute_lcm(x, y):

   # Greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 44
num2 = 14

print("The L.C.M. is", compute_lcm(num1, num2))
