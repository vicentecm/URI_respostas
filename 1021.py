#URI 1021 https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

N = float(input())
while N >= 1000000.00 or N<=0:
    print("digite novamente")
    N = int(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in notas:
    valor = int(N/i)
    print(f"{valor:.0f} nota(s) de R$ {i:.2f}")
    N-= valor*i

print("MOEDAS:")
for i in moedas:
    valor = int(round(N,2)/i) # arredondamento
    print(f"{valor:.0f} moeda(s) de R$ {i:.2f}")
    N-= valor*i