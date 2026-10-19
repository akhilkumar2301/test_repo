# Planted Issues

1. **SQL injection** - `backend/app.py`, `get_user_data()`, query construction
   line. The `username` value is interpolated directly into SQL with `%`
   formatting, allowing crafted input to alter the `WHERE` clause. A
   parameterized query should bind the value instead.

2. **Unclosed database connection** - `backend/app.py`, `get_user_data()`.
   The function opens a SQLite connection but never closes it and does not use
   a context manager. Repeated calls can leak resources and leave transactions
   or locks unmanaged.

3. **DOM-based XSS** - `frontend/script.js`, `renderUserGreeting()`.
   The `username` URL parameter is attacker-controlled and is inserted directly
   into `innerHTML`. HTML or script markup in the parameter can execute in the
   page context. Text rendering or explicit sanitization is required.

4. **Undefined function reference** - `frontend/script.js`, `window.onload`.
   The load handler calls `initializeAnalyticsEngine()`, but no such function is
   defined or imported. The resulting `ReferenceError` stops the handler before
   the greeting is rendered.