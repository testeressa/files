import csv
import json

# books_file = "books.csv"
# users_file = "users.json"
# result_file = "result.json"


def create_book_list(books_file):
    with open(books_file, "r") as b:
        book_list = []
        for book in list(csv.DictReader(b)):
            book = {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"],
            }
            book_list.append(book)
    return book_list


def create_user_list(users_file):
    with open(users_file, "r") as users:
        user_list = []
        for u in json.load(users):
            user_list.append(
                {
                    "name": u.get("name"),
                    "gender": u.get("gender"),
                    "address": u.get("address"),
                    "age": u.get("age"),
                    "books": [],
                }
            )
    return user_list


def assign_owner_to_a_book(book_list, user_list):
    while len(book_list) > 0:
        for user in user_list:
            if len(book_list) > 0:
                user["books"].append(book_list.pop())
    return user_list


def create_result_file(result_file):
    user_list = assign_owner_to_a_book(create_book_list("books.csv"), create_user_list("users.json"))
    with open(result_file, "w") as r:
        result = json.dumps(user_list, indent=1)
        r.write(result)


create_result_file("result.json")
