dados = {"crossfox": {"Km": 35000, "ano": 2005},
          "DS5": {"Km":17000 , "ano": 2015}, 
          "Fusca": {"Km": 130000, "ano": 1979}, 
          "Jetta": {"kM": 5000, "ANO": 2011}, 
          "passat": {"Km": 62000, "ano": 1999}}

print(dados.get("Jetta", "Veiculo não encontrado"))