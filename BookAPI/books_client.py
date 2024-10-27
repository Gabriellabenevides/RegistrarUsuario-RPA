import requests
from requests.auth import HTTPBasicAuth


def obterLivros():
    url = 'https://demoqa.com/BookStore/v1/Books'
    headers = {'Content-Type': 'application/json'}
    username = 'gabriella.benevides'  
    password = 'Ab!123456'  
     

    try:
        response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False, timeout=90)
        response.raise_for_status()  
        print("Resposta bruta:", response.text)
        data = response.json() 
        print("Sucesso:", data)

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        raise e
    except ValueError:
        print("A resposta não está no formato JSON.")

def obterLivroPorId(Id):
    url = 'https://demoqa.com/BookStore/v1/Book'
    headers = {'Content-Type': 'application/json'}
    username = 'gabriella.benevides'  
    password = 'Ab!123456'  
    params = {'ISBN': Id}

    try:
        response = requests.get(url, headers=headers, params=params, auth=HTTPBasicAuth(username, password), verify=False, timeout=90)
        response.raise_for_status()  
        print("Resposta bruta:", response.text)
        data = response.json() 
        print("Sucesso:", data)

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        raise e
    except ValueError:
        print("A resposta não está no formato JSON.")

