BEGIN TRANSACTION;
CREATE TABLE notes (autor TEXT, note TEXT);
INSERT INTO "notes" VALUES('Alice','This is a note.');
INSERT INTO "notes" VALUES('Bob','Another note.');
COMMIT;
