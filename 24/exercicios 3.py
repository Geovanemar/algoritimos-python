while True:
    nota = int(input("digite uma nota: "))
    if nota >= 0 and nota <= 10:
        print("a nota é:" , nota)
        break
    else:
        print("esse valor não condiz")
        
