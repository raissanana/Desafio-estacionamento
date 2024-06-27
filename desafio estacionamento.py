def main():
    vagas = int(input("numero de vagas "))
    clientes = int(input("numero esperado de clientes "))
    
    lista = []
    for i in range(clientes):
        n1 = int (input ("Plano de estacionamento "))
        lista.append(n1)
     
    vagas_ocupadas = [0] * (vagas + 1)
    
    clientes_acomodados = 0
    
    for i in lista:
        if i <= vagas and not vagas_ocupadas[i]:
            vagas_ocupadas[i] = 1
            clientes_acomodados += 1
    
    print("clientes atendidos", clientes_acomodados)

main()
