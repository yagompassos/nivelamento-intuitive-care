-- ----------------(Segundo SCRIPT) ------------------
-- Script para iportação dos dados
-- Autor: Yago Passos
-- base de dados: ANS_DB


USE ANS_DB;

-- Deve-se tirar a opção -secure-file-priv: https://stackoverflow.com/questions/32737478/how-should-i-resolve-secure-file-priv-in-mysql
LOAD DATA INFILE 'Relatorio_cadop.csv'
INTO TABLE OPERADORA
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    REGISTRO_OPERADORA, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, 
    Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, 
    Regiao_de_Comercializacao, Data_Registro_ANS
)
SET Data_Registro_ANS = STR_TO_DATE(Data_Registro_ANS, '%Y-%m-%d');
