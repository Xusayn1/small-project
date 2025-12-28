from core.db_settings import execute_query
def add_category():
    title = input("Enter category title: ")
    # check if title exists or not
    query = "INSERT INTO category (title) VALUES (%s)"
    params = (title,)
    if execute_query(query=query, params=params):
        print("Category is added")
    else:
        print("Something getting wrong, try again!")
def delete_category(cursor,conn):
    category_id = input("Enter category id: ")
    query = "DELETE FROM category WHERE category_id = %s"
    params = (category_id,)
    cursor.execute(query, params)
    conn.commit()
def show_all_categories():
    query = "SELECT * FROM category;"
    categories = execute_query(query=query, fetch="all")
    if categories:
        counter = 1
        for cat in categories:
            print(f"{counter}) {cat['id']}\t{cat['title']}")
            counter += 1
        return True
    else:
        print("No category")
        return None