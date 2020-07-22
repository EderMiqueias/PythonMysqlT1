CREATE DATABASE testePythonMysql;

USE testePythonMysql;

CREATE TABLE cidades (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    cep VARCHAR(8) NOT NULL
);

CREATE TABLE pessoas (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    idade INT NOT NULL,
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidades(id)
);

INSERT INTO cidades (nome, cep) VALUES ('manaira', '58995000');
INSERT INTO pessoas (nome, idade, id_cidade) VALUES ('slim', 19, 1);
