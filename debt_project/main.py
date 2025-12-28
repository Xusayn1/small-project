from debt_project.tables import create_tables
from users import add_user, get_user
from debts import add_debt, get_debts

create_tables()

while True:
    print("""
1. User qo‘shish
2. Userlarni ko‘rish
3. Qarz qo‘shish
4. Qarzlarni ko‘rish
0. Chiqish
""")

    choice = input("Tanlang: ")

    if choice == "1":
        first_name = input("first_name: ")
        last_name = input("last_name: ")
        phone = input("Telefon: ")
        add_user(first_name,last_name, phone)
    elif choice == "2":
        user_id = int(input("User ID ni kiriting: "))
        user = get_user(user_id)

        if user:
            print(user)
        else:
            print(" Bunday user topilmadi")

    elif choice == "3":
        user_id = int(input("User ID: "))
        amount = float(input("Summa: "))
        debt_type = input("got / gave: ")
        add_debt(user_id, amount, debt_type)

    elif choice == "4":
        get_debts()

    elif choice == "0":
        break
