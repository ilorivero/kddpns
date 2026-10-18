"""
Módulo de Estilização e Geração de Relatórios Acadêmicos em Word (.docx)
Pipeline de KDD e Epidemiologia Computacional - PNS 2019
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Paleta de Cores Acadêmica
COLOR_PRIMARY = RGBColor(27, 54, 93)      # Azul Marinho Profundo (#1B365D)
COLOR_SECONDARY = RGBColor(46, 91, 136)   # AzulArdósia (#2E5B88)
COLOR_TEXT = RGBColor(33, 37, 41)         # Chumbo Quase Preto (#212529)
COLOR_MUTED = RGBColor(108, 117, 125)     # Cinza Neutro (#6C757D)
COLOR_HIGHLIGHT = RGBColor(166, 43, 43)   # Carmim (#A62B2B)

HEX_HEADER_BG = "1B365D"
HEX_ZEBRA_BG = "F4F6F9"
HEX_WHITE_BG = "FFFFFF"
HEX_BORDER = "D0D5DD"
HEX_CALLOUT_BG = "EBF3FA"
HEX_CALLOUT_BORDER = "2E5B88"


def set_cell_background(cell, hex_color: str):
    """Aplica cor de fundo a uma célula de tabela docx."""
    tcPr = cell._tc.get_or_add_tcPr()
    # Remove existing shading if present
    for child in list(tcPr):
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    shd_xml = f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'
    tcPr.append(parse_xml(shd_xml))


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Define margens internas (padding) de uma célula em twips (1/20 de ponto)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)


def create_base_document() -> docx.Document:
    """Cria e configura o documento base no padrão A4 com margens ABNT/Acadêmicas."""
    doc = docx.Document()
    
    # Configuração de Página: A4, Margens 2.5 cm (superior, inferior, esquerda, direita)
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.98)     # ~2.5 cm
        section.bottom_margin = Inches(0.98)  # ~2.5 cm
        section.left_margin = Inches(0.98)    # ~2.5 cm
        section.right_margin = Inches(0.98)   # ~2.5 cm
        
        # Cabeçalho e Rodapé discretos
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Projeto KDD - Microdados PNS 2019 | Epidemiologia Computacional")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = COLOR_MUTED

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Pesquisa Nacional de Saúde (IBGE) — Análise Focada em Doenças Cardiovasculares")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = COLOR_MUTED

    # Configuração do Estilo Normal
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = COLOR_TEXT
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(6)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    return doc


def add_title_block(doc: docx.Document, title: str, subtitle: str, stage_tag: str):
    """Insere o cabeçalho/bloco de título acadêmico."""
    p_tag = doc.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tag.paragraph_format.space_before = Pt(0)
    p_tag.paragraph_format.space_after = Pt(4)
    rtag = p_tag.add_run(f"RELATÓRIO TÉCNICO-CIENTÍFICO DE MINERAÇÃO DE DADOS • {stage_tag.upper()}")
    rtag.font.name = "Calibri"
    rtag.font.size = Pt(9.5)
    rtag.font.bold = True
    rtag.font.color.rgb = COLOR_SECONDARY

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(6)
    rtitle = p_title.add_run(title)
    rtitle.font.name = "Calibri"
    rtitle.font.size = Pt(20)
    rtitle.font.bold = True
    rtitle.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    rsub = p_sub.add_run(subtitle)
    rsub.font.name = "Calibri"
    rsub.font.size = Pt(12)
    rsub.font.italic = True
    rsub.font.color.rgb = COLOR_MUTED

    # Linha divisória horizontal sutil
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(14)
    p_div_border = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="{HEX_HEADER_BG}"/></w:pBdr>')
    p_div._p.get_or_add_pPr().append(p_div_border)


def add_heading_1(doc: docx.Document, text: str):
    """Insere Heading 1 estilizado."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p


def add_heading_2(doc: docx.Document, text: str):
    """Insere Heading 2 estilizado."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p


def add_heading_3(doc: docx.Document, text: str):
    """Insere Heading 3 estilizado."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = COLOR_TEXT
    return p


