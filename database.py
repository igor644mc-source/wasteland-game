# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('wasteland_game.db')
    cursor = conn.cursor()
    # Создаем таблицу пользователей, если её еще нет
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            user_id INTEGER PRIMARY KEY,
            hp INTEGER DEFAULT 100,
            water INTEGER DEFAULT 50,
            loot INTEGER DEFAULT 0,
            current_node TEXT DEFAULT 'start'
        )
    ''')
    conn.commit()
    conn.close()

def get_player(user_id):
    conn = sqlite3.connect('wasteland_game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT hp, water, loot, current_node FROM players WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    
    if not row:
        # Если игрока нет в базе, создаем ему новую запись
        cursor.execute('INSERT INTO players (user_id) VALUES (?)', (user_id,))
        conn.commit()
        player = {'hp': 100, 'water': 50, 'loot': 0, 'current_node': 'start'}
    else:
        player = {'hp': row[0], 'water': row[1], 'loot': row[2], 'current_node': row[3]}
    
    conn.close()
    return player

def update_player(user_id, hp, water, loot, current_node):
    conn = sqlite3.connect('wasteland_game.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE players 
        SET hp = ?, water = ?, loot = ?, current_node = ? 
        WHERE user_id = ?
    ''', (hp, water, loot, current_node, user_id))
    conn.commit()
    conn.close()