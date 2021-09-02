import sys

def maximum(l1, l2, l3, l4):
   len_l1 = len(l1)
   len_l2 = len(l2)
   len_l3 = len(l3)
   len_l4 = len(l4)
   lst = [len_l1, len_l2, len_l3, len_l4]
   return max(lst)

def sort_into_times(groups):
   seven = []
   seven_thirty = []
   eight = []
   eight_thirty = []
   for group in groups:
      tokens = group.strip().split("\n")
      if tokens[0] == "7:00":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               seven.append(x)
         seven.append("FLAG")
      if tokens[0] == "7:30":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               seven_thirty.append(x)
         seven_thirty.append("FLAG")
      if tokens[0] == "8:00":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               eight.append(x)
         eight.append("FLAG")
      if tokens[0] == "8:30":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               eight_thirty.append(x)
         eight_thirty.append("FLAG")
   return seven, seven_thirty, eight, eight_thirty

def boxify(lst):
   s = []
   for line in lst:
      if line == "BOOKER:":
         s.append("+----------------------------------------+")
         s.append("| {:<38} |".format(line))
      elif line == "Park" or line == "Track" or line == "Other":
         s.append("| {:^38} |".format(line))
      elif line == "POD 1:":
         s.append("| {:<38} |".format(line))
         s.append("|--------- {:<29} |".format(""))
      elif line == "POD 2:":
         s.append("| {:<38} |".format(line))
         s.append("|--------- {:<29} |".format(""))
      elif line == "POD 3:":
         s.append("| {:<38} |".format(line))
         s.append("|--------- {:<29} |".format(""))
      
      elif line == "FLAG":
         s.append("+----------------------------------------+")
         s.append("  {:<38}  ".format(""))
      else:
         s.append("| {:<38} |".format(line))
   return s

def printer(time1, time2, time3, time4):
   print("| {:^39} | {:^40} | {:^40} | {:^39} |".format("7:00", "7:30", "8:00", "8:30"))
   print("|{}|\n|{:170}|".format("-" * 170, ""))
   most = maximum(time1, time2, time3, time4)
   line = 0
   flag = 0
   while line < most:
      try:
         print(time1[line], end =" ") 
      except:
         print("  {:<38}  ".format(""), end =" ")
      try:
         print(time2[line], end =" ") 
      except:
         print("  {:<38}  ".format(""), end =" ")
      try:
         print(time3[line], end =" ") 
      except:
         print("  {:<38}  ".format(""), end =" ")
      try:
         print(time4[line], end =" ") 
      except:
         print("  {:<38}  ".format(""), end =" ")
      print("")
      line += 1
   

def main():
   file = sys.argv[1]
   with open(file) as fd:
      filelines = fd.read()
      lst = filelines.strip().split("#")
      lst = lst[:-1]
   time1, time2, time3, time4 = sort_into_times(lst)
   time1 = boxify(time1)
   time2 = boxify(time2)
   time3 = boxify(time3)
   time4 = boxify(time4)
   printer(time1, time2, time3, time4)

if __name__ == "__main__":
   main()
