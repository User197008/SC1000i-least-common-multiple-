num = []
pri = []
fac = []
new_fac = []
conteo = []
def Enter_Number():
      count = 0
      c = int(input('Ingresar el numero de entradas:'))
      for i in range(c):
            num.append(0)
      while c!= count:
            N = int(input('Ingresar el numero:'))
            num[count] = N
            count += 1
Enter_Number()

p = max(num)            

count = 0
def numerosprimos(n): 
      for i in range(1,n+1):
        primo(i)
def primo(x):    
      if x<=1:
            return False
      else:
            for i in range(2,x-1):
                  if x%i == 0:
                        return False
      if x%1==0 and x%x==0:
            pri[count].append(x)           
            return True
for k in num:
      pri.append([])
      numerosprimos(k)
      count += 1      

def factor():
      tan = 0
      for h in num:
            fac.append([])
            while h >= 2:
                  for i in pri[tan]:
                        if h%i == 0:
                              h /= i
                              fac[tan].append(i)
            fac[tan].sort()
            tan += 1
factor()

def borrar_repetidos():
      fff = 0
      for t in fac:
            new_fac.append([])
            for i in t:
                  if i not in new_fac[fff]:
                        new_fac[fff].append(i)
            fff += 1      
borrar_repetidos()

def contar():
      ttt = 0
      for t in new_fac:
            conteo.append([])
            for w in t:
                  count = 0
                  for item in fac[ttt]:
                        if item == w:
                              count += 1
                  conteo[ttt].append(count)
            ttt += 1
contar()

factor2 = []
exponen = []
def factoexpo():
      v = []
      for item1 in new_fac:
            v += item1
      for t in v:
            factor2.append(t)

      f = []
      for item2 in conteo:
            f += item2
      for k in f:
            exponen.append(k)
factoexpo()




def unificar():
      new_factor = []
      
      expo = []
      uni =[[x,y] for x,y in zip(factor2,exponen)]

      

      coe =[]
      c = 0

      for i in range(1,p+1):
            coe.append([])
            for g in uni:
                  if g[0] == i:
                        coe[c].append(g[1])
            c += 1

      
      coe2=[]                 
      for j in coe:
            if j != []:
                  coe2.append(j)
      

      
      for a in factor2:
            if a not in new_factor:
                  new_factor.append(a)

      
      for k in coe2:
            m = max(k)
            expo.append(m)


      new_factor.sort()
      f =[]
      for x,y in zip(new_factor,expo):
           e = x**y
           f.append(e)
      
      
      MCM = 1
      for t in f:
            MCM *= t
      print('MCM es:',MCM)
unificar()

