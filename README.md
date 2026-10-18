# Pipeline de KDD e Epidemiologia Computacional — Microdados da PNS 2019

## Estudo de Fatores de Risco e Doenças Cardiovasculares na População Brasileira
**Variável-Alvo:** `Q06306` (*Diagnóstico Médico de Doença do Coração: 1 = Sim / Cardiopata, 2 = Não / Saudável*)

---

## 🏛️ Arquitetura da Pipeline Modular (4 Etapas KDD)

A pipeline é composta por 4 scripts Python independentes e encadeados, gerando em cada fase o dataset intermediário correspondente, gráficos em alta resolução (300 DPI) e relatórios técnico-científicos formatados em Microsoft Word (`.docx`).

```
pns2019.csv (Microdados Brutos) ──► Deve estar na pasta raiz deste código
    │
    ▼
[01_analise_descritiva.py] ──────► output/pns_etapa1_descritiva.csv + output/relatorio_etapa1.docx
    │
    ▼
[02_tratamento_outliers.py] ─────► output/pns_etapa2_outliers.csv   + output/relatorio_etapa2.docx
    │
    ▼
[03_tratamento_dados_ausentes.py] ► output/pns_etapa3_sem_nulos.csv  + output/relatorio_etapa3.docx
    │
    ▼
[04_analise_entropia.py] ────────► output/pns_etapa4_entropia.csv   + output/relatorio_etapa4.docx
```

---

## 📋 Conjunto das 44 Variáveis Selecionadas da PNS 2019

| Domínio | Variáveis | Descrição Resumida |
| :--- | :--- | :--- |
| **Alimentação** (13) | `P006`, `P00620`, `P00901`, `P01101`, `P01301`, `P01501`, `P01801`, `P02001`, `P023`, `P02401`, `P02501`, `P02601`, `P02602` | Consumo semanal de feijão, hortaliças cruas/cozidas, carnes, peixes, sucos naturais, açúcares de adição, refrigerantes e doces. |
| **Antropometria** (4) | `P00104`, `P00404`, `W00101`, `W00201` | Peso corporal (kg), Altura (cm), Perímetro da cintura (cm) e Perímetro do quadril (cm). |
| **Tabagismo** (11) | `P050`, `P05101`, `P052`, `P053`, `P05401`, `P05402`, `P058`, `P05901`, `P06701`, `P068`, `M01001` | Frequência de fumo atual, histórico de fumo diário, quantidade de cigarros, idade de início, uso de cigarro de palha, tempo de cessação e fumo passivo. |
| **Consumo de Álcool** (4) | `P027`, `P02801`, `P029`, `P03201` | Frequência de ingestão alcoólica, dias de consumo na semana, doses típicas consumidas e episódios de consumo pesado (*binge drinking*). |
| **Atividade Física** (9) | `P034`, `P035`, `P036`, `P03701`, `P03901`, `P040`, `P042`, `P04501`, `P04502` | Esforço físico ocupacional, deslocamento ativo a pé/bicicleta, prática esportiva no lazer, caminhadas e tempo de telas (TV, computador, tablet). |
| **Saúde Mental** (3) | `N001`, `N010`, `N016` | Autoavaliação do estado geral de saúde, distúrbios de sono e sintomas depressivos/anedonia nas últimas duas semanas. |
| **Variável-Alvo** (1) | `Q06306` | Diagnóstico prévio de Doença Crônica do Coração (1 = Cardiopata, 2 = Saudável). |

---

## 🔬 Detalhamento Metodológico das Etapas

### Etapa 1: `01_analise_descritiva.py`
- Filtra a coorte de moradores selecionados com resposta válida ao diagnóstico cardíaco (90.846 indivíduos: 4.732 cardiopatas [5,21%] e 86.114 saudáveis [94,79%]).
- Análise univariada completa (Média, Desvio Padrão, Mediana, Mínimo, Máximo, IQR e contagens) para todas as 44 variáveis.
- Análise bivariada rigorosa:
  - Teste t de Student (Welch) e Teste U de Mann-Whitney para atributos contínuos.
  - Teste Qui-Quadrado de Independência (\\(\chi^2\\)) e V de Cramér para atributos categóricos.
- Gráficos gerados (300 DPI):
  - `etapa1_fig1_imc_antropometria_ecdf.png`: Densidade (KDE) e Curva de Frequência Acumulada Empírica (ECDF) com marcação de pontos de inflexão de aceleração do risco antropométrico.
  - `etapa1_fig2_boxplots_antropometria.png`: Boxplots pareados de IMC, peso, cintura e idade de início do tabagismo.
  - `etapa1_fig3_habitos_bivariada_acumulada.png`: Proporções e curvas acumuladas de vulnerabilidade (N001, P050, P03901, P027).

