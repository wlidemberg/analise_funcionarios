import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Lê o arquivo csv
try:
    df = pd.read_csv('funcionarios.csv', encoding='utf-8', sep=';')
except UnicodeDecodeError:
    df = pd.read_csv('funcionarios.csv', encoding='cp1252', sep=';') 

# Padronizar colinas
df.columns = df.columns.str.strip().str.lower() 

# Converte datas
data_admissao = pd.to_datetime(df['data_admissao'], dayfirst=True)

# Mostra todos os dados
print('======  Lista de Funcionarios ======')
print(df, '\n\n')

quantidade_funcionarios = len(df)
print(f"Quantidade de funcionarios: {quantidade_funcionarios}.")

#Média Salarial
media_salario = df['salario'].mean()
print(f"Media Salarial Geral: R$ {media_salario:.2f}")

# Maior e Menor Salário
maior_salario = df['salario'].max()
menor_salario = df['salario'].min()
print(f" O maior Salário: R$ {maior_salario:.2f} - Menor Salário: R$ {menor_salario:.2f}")

# Funcionário mais antigo
# data_admissao = pd.to_datetime(df['Data_admissao'], dayfirst=True)# Transforma em datas
mais_antigo = df.loc[data_admissao.idxmin()]
print(f" O funcionario mais antigo: {mais_antigo['nome']} admitido em : {mais_antigo['data_admissao']}")

# Distribuição por setor
print('\n====== Funcionários por setor ======')
func_to_setor = df['setor'].value_counts()
print(func_to_setor)

# Gerar Relatório.txt
with open("relatorio_funcionarios.txt", 'w', encoding="utf-8") as arquivo:
    arquivo.write("========== Relatório de Funcionários ==========\n\n")

    arquivo.write("📋 Lista de Funcionários:\n")
    arquivo.write(df.to_string(index=False))
    arquivo.write('\n\n')

    arquivo.write(f"Quantidade de funcionários: {quantidade_funcionarios}\n")
    arquivo.write(f"Média Salarial Geral: R$ {media_salario:.2f}\n")
    arquivo.write(f"Maior Salário: R$ {maior_salario:.2f}\n")
    arquivo.write(f"Menor Salário: R$ {menor_salario:.2f}\n")
    arquivo.write(f"Funcionário mais antigo: {mais_antigo['nome']} - admitido em {mais_antigo['data_admissao']}\n")
    arquivo.write(f"Funcionários por setor:\n")
    arquivo.write(func_to_setor.to_string())
print("Relatório Gerado com Sucesso!")    