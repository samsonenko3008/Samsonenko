# TODO Напишите функцию для поиска индекса товара
def function_():
    list_ = []
    for a in items_list:
        if a is find_item:
            list_.append(items_list.index(a))
    list_.sort()
    list_.append(None)
    return list_[0]

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = function_()   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
