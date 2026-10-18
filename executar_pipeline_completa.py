"""
Orquestrador Geral da Pipeline KDD - PNS 2019
Executa sequencialmente e de forma auditada as 4 etapas metodológicas:
  1. Análise Descritiva e Bivariada (01_analise_descritiva.py)
  2. Detecção e Tratamento de Outliers / Winsorização (02_tratamento_outliers.py)
  3. Tratamento de Dados Ausentes e Pulos de Questionário (03_tratamento_dados_ausentes.py)
  4. Teoria da Informação de Shannon e Ganho de Informação (04_analise_entropia.py)
"""

import time
import subprocess
import sys

SCRIPTS = [
    ("Etapa 1: Análise Exploratória e Descritiva", "01_analise_descritiva.py"),
    ("Etapa 2: Tratamento de Outliers e Winsorização", "02_tratamento_outliers.py"),
    ("Etapa 3: Tratamento de Ausentes e Pulos de Questionário", "03_tratamento_dados_ausentes.py"),
    ("Etapa 4: Teoria da Informação e Ganho de Informação", "04_analise_entropia.py")
]

def main():
    print("=" * 85)
    print(" PIPELINE DE KDD E EPIDEMIOLOGIA COMPUTACIONAL - MICRODADOS DA PNS 2019 (IBGE)")
    print(" ESTUDO DE FATORES DE RISCO ASSOCIADOS A DOENÇAS CARDIOVASCULARES (Q06306)")
    print("=" * 85)
    
    t_start_total = time.time()
    
    for idx, (nome, script) in enumerate(SCRIPTS, start=1):
        print(f"\n>>> INICIANDO [{idx}/4]: {nome} ({script})...")
        t_start = time.time()
        
        result = subprocess.run([sys.executable, script])
        
        if result.returncode != 0:
            print(f"\n❌ ERRO na execução do script {script}. Pipeline abortada.")
            sys.exit(result.returncode)
            
        t_elapsed = time.time() - t_start
        print(f"✔ CONCLUÍDO [{idx}/4] em {t_elapsed:.1f} segundos.")

    t_total = time.time() - t_start_total
    print("\n" + "=" * 85)
    print(f"🎉 PIPELINE COMPLETA EXECUTADA COM SUCESSO EM {t_total:.1f} SEGUNDOS!")
    print("   Todos os arquivos CSV intermediários, relatórios .docx e gráficos 300 DPI")
    print("   encontram-se disponíveis na pasta './output'.")
    print("=" * 85)

if __name__ == '__main__':
    main()
