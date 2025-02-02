import requests

# Função que faz uma requisição à API para obter a lista de todos os usuários.
def busca_usuarios():

    url = 'https://jsonplaceholder.typicode.com/users/'
    try:
        response = requests.get(url,
            headers = {
                'Content-Type' : 'application/json',
            },

        )
        response.raise_for_status() # Verifica se a requisição foi bem-sucedida
        return response.json() # Retorna os dados dos usuários em formato JSON.

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}. URL: {url}") #Exibe erros de requisição, como falhas de conexão ou URLs inválidas.
        return None

# Função que faz uma requisição à API para obter os dados de um usuário específico pelo ID.
def busca_usuario_id(id_usuario):

    url = f'https://jsonplaceholder.typicode.com/users/{id_usuario}'

    try:
        response = requests.get(url,
            headers = {
                'Content-Type' : 'application/json',
            },
        )

        if response.status_code == 200:
            return response.json()  # Retorna os dados do usuário se ele existir, em formato JSON

        elif response.status_code == 404:
            return None  # Retorna None se o usuário não existir

        else:        
            raise Exception(f"Erro na requisição: {response.status_code}") # Exceção para outros códigos de status inesperados

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}. URL: {url}")
        return None

# Função que faz uma requisição à API para obter os posts de um usuário específico pelo ID.
def busca_post_user_id(id_usuario):

    url = f'https://jsonplaceholder.typicode.com/posts?userId={id_usuario}'
    
    try:
        response = requests.get(url,
            headers={
                'Content-Type' : 'application/json',

            },
        )

        if response.status_code == 200:
            return response.json()  # Retorna os dados do post se ele existir

        elif response.status_code == 404:
            return None  # Retorna None se o usuário não possuir nenhum post realizado

        else:        
            raise Exception(f"Erro na requisição: {response.status_code}") # Exceção para outros códigos de status inesperados
        
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}. URL: {url}")
        return None

#Função que exibe o menu para o usuário
def menu():
    print("\n============================= Menu =============================")
    print('Digite [ 1 ] para Exibir uma lista dos usuários com seus respectivos IDs e nomes.')
    print('Digite [ 2 ] para Inserir o ID de um Usuário e obter mais dados.')
    print('Digite [ 0 ] para Sair.')

def main():

    while True:
        menu()
        try:
            opcao = int(input("\nEscolha uma opção: ")) 

            if opcao == 1: #Opção 1: Listar todos os usuários.

                print('\nLista de Usuários\n')
                usuarios = busca_usuarios()

                for usuario in usuarios:
                    print(f"ID: {usuario['id']} - Nome: {usuario['name']}")

            elif opcao == 2: #Opção 2: Buscar um usuário pelo ID.

                usuario_id = input("Digite o ID do usuário desejado: ")

                if not usuario_id.isdigit() or int(usuario_id) <= 0: #Verifica se o ID é um número positivo válido.
                    print("\nID inválido! Digite um número positivo.")
                    continue

                usuario = busca_usuario_id(usuario_id) #Busca os dados do usuário pelo ID.
                
                if usuario: #Se o usuário for encontrado, exibe seus dados.

                    print(f"\nNome: {usuario['name']} | Email: {usuario['email']}")

                    titulos = busca_post_user_id(usuario_id) #Busca os posts do usuário pelo ID.

                    if titulos:  #Se o usuário tiver posts, exibe os títulos.
                        print('\nTitulos dos posts criado por esse usuário:\n')

                        for titulo in titulos:
                            print(f"Titulo {titulo['id']} : \"{titulo['title']}\"")
                    else:
                        print(f"\nNão foram encontrados titulos para este usuário.")
           
                else:
                    print(f"\nUsuário com ID {usuario_id} não encontrado.")


            elif opcao == 0: #Opção para sair do programa.

                print ('Saindo...')
                break
            
            else: #Mensagem para opções invalidas
                print('\nDigite uma opcao valida! (1, 2 ou 0)')

        except ValueError: #Captura erros de entrada inválida (não numérica).
            print("\nOpção inválida! Digite um número.")
            continue  #Volta para o menu

if __name__ == "__main__":
    main()