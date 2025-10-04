BOOKS = (
    (1, "شازده کوچولو", "آنتوان دو سنت اگزوپری", 1943, "داستان", True),
    (2, "1984", "جورج اورول", 1949, "علمی-تخیلی", True),
    (3, "ثروت ملل", "آدام اسمیت", 1776, "اقتصاد", False),
    (4, "انسان خردمند", "یووال نوح هراری", 2011, "تاریخ", True),
    (5, "کیمیاگر", "پائولو کوئلیو", 1988, "داستان", True),
    (6, "صد سال تنهایی", "گابریل گارسیا مارکز", 1967, "داستان", False),
    (7, "هری پاتر و سنگ جادو", "جی. کی. رولینگ", 1997, "فانتزی", True),
    (8, "نبرد من", "آدولف هیتلر", 1925, "تاریخ", True),
    (9, "پدر پولدار پدر بی‌پول", "رابرت کیوساکی", 1997, "اقتصاد", True),
    (10, "دیوان حافظ", "حافظ شیرازی", 1390, "شعر", True)
)


def books(book_tupel) -> list:
    books = []
    for book in book_tupel:
        books.append( {

            "id": book[2],
            "title": book[5],
            "author": book[0],
            "publish_date": book[4],
            "gener": book[3],
            "is_available": book[1]

        })
    return books

def sort_books(books):
    
    return sorted(books, key=lambda book: (book[3], book[0]))

sorted_books = sort_books(BOOKS)
for i in sorted_books:
    print(i)
