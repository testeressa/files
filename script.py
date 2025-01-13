import csv
import json

books_file = "books.csv"
users_file = "users.json"
result_file = "result.json"


def assign_owner_to_a_book():

    # create book_list
    with open(books_file, "r") as b:
        book_list = list(csv.DictReader(b))

    # create user_list
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

    # assign owner to a book
    while len(book_list) > 0:
        for user in user_list:
            if len(book_list) > 0:
                user["books"].append(book_list.pop())

    with open(result_file, "w") as r:
        result = json.dumps(user_list, indent=1)
        r.write(result)


assign_owner_to_a_book()
