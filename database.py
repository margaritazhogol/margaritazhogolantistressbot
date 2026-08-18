"""
Хранилище результатов прохождения теста на SQLite.
"""
import sqlite3
from datetime import datetime
from pathlib import Path
 
DB_PATH = Path(__file__).parent / "results.db"
 
 
def init_db() -> None:
    """Создаёт таблицу результатов, если её ещё нет."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                score INTEGER NOT NULL,
                result_title TEXT NOT NULL,
                completed_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
 
 
def save_result(user_id: int, username: str | None, score: int, result_title: str) -> None:
    """Сохраняет результат одного прохождения теста."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO results (user_id, username, score, result_title, completed_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (user_id, username, score, result_title, datetime.utcnow().isoformat()),
        )
        conn.commit()
 
 
def get_stats() -> dict:
    """Сводная статистика по всем прохождениям теста."""
    with sqlite3.connect(DB_PATH) as conn:
        total = conn.execute("SELECT COUNT(*) FROM results").fetchone()[0]
        avg_score = conn.execute("SELECT AVG(score) FROM results").fetchone()[0]
    return {"total_completions": total, "average_score": avg_score}
 
