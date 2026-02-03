import MySQLdb
import sys
import os

def setup_db():
    try:
        # Connect without db name to create it
        conn = MySQLdb.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            port=3306
        )
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS quizapp;")
        conn.select_db("quizapp")
        print("Database 'quizapp' created/selected.")

        sql_path = os.path.join("DB", "quizappstructure.sql")
        if not os.path.exists(sql_path):
            print(f"Error: SQL file not found at {sql_path}")
            return

        print(f"Importing {sql_path}...")
        with open(sql_path, 'r') as f:
            sql_script = f.read()
            
        # Splitting script by semicolon to execute commands one by one
        # This is a simple approach and might fail for complex scripts with stored procs, 
        # but for standard structure it should work.
        commands = sql_script.split(';')
        for command in commands:
            cmd = command.strip()
            if cmd:
                try:
                    cur.execute(cmd)
                except Exception as e:
                    print(f"Warning: Failed to execute command: {e}")
        
        conn.commit()
        cur.close()
        conn.close()
        print("Database structure imported successfully.")
    except Exception as e:
        print(f"Error during database setup: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    setup_db()