def add_callout(doc: docx.Document, text: str, title: str = "Nota Metodológica"):
    """Insere uma caixa de destaque (callout) com borda lateral elegante."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    # Borda esquerda grossa e outras sem borda
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_CALLOUT_BORDER}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)
    
    rtitle = p.add_run(f"📌 {title}: ")
    rtitle.font.name = "Calibri"
    rtitle.font.size = Pt(10.5)
    rtitle.font.bold = True
    rtitle.font.color.rgb = COLOR_SECONDARY
    
    rtext = p.add_run(text)
    rtext.font.name = "Calibri"
    rtext.font.size = Pt(10)
    rtext.font.color.rgb = COLOR_TEXT
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)


def add_styled_table(doc: docx.Document, df, caption: str, max_rows: int = 50, col_widths=None):
    """
    Insere uma tabela estilizada com cabeçalho azul-marinho, linhas zebradas e tipografia precisa.
    """
    # Adiciona legenda da tabela
    p_cap = doc.add_paragraph()
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(3)
    p_cap.paragraph_format.keep_with_next = True
    rcap = p_cap.add_run(f"Tabela: {caption}")
    rcap.font.name = "Calibri"
    rcap.font.size = Pt(10)
    rcap.font.bold = True
    rcap.font.color.rgb = COLOR_PRIMARY

    # Converte dataframe se necessário
    data_to_show = df.head(max_rows) if len(df) > max_rows else df
    
    table = doc.add_table(rows=len(data_to_show) + 1, cols=len(df.columns))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Configuração de bordas sutis na tabela inteira
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{HEX_BORDER}"/>'
        f'<w:bottom w:val="single" w:sz="10" w:space="0" w:color="{HEX_HEADER_BG}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

    # Cabeçalho
    hdr_cells = table.rows[0].cells
    for col_idx, col_name in enumerate(df.columns):
        cell = hdr_cells[col_idx]
        set_cell_background(cell, HEX_HEADER_BG)
        set_cell_margins(cell, top=120, bottom=120, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(str(col_name))
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    # Linhas de Dados
    for row_idx, row_values in enumerate(data_to_show.values):
        row_cells = table.rows[row_idx + 1].cells
        bg_color = HEX_ZEBRA_BG if row_idx % 2 == 1 else HEX_WHITE_BG
        for col_idx, val in enumerate(row_values):
            cell = row_cells[col_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            
            # Formatação de texto vs números
            val_str = ""
            if val is None or (isinstance(val, float) and str(val) == 'nan'):
                val_str = "-"
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif isinstance(val, (int, float)):
                if isinstance(val, int) or val == int(val):
                    val_str = f"{int(val):,}".replace(",", ".")
                else:
                    val_str = f"{val:.4f}".rstrip('0').rstrip('.') if abs(val) < 0.001 else f"{val:.3f}"
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            else:
                val_str = str(val)
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT

            run = p.add_run(val_str)
            run.font.name = "Calibri"
            run.font.size = Pt(9)
            run.font.color.rgb = COLOR_TEXT

    # Ajuste opcional de larguras
    if col_widths and len(col_widths) == len(df.columns):
        for row in table.rows:
            for idx, w in enumerate(col_widths):
                row.cells[idx].width = Inches(w)

    # Espaço após a tabela
    p_post = doc.add_paragraph()
    p_post.paragraph_format.space_before = Pt(2)
    p_post.paragraph_format.space_after = Pt(10)
    if len(df) > max_rows:
        r_note = p_post.add_run(f"Nota: Tabela truncada para visualização (exibindo {max_rows} de {len(df)} registros).")
        r_note.font.size = Pt(8.5)
        r_note.font.italic = True
        r_note.font.color.rgb = COLOR_MUTED


def add_figure_with_caption(doc: docx.Document, image_path: str, caption: str, width_in_inches: float = 6.2):
    """
    Insere uma imagem em alta resolução centrada com legenda e nota interpretativa.
    """
    if not os.path.exists(image_path):
        p_err = doc.add_paragraph(f"[Erro: Imagem não encontrada no caminho '{image_path}']")
        p_err.runs[0].font.color.rgb = COLOR_HIGHLIGHT
        return

    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(image_path, width=Inches(width_in_inches))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(12)
    rcap = p_cap.add_run(f"Figura: {caption}")
    rcap.font.name = "Calibri"
    rcap.font.size = Pt(9.5)
    rcap.font.bold = True
    rcap.font.color.rgb = COLOR_PRIMARY
