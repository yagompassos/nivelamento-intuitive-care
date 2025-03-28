-- ----------------(Terceiro SCRIPT) ------------------
-- Script DML Para obtenção de dados sobre as operadoras 
-- Autor: Yago Passos
-- base de dados: 

SELECT 
    o.Nome_Fantasia, 
    SUM(d.Valor_Despesas) AS Total_Despesas
FROM despesas d
JOIN operadoras o ON d.REGISTRO_OPERADORA = o.REGISTRO_OPERADORA
WHERE d.Categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND d.Data_Registro >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY o.Nome_Fantasia
ORDER BY Total_Despesas DESC
LIMIT 10;

SELECT 
    o.Nome_Fantasia, 
    SUM(d.Valor_Despesas) AS Total_Despesas
FROM despesas d
JOIN operadoras o ON d.REGISTRO_OPERADORA = o.REGISTRO_OPERADORA
WHERE d.Categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND d.Data_Registro >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY o.Nome_Fantasia
ORDER BY Total_Despesas DESC
LIMIT 10;
