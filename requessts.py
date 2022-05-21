import requests


def checkAutoTable(token):

    endpoint = "http://localhost:8080/autos/getAll"
    headers = {"Authorization": f"Bearer {token}"}
    print(requests.get(endpoint, data='', headers=headers).json())


def checkPersonnelTable(token):
    endpoint = "http://localhost:8080/personnels/getAll"
    headers = {"Authorization": f"Bearer {token}"}
    print(requests.get(endpoint, data='', headers=headers).json())


def checkJournalTable(token):
    endpoint = "http://localhost:8080/journals/getAll"
    headers = {"Authorization": f"Bearer {token}"}
    print(requests.get(endpoint, data='', headers=headers).json())


def checkRoutesTable(token):
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://localhost:8080/routes/"
    while True:
        print('1 - Показать все маршруты')
        print('2 - Найти маршрут по id')
        print('8 - Назад')
        print('9 - Выход из программы')
        x = input()
        if int(x) == 1:
            print(requests.get(endpoint + 'getAll', data='', headers=headers).json())
        if int(x) == 2:
            id = input('Введите id маршрута\n')
            print(requests.get(endpoint + f'getRouteById?id={id}', data='', headers=headers).json())
        if int(x) == 8:
            return
        if int(x) == 9:
            exit(0)


def editRoutesTable(token):
    endpoint = "http://localhost:8080/routes/addNew"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        'name': 'Moscow',
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.text)


def editAutosTable(token):
    endpoint = "http://localhost:8080/routes/addNew"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        'name': 'Moscow',
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.json())


def editPersonnelTable(token):
    endpoint = "http://localhost:8080/routes/addNew"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        'name': 'Moscow',
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.json())


def editJournalTable(token):
    endpoint = "http://localhost:8080/routes/addNew"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        'name': 'Moscow',
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.json())