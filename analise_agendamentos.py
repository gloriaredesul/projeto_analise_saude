import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Configurações visuais e funcionais
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)

print("🔍 Análise de Faltas em Agendamentos Médicos - Versão Profissional\n")

# Carregar os dados do Excel
df = pd.read_excel('agendamentos.xlsx')

# Pré-processamento
df['data_agendamento'] = pd.to_datetime(df['data_agendamento'])
df['faltou'] = df['compareceu'].apply(lambda x: 0 if str(x).strip().lower() == 'sim' else 1)

# 1. Resumo geral
total_agendamentos = df.shape[0]
total_faltas = df['faltou'].sum()
taxa_faltas = (total_faltas / total_agendamentos) * 100

print(f"📅 Total de agendamentos: {total_agendamentos}")
print(f"❌ Total de faltas: {total_faltas}")
print(f"⚠️ Taxa de faltas geral: {taxa_faltas:.2f}%\n")

# 2. Faltas por bairro
faltas_por_bairro = df.groupby('bairro')['faltou'].mean().sort_values(ascending=False)
print("📍 Taxa de faltas por bairro:")
print(faltas_por_bairro)

# Salvar em CSV para relatórios
faltas_por_bairro.to_csv('output_faltas_bairro.csv')

# 3. Idade média dos pacientes que faltam
media_idade_faltantes = df[df['faltou'] == 1]['idade'].mean()
print(f"\n📈 Idade média de quem faltou: {media_idade_faltantes:.1f} anos")

# 4. Visualização: gráfico de faltas por bairro
plt.figure(figsize=(10, 5))
sns.barplot(x=faltas_por_bairro.index, y=faltas_por_bairro.values, palette='crest')
plt.title('Taxa de Faltas por Bairro - Clínica Saúde Ativa')
plt.ylabel('Taxa de Faltas (%)')
plt.xlabel('Bairro')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar gráfico
plt.savefig('grafico_faltas_bairro.png')
plt.show()

# 5. Sugestão baseada nos dados
print("\n💡 Recomendações:")
print("- Enviar lembretes por WhatsApp/SMS para bairros com maior taxa de ausência.")
print("- Criar ações educativas para o público acima de 45 anos.")
print("- Monitorar taxa mensalmente para avaliar melhorias.")
print("\n✅ Relatórios salvos em: output_faltas_bairro.csv e grafico_faltas_bairro.png")
