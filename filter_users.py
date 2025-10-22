import json


def get_user_data():
    with open("users.json", "r") as file:
        users = json.load(file)
    return users


def filter_users_by_name(name):
    users = get_user_data()
    return [user for user in users if user["name"].lower() == name.lower()]


def filter_users_by_age(age):
    users = get_user_data()
    return [user for user in users if user["age"] == age]


def print_users(users):
    for user in users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? (Currently, only 'name' and 'age' is supported): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        print_users(filter_users_by_name(name_to_search))

    elif filter_option == "age":
        while True:
            age_to_search = input("Enter a age to filter users: ").strip()
            try:
                age_to_search = int(age_to_search)
                print_users(filter_users_by_age(age_to_search))
                break
            except ValueError:
                print("Please enter a valid integer for age.")
    else:
        print("Filtering by that option is not yet supported.")
