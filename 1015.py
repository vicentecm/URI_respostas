# URI 1015 https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
import math

p1 = input().split(" ")
p2 = input().split(" ")

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

antes_da_raiz = ((x2-x1)**2) + ((y2-y1)**2)
raiz = math.sqrt(antes_da_raiz)

print(f"{raiz:.4f}")

