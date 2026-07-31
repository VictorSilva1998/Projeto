class Cores:
    FUNDO = "#8e8acc"
    CARTAO = "#dee3f8"
    TEXTO = "#000000"
    TEXTO_SECUNDARIO = "#7e7e7e"
    PLACEHOLDER = "#4264f0"
    BORDA = "#5d6796"
    PRIMARIA = "#2448d4"
    PRIMARIA_HOVER = "#353d5c"
    PRIMARIA_PRESSED = "#3b56C2"

ESTILO = f"""
QWidget#Janela{{
    background-color: {Cores.FUNDO}
}}
QFrame#Formulario {{
    background-color: {Cores.CARTAO}
}}
QLabel#Titulo {{
    font-size: 22px;
    font-weight: bold;
    color {Cores.TEXTO}
}}
QLabel#Subtitulo {{
    font-size: 18px;
    font-weight: normal;
    color {Cores.TEXTO_SECUNDARIO}
}}
"""