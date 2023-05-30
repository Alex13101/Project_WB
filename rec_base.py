
import time
import datetime
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker
import connect_base_flask
from def_extract_WB_grequests import search_right_product
from def_extract_WB_grequests import demonstration


search = input('что ищем? ')
discount_amount = input('какая скидка норм? ')
user = connect_base_flask.User(name='Alex', email='Podiyachiy-a@mail.ru')
queryx = connect_base_flask.Query(query=search, discount=discount_amount)  # Записываем в базу запрос и размер скидки
connect_base_flask.session.add(user, queryx)  # Отправляем в базу
connect_base_flask.session.commit()


result = search_right_product(search)
def record_in_base(result):
    for x in result:
        for key, value in x.items():
            if key == 'product_id':
                print(f'артикул - {value}')
                product_id = connect_base_flask.Product(id=value)
                connect_base_flask.session.add(product_id)  # Отправляем в базу
            elif key == 'salePriceU':
                print(f'цена - {value}')
                price = connect_base_flask.Product(price=value)
                connect_base_flask.session.add(price)  # Отправляем в базу
            elif key == 'name':
                print(f'Название - {value}')
                name = connect_base_flask.Product(name=value)
                connect_base_flask.session.add(name)  # Отправляем в базу
        connect_base_flask.session.commit()





demonstration(search_right_product(search))

