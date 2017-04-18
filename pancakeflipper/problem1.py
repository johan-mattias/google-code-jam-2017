import sys

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

debug = 0

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = raw_input().split(" ")  # read a list of integers, 2 in this case

  flip_count = 0
  n_list = list(n)


  flag = 1
  imp_flag = 0

  for index in range(len(n_list)):
    if (n_list[index]!="+"):
      flag = 0
      #flip k next spaces
      if(debug): print "flip"
      flip_count+=1
      if(debug): print index, " : ", n_list
      for x in range(0, int(k)):
        if((x+index)<len(n_list)):
          #print "char", n_list[x+index], "index", index, "place", x
          if(n_list[x+index] == "+"):
            n_list[x+index] = "-"
          else:
            n_list[x+index] = "+"
        else:
          imp_flag = 1
      if(debug): print index, " : ", n_list
            
  if flag == 1:
  	print("Case #{}: {}".format(i, 0))
  elif imp_flag == 1:
    print("Case #{}: {}".format(i, "IMPOSSIBLE"))
  else:
    print("Case #{}: {}".format(i, flip_count))

