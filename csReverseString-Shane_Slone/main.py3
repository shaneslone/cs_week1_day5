def csReverseString(chars):
   p1 = 0
   p2 = len(chars) -1
   while (p1 < p2):
       temp = chars[p1]
       chars[p1] = chars[p2]
       chars[p2] = temp
       p1 += 1
       p2 -= 1
   return chars