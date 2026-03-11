quantidadeInicio = 100
print("O estoque inicial é de: ", quantidadeInicio)

recebido = 50
total = quantidadeInicio + recebido
print("O estoque final é de: ", total)

vendas = 30
restoVendas = total - vendas
print("O que sobrou das vendas foi: ", restoVendas)

devolvidos = 5
restoDevolvido = restoVendas - devolvidos
print("A quantidade que restou após devolverem foi de: ", restoDevolvido)