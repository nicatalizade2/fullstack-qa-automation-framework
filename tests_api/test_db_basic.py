def test_create_and_read_user(db):

    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)


    db.execute("INSERT INTO users (name) VALUES ('Nico');")


    rows = db.fetch("SELECT name FROM users WHERE name='Nico';")

    assert rows[0][0] == 'Nico'
