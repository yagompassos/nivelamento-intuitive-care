-- ----------------(Primeiro SCRIPT) ------------------
-- Script DDL para criação das tabelas 
-- Autor: Yago Passos
-- base de dados: ANS_DB

-- não é possivel fazer o download de arquivos na web através de scripts .sql puro.
-- por isso, o arquivo já foi baixado e está no diretório /scripts_sql

CREATE DATABASE
    IF NOT EXISTS ANS_DB;
    
USE ANS_DB;


CREATE TABLE OPERADORA (
    REGISTRO_OPERADORA VARCHAR(6) PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL,
    Razao_Social VARCHAR(140) NOT NULL,
    Nome_Fantasia VARCHAR(140),
    Modalidade VARCHAR(2),
    Logradouro VARCHAR(40),
    Numero VARCHAR(20),
    Complemento VARCHAR(40),
    Bairro VARCHAR(30),
    Cidade VARCHAR(30),
    UF CHAR(2),
    CEP VARCHAR(8),
    DDD VARCHAR(4),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(50),
    Cargo_Representante VARCHAR(40),
    Regiao_de_Comercializacao INT CHECK (Regiao_de_Comercializacao BETWEEN 1 AND 6),
    Data_Registro_ANS DATE
);
