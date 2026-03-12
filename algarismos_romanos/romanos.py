import json

while True:
    
    with open("romanos.json", "r", encoding="utf-8") as f:
        letras_romanas = json.load(f)

    print("=-="*6)
    print("Algarismos Romanos")
    print("=-="*6)
    print(f"\nI: {letras_romanas['I']}")
    print(f"V: {letras_romanas['V']}")
    print(f"X: {letras_romanas['X']}")
    print(f"L: {letras_romanas['L']}")
    print(f"C: {letras_romanas['C']}")
    print(f"D: {letras_romanas['D']}")
    print(f"M: {letras_romanas['M']}\n")

    num_romano = input("Digite um algarismo romano: ").upper()

    soma = 0
    anterior = 0

    for l in reversed(num_romano):
        valor = letras_romanas[l]
        
        if valor < anterior:
            soma -= valor
        else:
            soma += valor
        
        anterior = valor

    print(soma)
    break
