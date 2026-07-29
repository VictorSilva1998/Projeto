class Cores:
    FUNDO = "#8e8acc"
    CARTAO = "#dee3f8"
    TEXTO = "#000000"
    TEXTO_SECUNDARIO = "#7e7e7e"
    PLACEHOLDER = "#94aaff"
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
    colaor {Cores.TEXTO}
}}
"""