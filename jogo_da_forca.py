contador = 10
palavra = "computador"
check = False
sla = list("__________")
quantidade = 10
while(check == False):
    tentativa = input()
    quantidade -= 1
    if(quantidade == 0):
        print("Acabou as tentativas")
        break
    if(len(tentativa) == 1):
        for i in range(len(palavra)):
            if(tentativa == palavra[i]):
                contador -= 1
                sla[i] = tentativa
        print(*sla)
    else:
        if(tentativa == palavra):
            print(f"Acertou em {quantidade} tentativas!!")
            break
    print(f"Faltam {quantidade} tentativas")
    