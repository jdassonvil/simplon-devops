CREATE TABLE users(
  id uuid DEFAULT uuid_generate_v4(),
  username TEXT,
  email TEXT
);
