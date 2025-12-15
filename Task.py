import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40.')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике.')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = 0
        for item_name in self.__name_items:
            total += self.__item_price.get(item_name, 0) #если указанный товар присутствует в словаре, возвращает его цену. Если такого товара нет, возвращает заранее заданное значение по умолчанию (в данном случае это 0)
        if len(self.__name_items) > 10:
            total *= 0.9
        return total       #round(total, 2) округляем до двух знаков после запятой
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = 0
        total = 0
        for item in self.__name_items:
            if self.__tax_rate.get(item, None) == 20:
                twenty_percent_tax.append(item)
        for item in twenty_percent_tax:
            total += self.__item_price.get(item, 0)
        total_with_discount = sum(total)
        if len(self.__name_items) > 10:
            total_with_discount *= 0.9
        tax = total_with_discount * 0.2
        return tax

