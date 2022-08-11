with open("texto.txt") as f:
    linhas = f.read().splitlines()
print(linhas)

def fazerConjunto(linha):
    conjunto = linha.split(", ")
    conjunto = set([int(i) for i in conjunto])
    return conjunto

def fazerConjuntostr(linha):
    conjunto = linha.split(", ")
    conjunto = set([str(i) for i in conjunto])
    return conjunto
  
def fazerUniao(c1, c2):
    return c1.union(c2)

def fazerInter(co1, co2):
    return co1.intersection(co2)

def fazerDif(con1, con2):
    return con1.diference(con2)

def fazerProd(con1):
  resultado = [[]]
  for s in con1:
    resultado = [x+[y] for x in resultado for y in s]
  return resultado

#Analisar o arquivo txt lido e realizar as operações
for i, linha in enumerate(linhas):
  if linha[0] == "U":
    c1 = fazerConjuntostr(linhas[i + 1])
    c2 = fazerConjuntostr(linhas[i + 2])
    c3 = fazerUniao(c1, c2)
    print("União: Conjunto 1", c1, "conjunto 2", c2, "resultado", c3)
  elif linha[0] == "I":
    c4 = fazerConjuntostr(linhas[i + 1])
    c5 = fazerConjuntostr(linhas[i + 2])
    c6 = fazerInter(c4, c5)
    print("Interseção: Conjunto 1", c4, "conjunto 2", c5, "resultado", c6)
  elif linha[0] == "D":
    c7 = fazerConjuntostr(linhas[i+1])
    c8 = fazerConjuntostr(linhas[i+2])
    print('Diferença: Conjunto 1',c7,"conjunto 2",c8,"resultado:",c7.difference(c8))
  elif linha[0] == "C":
    c9 = linhas[i+1].split(", ")
    c10 = linhas[i+2].split(", ")
    conjuntosProd = []
    conjuntosProd.append(c9)
    conjuntosProd.append(c10)
    print("Produto Cartesiano: Conjunto1",c9,"Conjunto 2", c10,"Resultado:", fazerProd(conjuntosProd))
      
