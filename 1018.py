#URI 1018 https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

N = int(input())
while N > 1000000 or N<0:
    print("digite novamente")
    N = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(N)
for i in notas: 
    valor = N // i
    print(f"{valor} nota(s) de R$ {i},00")
    N = N%i






