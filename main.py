import requests

#Função que retorna os dados de todos os usuarios
def busca_usuarios():

    url = 'https://jsonplaceholderr.typicode.com/users/'
    try:
        response = requests.get(url,
            headers = {
                'Content-Type' : 'application/json',
            },

        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}. URL: {url}")
    
#Funcao que retorna os dados do usuário com ID especifico
def busca_usuario_id(id_usuario):

    url = 'https://jsonplaceholder.typicode.com/users/' + str(id_usuario)

    try:
        response = requests.get(url,
            headers = {
                'Content-Type' : 'application/json',
            },
        )

        if response.status_code == 200:
            return response.json()  # Retorna os dados do usuário se ele existir

        elif response.status_code == 404:
            return None  # Retorna None se o usuário não existir

        else:        
            raise Exception(f"Erro na requisição: {response.status_code}") # Exceção para outros códigos de status inesperados

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}. URL: {url}")

#Fun~]ao que retorna os dados do post do usuário
def busca_post_user_id(id_usuario):

    url = 'https://jsonplaceholder.typicode.com/posts?userId=' +str(id_usuario)
    
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

def menu():
    print("\n============================= Menu =============================")
    print('Digite [ 1 ] para Exibir uma lista dos usuários com seus respectivos IDs e nomes.')
    print('Digite [ 2 ] para Inserir o ID de um Usuário e obter mais dados.')
    print('Digite [ 0 ] para Sair.')

def main():

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: ")) 

            if opcao == 1:

                print('\nLista de Usuários\n')
                usuarios = busca_usuarios()

                for usuario in usuarios:
                    print(f"ID: {usuario['id']} - Nome: {usuario['name']}")

            if opcao == 2:

                usuario_id = (input("Digite o ID do usuário desejado: "))

                if not usuario_id.isdigit() or int(usuario_id) <= 0:
                    print("\nID inválido! Digite um número positivo.")
                    continue

                usuario = busca_usuario_id(usuario_id)
                titulos = busca_post_user_id(usuario_id)

                if usuario:

                    print(f"\nNome: {usuario['name']} | Email: {usuario['email']}")
                    
                    if titulos:
                        print('\nTitulos dos posts criado por esse usuário:\n')

                        for titulo in titulos:
                            print(f"Titulo {titulo['id']} : \"{titulo['title']}\"")
                    else:
                        print(f"\nNão foram encontrados titulos para este usuário.")
           
                else:
                    print(f"\nUsuário com ID {usuario_id} não encontrado.")


            elif opcao == 0:

                print ('Saindo...')
                break
            
            else:
                print('\nDigite uma opcao valida!')

        except ValueError:
            print("\nOpção inválida! Digite um número.")
            continue  # Volta para o menu

if __name__ == "__main__":
    main()