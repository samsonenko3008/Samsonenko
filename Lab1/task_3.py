information_volume_of_disk = 1.44 * 1024 ** 2
pages_in_the_book = 100
lines_per_page = 50
characters_per_line = 25
one_code = 4

one_book = one_code * characters_per_line * lines_per_page * pages_in_the_book
books = information_volume_of_disk / one_book


# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books)
