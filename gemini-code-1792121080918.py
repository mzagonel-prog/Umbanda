import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Controle de Estoque - Terreiro", page_icon="🕯️", layout="wide"
)

st.title("🕯️ Controle de Estoque e Checklist - Terreiro")

# ---------------------------------------------------------
# DADOS INICIAIS DA SUA TABELA
# ---------------------------------------------------------
dados_estoque = [
    # VELAS DE 7 DIAS
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Oxalá",
        "Cor / Detalhe": "Branca",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Ogum",
        "Cor / Detalhe": "Tricolor (Verde/Vermelha/Branca)",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Exu",
        "Cor / Detalhe": "Preta/Vermelha",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Pomba Gira",
        "Cor / Detalhe": "Vermelha/Preta (Vermelho em cima)",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Xangô",
        "Cor / Detalhe": "Marrom",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Oxum",
        "Cor / Detalhe": "Amarela",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Ciganos",
        "Cor / Detalhe": "Toda colorida",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    {
        "Categoria": "Velas de 7 Dias",
        "Item": "Entidades (Geral)",
        "Cor / Detalhe": "Cores variadas",
        "Estoque Atual": 5,
        "Estoque Mínimo": 5,
    },
    # VELAS NORMAIS (PALITO)
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Branca",
        "Cor / Detalhe": "Branca",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Iemanjá",
        "Cor / Detalhe": "Azul claro",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Oxum",
        "Cor / Detalhe": "Amarela",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Iansã",
        "Cor / Detalhe": "Branca em cima / Vermelho embaixo",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Xangô",
        "Cor / Detalhe": "Marrom",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Caboclos/Mata",
        "Cor / Detalhe": "Verde escuro",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Ogum",
        "Cor / Detalhe": "Tricolor (Verde/Branco/Vermelho)",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Cosme",
        "Cor / Detalhe": "Rosa / Azul claro",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Pretos Velhos",
        "Cor / Detalhe": "Branca em cima / Preto embaixo",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Exu",
        "Cor / Detalhe": "Preto em cima / Vermelho embaixo",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    {
        "Categoria": "Velas Normais (Palito)",
        "Item": "Pomba Gira",
        "Cor / Detalhe": "Vermelho em cima / Preto embaixo",
        "Estoque Atual": 10,
        "Estoque Mínimo": 10,
    },
    # DEFUMAÇÃO
    {
        "Categoria": "Defumação",
        "Item": "Ervas Secas",
        "Cor / Detalhe": "Para defumação (500g de cada)",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Defumação",
        "Item": "Carvão",
        "Cor / Detalhe": "Para defumação (3kg)",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    # CANJIRA / BARÁ DA RUA
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Cachaça",
        "Cor / Detalhe": "",
        "Estoque Atual": 2,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Espumante",
        "Cor / Detalhe": "Rosé Moscatel",
        "Estoque Atual": 2,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Azeite de Dendê",
        "Cor / Detalhe": "",
        "Estoque Atual": 2,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Farinha",
        "Cor / Detalhe": "Mandioca (1kg)",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Perfume (P. Gira)",
        "Cor / Detalhe": "Bem doce",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Perfume (Exu)",
        "Cor / Detalhe": "",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Pólvora",
        "Cor / Detalhe": "",
        "Estoque Atual": 3,
        "Estoque Mínimo": 3,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Algodão",
        "Cor / Detalhe": "",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Linha",
        "Cor / Detalhe": "Preta",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Canjira / Bará da Rua",
        "Item": "Linha",
        "Cor / Detalhe": "Vermelha",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    # CIGANOS
    {
        "Categoria": "Ciganos",
        "Item": "Farinha",
        "Cor / Detalhe": "Milho (1kg)",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Ciganos",
        "Item": "Lentilha",
        "Cor / Detalhe": "1kg",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Ciganos",
        "Item": "Perfume",
        "Cor / Detalhe": "Doce (1 frasco 500ml)",
        "Estoque Atual": 1,
        "Estoque Mínimo": 1,
    },
    # BEBIDAS (GERAL E SEGURANÇAS)
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Cerveja Branca",
        "Cor / Detalhe": "Segurança de Ogum (Porta)",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Guaraná",
        "Cor / Detalhe": "Eco do Congá",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Vinho Tinto",
        "Cor / Detalhe": "Doce",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Vinho Tinto",
        "Cor / Detalhe": "Seco",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Cerveja Escura",
        "Cor / Detalhe": "Caracu",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Cerveja Escura",
        "Cor / Detalhe": "Malzbier",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Bebidas (Geral e Seguranças)",
        "Item": "Conhaque",
        "Cor / Detalhe": "Dreher",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    # ITENS GERAIS E CONGÁ
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Perfume/Alfazema",
        "Cor / Detalhe": "Limpeza do chão e Congá",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Pemba",
        "Cor / Detalhe": "Branca",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Banha de Ori",
        "Cor / Detalhe": "Amaci e desenvolvimento",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Isqueiros",
        "Cor / Detalhe": "",
        "Estoque Atual": 0,
        "Estoque Mínimo": 3,
    },
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Cigarros",
        "Cor / Detalhe": "",
        "Estoque Atual": 0,
        "Estoque Mínimo": 2,
    },
    {
        "Categoria": "Itens Gerais e Congá",
        "Item": "Melado",
        "Cor / Detalhe": "",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
    # PAI MALAQUIAS
    {
        "Categoria": "Pai Malaquias",
        "Item": "Linha de costura",
        "Cor / Detalhe": "Preta",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Pai Malaquias",
        "Item": "Linha de costura",
        "Cor / Detalhe": "Branca",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
    {
        "Categoria": "Pai Malaquias",
        "Item": "Azeite de Oliva",
        "Cor / Detalhe": "Virgem (1 frasco pequeno)",
        "Estoque Atual": 0,
        "Estoque Mínimo": 1,
    },
]

df = pd.DataFrame(dados_estoque)

# Navegação entre estoque e afazeres
aba1, aba2 = st.tabs(["📦 Estoque e Checklist", "📋 Afazeres da Semana"])

with aba1:
  # Filtro de Categoria
  categorias = ["Todas"] + list(df["Categoria"].unique())
  cat_selecionada = st.selectbox("Filtrar Seção:", categorias)

  if cat_selecionada != "Todas":
    df_exibicao = df[df["Categoria"] == cat_selecionada].copy()
  else:
    df_exibicao = df.copy()

  # Atualização da coluna "Repor?"
  df_exibicao["Repor?"] = df_exibicao.apply(
      lambda row: "⚠️ SIM"
      if row["Estoque Atual"] < row["Estoque Mínimo"]
      else "✅ OK",
      axis=1,
  )

  # Resumo rápido
  qtd_repor = len(df_exibicao[df_exibicao["Repor?"] == "⚠️ SIM"])
  col1, col2 = st.columns(2)
  col1.metric("Total de Itens Exibidos", len(df_exibicao))
  col2.metric("Itens Críticos para Repor", qtd_repor)

  st.markdown("### ✏️ Edite os valores atuais diretamente na tabela:")

  # Tabela interativa
  df_editado = st.data_editor(
      df_exibicao,
      column_config={
          "Repor?": st.column_config.TextColumn(
              "Repor?", help="Calculado automaticamente", disabled=True
          )
      },
      use_container_width=True,
  )

  # Lista rápida de compra
  itens_repor = df_editado[df_editado["Repor?"] == "⚠️ SIM"]
  if not itens_repor.empty:
    st.warning("🛒 **Lista de Itens que Precisam de Reposição:**")
    for _, row in itens_repor.iterrows():
      st.write(
          f"- **{row['Item']}** ({row['Cor / Detalhe']}) — Atual:"
          f" **{row['Estoque Atual']}** | Mínimo: **{row['Estoque Mínimo']}**"
      )

with aba2:
  st.subheader("📋 Afazeres da Semana")

  tarefas = [
      "Verificar a mala do Destranca (avaliar se faltam itens específicos).",
      (
          "Conversar com o Pai sobre o uso do melado misturado com água no"
          " desenvolvimento."
      ),
      (
          "Checar o calendário: teremos festas ou obrigações próximas que"
          " exijam velas de 7 dias ou bebidas específicas de outras entidades?"
      ),
  ]

  for i, tarefa in enumerate(tarefas):
    st.checkbox(tarefa, key=f"tarefa_{i}")