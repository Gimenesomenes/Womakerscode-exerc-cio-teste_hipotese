import math
from scipy.stats import norm

# 1. Questão 1: 

# A associação dos proprietários de industrias metalurgicas estão muito preocupados com o tempo perdido 
# com acidentes de trabalho, cuja media, nos últimos tempos, tem sido da ordem de 60 horas/homem por ano 
# e o desvio padrão 20 horas/homem. Tentou-se um programa de prevenção de acidentes, após o qual foi tomada 
# uma amostra de nove industrias e medido o número de horas/homens perdidos por acidentes, que foi de 50 horas. 
#Você diria, no nível de 5%, que há evidências de melhoria? 


# Resolução 
# 1. Definir as hipóteses nula e alternativa: 

# H0 = 60 horas (média de horas)
# H0 < 60 horas

# 2. Escolher o nível de significância. Vamos usar 5% alpha = 0.05
# 3. Calcular a estatística do teste: Calcular o valor Z:


alpha = 0.05      # nível de significância
x_media = 50      # média da amostra
u = 60            # média sob a hipótese nula
desvpad = 20      # desvio padrão da população
n = 9             # tamanho da amostra


zcalculado = (x_media - u)/(desvpad/ math.sqrt(n))
print(f"zcalculado: {zcalculado}")


# Calcular p_valor:

p_valor = norm.cdf(zcalculado)
print(f"p_valor: {p_valor}")

z_alpha = norm.ppf(0.05)
print(f"Valor z para alpha = 0.05, é {z_alpha}")

# Comparar a estatística de teste com o valor crítico ou p-valor

if p_valor < alpha: 
  print("Rejeitar H0: Há evidências de melhoria")
else:
  print("Não rejeitar H0: Não há evidências de melhoria.")



print("\n\n\nExercício 2:")
# Questão 2:

# Um fabricando afirma que seus cigarros contêm não mais que 30mg de nicotina. Uma amostra de 25 cigarros fornece média de 31,5 mg
# e desvio padrão de 3mg. No nível de 5%, os dados refutam ou não a afirmação do fabricante? 

# 1° Determinar o parâmetro de interesse, no caso aqui será a média

# 2° Definir a hipotese nula a ser testada H0 e a alternativa H1.

# H0 <= 30 mg
# H1 > 30mg
# N = 25 cigarros
# média da amostra = 31,5 mg
# desvio padrão = 3 mg

import numpy as np
from scipy import stats


alpha = 0.05            # nível de significância
media_h0 = 30           # média alegada pelo fabricante
media_amostra = 31.5    # média da amostra
desv_pad = 3            # desvio padrão da amostra
N = 25                  # tamanho da amostra

# utilizaremos o teste t pois temos uma amostra < 30

tcalculado = (media_amostra - media_h0)/(desv_pad/ math.sqrt(N))
print(f"O valor t-calculado é: {tcalculado}")

# Graus de liberdade

graus_liberdade = N - 1
print(f"Possui {graus_liberdade} graus liberdade.")

# Calculando o valor crítico para o nível de significância de 0.05

t_critico = stats.t.ppf(0.95, graus_liberdade)
print(f"O valor do t_crítico é: {t_critico}")

if tcalculado > t_critico:
  print("Rejeitar a hipótese H0 nula, portânto os cigarros possuem <= 30mg de nicotina.")
else: 
  print("Não rejeitamos a hipótese H0, portânto os cigarros possuem > 30mg de nicotina.")


print("\n\n\nExercício 3:")


# Questão 3: 

# A resistência de um certo tipo de cabo de aço é uma variável aleatória modelada pela distribuição Normal 
# com desvio padrão igual a 6kgf. Uma amostra de tamanho 25 desses cabos, escolhida ao acaso, forneceu média igual a 9,8 kgf.
# Teste as hipóteses u = 13 versus u = 8 e tire suas conclusões a um nível de significância de 10%.


# 1. Definir a hipótese a ser testada H0
# H0 = 13
# H1 =! 13

# calcular t-student ou teste t:

media_h0 = 13
media_amostra = 9.8
desv_pad = 6
N = 25
alpha = 0.10


# Calculo estatística de z:

z_calculado =  (media_amostra - media_h0)/(desv_pad/ math.sqrt(N))
print(f"O valor de z_calculado é: {z_calculado}")

# Calcular o valor crítico para um teste bilateral:

z_critico = norm.ppf(1 - (alpha/2))
print(f"O valor de z-critico é: {z_critico}")

# Tomada de decisão:

if np.abs(z_calculado) > z_critico:
  print("Rejeitar H0: Média populacional não é igual a 13.")
else: 
  print("Não rejeitar H0: Média populacional é igual a 13.")

# Para u = 8 faria a mesma conta que foi feito para u = 13.

