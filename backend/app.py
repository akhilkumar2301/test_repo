import sqlite3
import sys


def get_user_data(username):
    connection = sqlite3.connect("users.db")
    query = "SELECT username, email FROM users WHERE username = '%s'" % username
    rows = connection.execute(query).fetchall()
    return rows


if __name__ == "__main__":
    requested_user = sys.argv[1] if len(sys.argv) > 1 else "alice"
    print(get_user_data(requested_user))