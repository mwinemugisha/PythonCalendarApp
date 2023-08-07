def intnumchk(b):
   gl =0
   while gl == 0:
     for i in range(len(b)):
       if (ord(b[i]) < 48 or ord(b[i]) > 57):
         gl = 0
         break
       elif (ord(b[i]) >= 48 and ord(b[i]) <= 57):
         gl = 1
     if (gl == 1):
       return(1)
     elif(gl == 0):
       return(0)