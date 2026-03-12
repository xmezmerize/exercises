import os, uuid, json

class Produto:
    def __init__(self, id: str, nome: str, quantid: int):
        self.id = id
        self.nome = nome
        self.quantid = quantid

def limpar():
        os.system("clear")
        
while True:
    print("=-="*16)
    print(" Bem-vindo ao sistema da Lojinha do Sr. Marcos!")
    print("=-="*16)
    print("\n")

    try:
        opcao = int(input("Selecione a opção abaixo:\n1. Cadastrar produto\n2. Ver produtos\n3. Editar produto\n4. Deletar produtos\n5. Sair\n\n> "))
    except:
        print("> Opção inválida!\n")
        input("Pressione ENTER para continuar")
        continue

    
    if opcao == 1:
        limpar()
        
        try:
            with open("produto.json", "r", encoding="utf-8") as f:
                produtos = json.load(f)
        except:
            produtos = []
        
        id = str(uuid.uuid1())
        nome = input("Digite o nome do produto: ")
        existe = False
        
        for p in produtos:
            if p['nome'] not in nome:
                existe == True
                break
        
        if existe:
            print("Esse produto já existe no estoque!")
        else:
            quantid = int(input("Informe a quantidade do produto: "))
            
            produto = Produto(id, nome, quantid)
        
            produtos.append({
                "id": produto.id,
                "nome": produto.nome,
                "quantidade": produto.quantid
            })

            with open("produto.json", "w", encoding="utf-8") as f:
                json.dump(produtos, f, indent=4)
        
            print()
            print("Produto adicionado!\n")
   
        input("Pressione ENTER para voltar ao menu inicial")

    elif opcao == 2:
        limpar()
        
        if os.path.exists("produto.json"):
            with open("produto.json", "r", encoding="utf-8") as f:
                produtos = json.load(f)
            
            for p in produtos:
                print(f"id: {p['id']}")
                print(f"nome do produto: {p['nome']}")
                print(f"quantidade: {p['quantidade']}")
                print()
        else:
            print("Não existem produtos no estoque!\n")
        
        input("Pressione ENTER para voltar ao menu inicial")
        
    elif opcao == 3:
        limpar()
            
        filtro = int(input("Escolha qual filtro você quer para buscar o produto:\n> 1. Buscar pelo id\n> 2. Buscar pelo nome\n"))

        if os.path.exists("produto.json"):
            with open("produto.json", "r", encoding="utf-8") as f:
                produtos = json.load(f)

            if filtro == 1:
                id_busca = input("Digite o id do produto:\n> ")

                for p in produtos:
                    if p['id'] == id_busca:
                        novo_nome = input("Digite um novo nome para o produto: ")
                        nova_quantidade = input("Informe a quantidade do produto: ")

                        if novo_nome != "":
                            p['nome'] = novo_nome

                        if nova_quantidade != "":
                            p['quantidade'] = int(nova_quantidade)

            elif filtro == 2:
                nome_busca = input("Digite o nome do produto desejado: ")

                for p in produtos:
                    if p['nome'] == nome_busca:
                        novo_nome = input("Digite um novo nome para o produto: ")
                        nova_quantidade = input("Informe a quantidade do produto: ")

                        if novo_nome != "":
                            p['nome'] = novo_nome

                        if nova_quantidade != "":
                            p['quantidade'] = int(nova_quantidade)

            with open("produto.json", "w", encoding="utf-8") as f:
                json.dump(produtos, f, indent=4)

            print("\nSeu produto foi atualizado com sucesso!\n")

        else:
                print("Não existem produtos no estoque!\n")

        input("Pressione ENTER para voltar ao menu inicial")

    elif opcao == 4:
        limpar()
        
        filtro = int(input("Digite o filtro desejado para deletar um produto do sistema:\n> 1. Deletar pelo id\n> 2. Deletar pelo nome\n"))
        
        if filtro == 1:
            if os.path.exists("produto.json"):
                with open("produto.json", "r", encoding="utf-8") as f:
                    json.load(f)
        
                id_busca = input("Digite o id do produto:\n> ")
        
                for p in produtos:
                    if p['id'] == id_busca:
                        produtos.remove(p)
                        print(f"O produto: {p['nome']} foi deletado com sucesso.\n")
        
                with open("produto.json", "w", encoding="utf-8") as f:
                    json.dump(produtos, f, indent=4)
            else:
                print("Não existem produtos no estoque!\n")
        elif filtro == 2:
            if os.path.exists("produto.json"):
                with open("produto.json", "r", encoding="utf-8") as f:
                    json.load(f)
                
                nome_busca = input("Digite o nome do produto:\n> ")
                
                for p in produtos:
                    if p['nome'] == nome_busca:
                        produtos.remove(p)
                        print(f"O produto: {p['nome']} - foi deletado com sucesso.\n")
                
                with open("produto.json", "w", encoding="utf-8") as f:
                    json.dump(produtos, f, indent=4)
            else:
                print("Não existem produtos no estoque!\n")
                
        input("Pressione ENTER para voltar ao menu inicial")
    elif opcao == 5:
        limpar()
        
        print("Volte sempre! :)")
        break