### Etapa 2: `02_tratamento_outliers.py`
- Discussão ético-epidemiológica: evita o descarte de registros (*listwise deletion*), que geraria grave viés de seleção ao excluir pacientes mais graves da amostra.
- Aplicação de limites estatísticos de Tukey por IQR: \\([Q_1 - 1,5 \times IQR, \quad Q_3 + 1,5 \times IQR]\\).
- Cruzamento com barreiras de sanidade biológica/fisiológica da OMS/SBC (Peso: [30, 220] kg; Altura: [120, 220] cm; Cintura: [40, 180] cm; Quadril: [50, 220] cm).
- **Winsorização (*Capping*)**: Truncamento de valores que excedem os limites, preservando 100% dos 90.846 registros na coorte.
- Gráficos gerados (300 DPI):
  - `etapa2_fig1_boxplots_antes_depois.png`: Boxplots comparativos Antes vs. Depois.
  - `etapa2_fig2_ecdf_inflexao_antes_depois.png`: Curvas ECDF destacando os pontos de corte de Capping.
  - `etapa2_fig3_kde_densidade_antes_depois.png`: Densidades KDE comprovando estabilização das caudas longas.

### Etapa 3: `03_tratamento_dados_ausentes.py`
- Fundamentação teórica dos mecanismos de Rubin (1976): MCAR, MAR e NMAR.
- **Passo 1 (Lógica de Pulos Estruturais - *Skip Patterns*)**: Atribuição determinística do valor `0` a indivíduos não expostos (não-fumantes `P050=3` têm perguntas de cigarros zeradas; abstêmios `P027=3` têm consumo de álcool zerado; indivíduos sem esforço físico têm dias zerados).
- **Passo 2 (Imputação por Tendência Central Estratificada por Classe)**:
  - Variáveis contínuas/discretas: Mediana da subpopulação específica (Cardiopata `Q06306=1` vs. Saudável `Q06306=2`).
  - Variáveis categóricas/ordinais: Moda da subpopulação específica.
- Verificação assertiva de auditoria: base final com **exatamente 0% de dados ausentes**.
- Gráficos gerados (300 DPI):
  - `etapa3_fig1_diagnostico_nulos_modulo.png`: Percentual de nulos por módulo.
  - `etapa3_fig2_pareto_inflexao_nulos.png`: Diagrama de Pareto com curva acumulada e ponto de inflexão de ausência estrutural.
  - `etapa3_fig3_antes_depois_imputacao.png`: Comparativo demonstrando 0,00% de nulos em todas as variáveis.

### Etapa 4: `04_analise_entropia.py`
- Fundamentação na Teoria da Informação de Claude Shannon (1948):
  - Entropia de Shannon: \\(H(X) = - \sum P(x) \log_2 P(x)\\)
  - Entropia Máxima: \\(H_{max} = \log_2(k)\\)
  - Entropia Normalizada: \\(H_{norm}(X) = H(X) / \log_2(k) \in [0, 1]\\)
  - Entropia Condicional: \\(H(Y|X)\\)
  - Ganho de Informação / Informação Mútua: \\(IG(Y, X) = H(Y) - H(Y|X)\\)
  - Razão de Ganho de Informação (*Gain Ratio*): \\(GR(Y, X) = IG(Y, X) / H(X)\\)
- Discretização de variáveis contínuas em decis (\\(k=10\\) quantis de frequência).
- Ranqueamento integral das 44 variáveis de acordo com o Ganho de Informação em relação ao diagnóstico cardíaco.
- Gráficos gerados (300 DPI):
  - `etapa4_fig1_ranking_ganho_informacao.png`: Gráfico horizontal de barras com o ranking das 44 variáveis colorido por domínio.
  - `etapa4_fig2_curva_ig_acumulado_inflexao.png`: Curva acumulada de Pareto de Informação Mútua com ponto de inflexão analítico (cotovelo/joelho da curva), indicando o subconjunto ideal de variáveis para modelos preditivos.
  - `etapa4_fig3_heatmap_matriz_informacional.png`: Heatmap de dependência não-linear de Spearman das top 15 variáveis.

---

## 🚀 Como Executar

### Execução Individual de Qualquer Etapa:
```bash
python 01_analise_descritiva.py
python 02_tratamento_outliers.py
python 03_tratamento_dados_ausentes.py
python 04_analise_entropia.py
```

### Execução Automatizada da Pipeline Completa:
```bash
python executar_pipeline_completa.py
```

---

## 📁 Estrutura de Arquivos Gerados na Pasta `./output`

- `pns_etapa1_descritiva.csv` (Base com coorte filtrada de 90.846 indivíduos e 45 atributos canônicos)
- `relatorio_etapa1.docx` (Relatório acadêmico da Etapa 1 com tabelas e gráficos embutidos)
- `pns_etapa2_outliers.csv` (Base com outliers tratados por Winsorização/Capping)
- `relatorio_etapa2.docx` (Relatório acadêmico da Etapa 2)
- `pns_etapa3_sem_nulos.csv` (Base 100% preenchida com 0% de nulos)
- `relatorio_etapa3.docx` (Relatório acadêmico da Etapa 3)
- `pns_etapa4_entropia.csv` (Tabela com ranking, H(X), H_norm, IG e Gain Ratio das 44 variáveis)
- `relatorio_etapa4.docx` (Relatório acadêmico da Etapa 4)
- 12 Figuras em alta resolução a 300 DPI (`.png`)
