import MySQLdb
import sys

def test_db():
    try:
        db = MySQLdb.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            db="quizapp",
            port=3306
        )
        print("Successfully connected to quizapp database")
        db.close()
    except Exception as e:
        print(f"Error connecting to database: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    test_db()
