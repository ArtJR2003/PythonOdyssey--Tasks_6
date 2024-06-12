for i in range(1, 100):
   if i > 1:
       for ii in range(2, i):
           if (i % ii) == 0:
               break
       else:
           print(i)
