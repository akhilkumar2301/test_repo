"""Regression tests for known backend defects.

These tests intentionally fail against the current implementation to keep the
known issues visible until `backend/app.py` is fixed.
"""

from __future__ import annotations

import sqlite3

import backend.app as app


def test_get_user_data_treats_username_as_literal_value(tmp_path, monkeypatch):
    """Malicious input must not change query behavior."""
    db_path = tmp_path / "users.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("CREATE TABLE users (username TEXT, email TEXT)")
        connection.executemany(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            [("alice", "alice@example.com"), ("bob", "bob@example.com")],
        )
        connection.commit()
    finally:
        connection.close()

    original_connect = sqlite3.connect

    def connect_to_test_db(_path: str):
        return original_connect(db_path)

    monkeypatch.setattr(app.sqlite3, "connect", connect_to_test_db)

    malicious_username = "' OR 1=1 --"
    rows = app.get_user_data(malicious_username)

    assert rows == []


def test_get_user_data_closes_connection(monkeypatch):
    """Database connections should be closed or context-managed."""

    class FakeCursor:
        def fetchall(self):
            return [("alice", "alice@example.com")]

    class FakeConnection:
        def __init__(self):
            self.closed = False
            self.entered = False
            self.exited = False

        def execute(self, _query: str):
            return FakeCursor()

        def close(self):
            self.closed = True

        def __enter__(self):
            self.entered = True
            return self

        def __exit__(self, *_args):
            self.exited = True

    fake_connection = FakeConnection()

    def connect_fake(_path: str):
        return fake_connection

    monkeypatch.setattr(app.sqlite3, "connect", connect_fake)

    app.get_user_data("alice")

    assert fake_connection.closed or (
        fake_connection.entered and fake_connection.exited
    )
