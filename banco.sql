-- Execute na instância DB com o administrador do MySQL.
-- Não apaga bancos nem tabelas existentes.
CREATE DATABASE IF NOT EXISTS atividade4 CHARACTER SET utf8mb4;
USE atividade4;

CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL
);
