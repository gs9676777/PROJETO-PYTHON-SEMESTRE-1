
menu = {
    1: "Cadastrar",
    2: "Login",
    3: "Login como administrador",
    0: "Sair"
}

menu1 = {
    1: "Musicas",
    2: "Playlist",
    3: "Historico",
    0: "Sair"
}

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = usuario() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Novo contato
            cadastrar() # Chama a função novo_contato
        elif escolha == 2: # Procurar contato
            login()
        elif escolha == 3:
            sair() # Chama a função procurar_contato
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida
    
def home():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = spotifei() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Novo contato
            cadastrar() # Chama a função novo_contato
        elif escolha == 2: # Procurar contato
            login() # Chama a função procurar_contato
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.")

def usuario():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Portal do Usuário:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def spotifei():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("bem-vindo ao spotifei:")
    for opcao, descricao in menu1.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def cadastrar():
    """
    Função para adicionar um novo contato à agenda.
    """
    print("Novo contato:")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")
    # Abre o arquivo contatos.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_contatos = open("contatos.txt", "a")
    # Grava o contato no arquivo
    arquivo_contatos.write(f"{email},{senha}\n") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_contatos.close()
    print("Seu login foi realizado com sucesso!") # Mensagem de sucesso
    
def login():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    print("Procurar contato:")
    email_procurar = input("Digite seu email de login: ")
    senha_procurar = input("Digite sua senha: ")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("contatos.txt", "r") as arquivo_contatos:
        conteudo = arquivo_contatos.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        email,senha = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if email_procurar.lower() == email.lower() and senha_procurar == senha.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Usuario logado")
            home() # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("usuario não encontrado, por favor tente novamente.") # Mensagem de erro se o contato não for encontrado
        
    
def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() # Encerra o programa
            
if __name__ == "__main__":
    main() # Chama a função main para iniciar o programa