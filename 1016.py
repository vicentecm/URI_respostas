#URI 1016 https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

entrada = int(input())
X = 60
Y = 90
diferenca_por_hora = Y - X
diferenca_km_por_minuto = diferenca_por_hora / 60
tempo = entrada / diferenca_km_por_minuto
print(f"{tempo:.0f} minutos")




