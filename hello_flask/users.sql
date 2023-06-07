CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	login TEXT UNIQUE NOT NULL CHECK (login != ''),
	password TEXT NOT NULL CHECK (password != ''),
	token TEXT
);