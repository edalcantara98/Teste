nome = input("Digite o nome do vendedor: ")
v1 = float(input("Digite o valor da sua primeira venda: R$"))
v2 = float(input("Digite o valor da sua segunda venda: R$"))
v3 = float(input("Digite o valor da sua terceira venda: R$"))

media = (v1 + v2 + v3)/3
bonus = media * 0.1

print("\nNome do vendedor:", nome)
print(f"Média de venda: R$ {media:.2f}")
print(f"Bônus de 10% da média de venda: R$ {bonus:.2f}")
