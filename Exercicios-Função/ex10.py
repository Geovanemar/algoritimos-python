def contar_vogal(n):
    vogais = "aeiouAEIOU"
    return sum(  i in "aeiouAEIOU" for i in n)

print(contar_vogal("Deus é bom demais"))