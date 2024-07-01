import psycopg2

class DatabaseConnector:
    def __init__(self, dbname, user, password, host, port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            
        except Exception as e:
            pass

    def create_table(self):
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                tg_id BIGINT NOT NULL,
                full_name TEXT DEFAULT '',
                tokens BIGINT DEFAULT 0,
                max_tokens BIGINT DEFAULT 0,
                befor_location TEXT DEFAULT '',
                claim_time TIMESTAMPTZ,
                km FLOAT
        );
        ''')

    def create_table_robots(self):
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS robots (
                id SERIAL PRIMARY KEY,
                tg_id BIGINT NOT NULL,
                wood BIGINT DEFAULT 0,
                stone BIGINT DEFAULT 0,
                bronze BIGINT DEFAULT 0,
                silver BIGINT DEFAULT 0,
                gold BIGINT DEFAULT 0,
                platinum BIGINT DEFAULT 0,
                diamond BIGINT DEFAULT 0,
                frendly BIGINT DEFAULT 0);
        ''')

    def create_table_robRewards(self):
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS robotRewards (
                id SERIAL PRIMARY KEY,
                tg_id BIGINT NOT NULL,
                claim_time TIMESTAMPTZ,
                earn BIGINT DEFAULT 0);
        ''')


    def create_table_referral(self):
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id SERIAL PRIMARY KEY,
                tg_id BIGINT NOT NULL,
                who BIGINT default 0,
                whom TEXT NOT NULL);
        ''')

    def user_exists_referral(self, tg_id : int):
        with self.connection:
            self.cursor.execute(
                "SELECT * FROM referrals WHERE tg_id = %s", (tg_id,))
            return bool(self.cursor.fetchall())
        

    def add_user_referral(self, tg_id, who=0, whom=''):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO referrals (tg_id, who, whom) VALUES ({tg_id}, {who}, '{whom}')")

    def plus_whom(self, tg_id, whom):
        with self.connection:
            return self.cursor.execute(
                f"UPDATE referrals SET whom = whom || ' {whom}' WHERE tg_id = {tg_id}")

    def user_exists_robReward(self, tg_id : int):
        with self.connection:
            self.cursor.execute(
                "SELECT * FROM robotRewards WHERE tg_id = %s", (tg_id,))
            return bool(self.cursor.fetchall())
        
    def add_user_robReward(self, tg_id):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO robotRewards (tg_id) VALUES ({tg_id})")

    def user_exists_rob(self, tg_id : int):
        with self.connection:
            self.cursor.execute(
                "SELECT * FROM robots WHERE tg_id = %s", (tg_id,))
            return bool(self.cursor.fetchall())
        
    def add_user_rob(self, tg_id):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO robots (tg_id) VALUES ({tg_id})")

    def drop_table(self):
        with self.connection:
            return self.cursor.execute('''
            DROP TABLE IF EXISTS users;
            ''')

    def user_exists(self, tg_id : int):
        with self.connection:
            self.cursor.execute(
                "SELECT * FROM users WHERE tg_id = %s", (tg_id,))
            return bool(self.cursor.fetchall())
        
    def add_user(self, tg_id, full_name):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO users (tg_id, tokens, km, full_name) VALUES ({tg_id}, 0, 0, '{full_name}')")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed.")

db = DatabaseConnector(
        dbname="main",
        user="anonim",
        password="112233qq",
        host="127.0.0.1",
        port=5432 
    )


db.create_table()
db.create_table_robots()
db.create_table_robRewards()
db.create_table_referral()
