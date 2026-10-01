class MeuBotao extends HTMLElement {
    connectedCallback() {
        const texto = this.innerHTML ||
        "clique aqui";

        this.innerHTML = `<button class="btn-customizado">${texto}</button>`;
    }
}

customElements.define("meu-botao", MeuBotao);