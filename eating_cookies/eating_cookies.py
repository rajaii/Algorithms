#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return eating_cookies(n - 1) + eating_cookies(n-2) + eating_cookies(n-3)
  

  
print(eating_cookies(1)) #1
print(eating_cookies(2))# 2
print(eating_cookies(5))# 13
print(eating_cookies(10))# 274

[3]
[1,2]
[1,1,1]
[2,1]

#  He can eat 1 cookie at a time 3 times
#  He can eat 1 cookie, then 2 cookies 
#  He can eat 2 cookies, then 1 cookie
#  He can eat 3 cookies all at once. 
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')