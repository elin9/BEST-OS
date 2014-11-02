BEGIN TRANSACTION;
CREATE TABLE bookposts(user varchar(50), title varchar(200), author varchar(200), edition varchar(30), ISBN varchar(100), condition varchar(200), otherNotes varchar(2500), courseNumber varchar(30), photo varchar(300), price double);
CREATE TABLE users(username varchar(100), password varchar(100), email varchar(100), sessionID varchar(100));
INSERT INTO "users" VALUES('ok','ok','ok','6ac8ace5-dc24-4c81-b2b1-a65428439e35');
INSERT INTO "users" VALUES('a','b','c','0');
INSERT INTO "users" VALUES('z','y','x','0');
COMMIT;
