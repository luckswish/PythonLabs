disk_size_in_mb = 1.44
pages_in_book = 100
strings_on_page = 50
chars_in_string = 25
bytes_for_char = 4
bytes_in_kb = 1024
kb_in_mb = 1024

book_size_in_mb = pages_in_book * strings_on_page * chars_in_string * bytes_for_char / bytes_in_kb / kb_in_mb
books_count = int(disk_size_in_mb // book_size_in_mb)

print("Количество книг, помещающихся на дискету:", books_count)
