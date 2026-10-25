# Planted Issues

1. **SQL injection** - `backend/app.py`, `get_user_data()`, query construction
   line. The `username` value is interpolated directly into SQL with `%`
   formatting, allowing crafted input to alter the `WHERE` clause. A
   parameterized query should bind the value instead.

2. **Unclosed database connection** - `backend/app.py`, `get_user_data()`.
   The function opens a SQLite connection but never closes it and does not use
   a context manager. Repeated calls can leak resources and leave transactions
   or locks unmanaged.
