# URI 1010

linha1 = input().split(" ")
linha2 = input().split(" ")

cod1 = int(linha1[0])
num1 = int(linha1[1])
vlr1 = float(linha1[2])
cod2 = int(linha2[0])
num2 = int(linha2[1])
vlr2 = float(linha2[2])

total = (num1*vlr1)+(num2*vlr2)

print(f"VALOR A PAGAR: R$ {total:.2f}")


