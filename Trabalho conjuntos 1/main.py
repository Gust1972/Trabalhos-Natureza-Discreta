with open("texto.txt") as f:
    linhas = f.read().splitlines()
print(linhas)

def fazerConjunto(linha):
    conjunto = linha.split(", ")
    return conjunto

def fazerConjuntostr(linha):
    conjunto = linha.split(", ")
    return conjunto
  
def fazerUniao(c1, c2):
    list = []
    list.extend(c1)
    for x in c2:
      if x not in list:
        list.append(x)
    return list

def fazerInter(co1, co2):
    list = []
    for x in co1:
      if x in co2:
        list.append(x)
    return list

def fazerDif(con1, con2):
    list = []
    for x in con1:
      if x not in con2:
        list.append(x)
    return list

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
    print('Diferença: Conjunto 1',c7,"conjunto 2",c8,"resultado:",fazerDif(c7,c8))
  elif linha[0] == "C":
    c9 = linhas[i+1].split(", ")
    c10 = linhas[i+2].split(", ")
    conjuntosProd = []
    conjuntosProd.append(c9)
    conjuntosProd.append(c10)
    print("Produto Cartesiano: Conjunto1",c9,"Conjunto 2", c10,"Resultado:", fazerProd(conjuntosProd))
