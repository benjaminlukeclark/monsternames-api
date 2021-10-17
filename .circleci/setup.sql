CREATE DATABASE development;
CREATE USER 'dev'@'%' IDENTIFIED WITH mysql_native_password BY 'helloWorld!1';
GRANT ALL ON development.* TO 'dev'@'%';