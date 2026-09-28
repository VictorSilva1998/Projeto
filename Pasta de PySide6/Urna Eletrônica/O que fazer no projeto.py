# 1. Crie o botão Votar e deixe-o desabilitado

# Substitua este trecho:

# layout.addWidget(self._criar_botao(
#     "2", "Votar", self.votar_clicado
# ))

# por:

# self.botao_votar = self._criar_botao(
#     "2", "Votar", self.votar_clicado
# )

# self.botao_votar.setEnabled(False)

# layout.addWidget(self.botao_votar)

# 2. Crie um método para habilitar a votação

# Adicione à classe TelaMenu:

# def habilitar_votacao(self):
#     self.botao_votar.setEnabled(True)

# 3. Chame esse método após emitir a Zerésima

# Por exemplo:

# def abrir_zeresima(self):

#     # Código que gera/exibe o relatório inicial

#     self.habilitar_votacao()

# ou diretamente:

# def abrir_zeresima(self):

#     # Código da zerésima

#     self.botao_votar.setEnabled(True)
# 4. (Opcional) Altere o visual do botão desabilitado

# Adicione ao seu ESTILO_MENU:

# #menu_botao:disabled {
#     background-color: #d9d9d9;
#     color: #808080;
#     border: 1px solid #b0b0b0;
# }