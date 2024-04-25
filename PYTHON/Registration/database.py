import sqlite3
from abc import ABC
from contextlib import closing

conn = sqlite3.connect("users.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"age"	INTEGER,
	"gender"	TEXT,
	"phone_number" INTEGER,
	"location"	TEXT,
	"latitude"	REAL,
	"longitude"	REAL,
	"chat_id"	INTEGER,
	"user_name"	TEXT);
""")
conn.commit()

class BaseCRUD(ABC):
	def __init__(self, database_path, table_name):
		self.database_path = database_path
		self.table_name = table_name

	def get_connection(self):
		return closing(sqlite3.connect(self.database_path))

	def insert(self, **kwargs):
		with self.get_connection() as connection:
			cursor = connection.cursor()
			columns = ', '.join(kwargs.keys())
			placeholders = ', '.join('?' for _ in kwargs)
			query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
			cursor.execute(query, tuple(kwargs.values()))
			connection.commit()

	# return cursor.lastrowid

	def get(self, chat_id):
		with self.get_connection() as connection:
			cursor = connection.cursor()
			query = f"SELECT * FROM {self.table_name} WHERE chat_id=?"
			cursor.execute(query, (chat_id,))
			cursor = dict_fetchone(cursor)
			return cursor

	def get_all(self):
		with self.get_connection() as connection:
			cursor = connection.cursor()
			query = f"SELECT * FROM {self.table_name}"
			cursor.execute(query)
			cursor = dict_fetchall(cursor)
			return cursor

	def update(self, chat_id, **kwargs):
		with self.get_connection() as connection:
			cursor = connection.cursor()
			columns = ', '.join(f"{key}=?" for key in kwargs)
			query = f"UPDATE {self.table_name} SET {columns} WHERE chat_id=?"
			cursor.execute(query, (*kwargs.values(), chat_id))
			connection.commit()

	def delete(self, chat_id):
		with self.get_connection() as connection:
			cursor = connection.cursor()
			query = f"DELETE FROM {self.table_name} WHERE chat_id=?"
			cursor.execute(query, (chat_id,))
			connection.commit()


def dict_fetchall(cursor):
	columns = [i[0] for i in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dict_fetchone(cursor):
	columns = [i[0] for i in cursor.description]
	return dict(zip(columns, cursor.fetchone()))


users = BaseCRUD("../Registration-db/database/users.db", "users")
# address = BaseCRUD("users.db", "address")
# users.insert(first_name="John", last_name="Doe", chat_id="123")
# users.update(chat_id=123, first_name="updated")
# users.delete(chat_id=1)


# get_user = users.get(chat_id=123)
# get_users = users.get_all()
# print(users.get_all())