import requests
import time
import grequests
import time
import threading

all_products = []

search = input('Что будем искать? - ')  # Вводим запрос

start = time.time()


def search_right_product(search):
    lock_products = threading.Lock()
    all_products = []

    def save_product(product):
        global all_products
        with lock_products:
            all_products += product

    def get_products(url):
        # Отправляем GET-запрос по указанному URL-адресу и получаем JSON-ответ
        products = requests.get(url).json()['data']['products']
        return products

    def t_product(url):
        # Вызываем функцию get_products для указанного URL-адреса и сохраняем результат в общем списке all_products
        save_product(get_products(url))

    urls = [
        f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={search}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)
    ]
    start = time.time()
    threads = []
    for url in urls:
        # Создаем поток с указанной функцией t_product в качестве целевой функции и аргументом url
        thread = threading.Thread(target=t_product, args=(url,))
        threads.append(thread)
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()
    print(threads)
    print(time.time() - start)
    print(len(all_products))
    print(all_products)

#all_products = search_right_product(search)
long_lst = len(all_products)  # Длина списка товаров
print(long_lst)

for i in range(0, long_lst):  # Идем по списку всех товаров
    title = all_products[i].setdefault("name")
    price = all_products[i].setdefault('salePriceU') / 100
    id_product = all_products[i].setdefault('id')
    print(f'{i}  {title} стоит  {price}  рублей')

# print(total)
search_right_product(search)