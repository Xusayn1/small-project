category = """
           CREATE TABLE IF NOT EXISTS category
           (
               id    BIGSERIAL PRIMARY KEY,
               title VARCHAR(255) NOT NULL UNIQUE
           ) \
           """

books = """
        CREATE TABLE IF NOT EXISTS books
        (
            id          BIGSERIAL PRIMARY KEY,
            category_id BIGINT       REFERENCES category (id) ON DELETE SET NULL,
            name        VARCHAR(255) NOT NULL UNIQUE,
            author      VARCHAR(255),
            note        TEXT,
            status      VARCHAR(32)  NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """
