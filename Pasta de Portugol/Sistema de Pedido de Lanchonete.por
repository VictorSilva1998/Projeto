programa {
  funcao inicio() 
  {
    real sanduiche,refrigerante,sobremesa,quantidade1,quantidade2,quantidade3,total,sanduiche_total,refrigerante_total,sobremesa_total,itens_total,cliente,troco
    
    sanduiche=12.5
    refrigerante=6
    sobremesa=8.75

    escreva ("Digite a quantidade de sanduíches desejados= ")
    leia (quantidade1)
    escreva ("Digite a quantidade de refrigerantes desejados= ")
    leia (quantidade2)
    escreva ("Digite a quantidade de sobremesas desejadas= ")
    leia (quantidade3)
    escreva ("Digite o valor pago pelo cliente em dinheiro= R$ ")
    leia (cliente)

    sanduiche_total=quantidade1*sanduiche
    refrigerante_total=quantidade2*refrigerante
    sobremesa_total=quantidade3*sobremesa
    total=sanduiche_total+refrigerante_total+sobremesa_total
    itens_total=quantidade1+quantidade2+quantidade3
    troco=cliente-total
    
    escreva ("Quantidade de sanduíches: ",quantidade1)
    escreva ("\nQuantidade de refrigerantes: ",quantidade2)
    escreva ("\nQuantidade de sobremesas: ",quantidade3)
    escreva ("\nValor pago pelo cliente: R$ ",cliente,"\n")
    escreva ("\nValor total gasto em sanduíches: R$ ",sanduiche_total)
    escreva ("\nValor total gasto em refrigerantes: R$ ",refrigerante_total)
    escreva ("\nValor total gasto em sobremesas: R$ ",sobremesa_total,"\n")
    escreva ("\nQuantidade total de itens comprados: ",itens_total)
    escreva ("\nValor total do pedido: R$ ",total,"\n")
    escreva ("\nValor do troco a ser devolvido ao cliente: R$ ",troco,"\n")
    escreva ("\n======== Resumo da Compra ========\n")
    escreva ("\nQuantidade de cada item:\n")
    escreva ("  Sanduíches= ",quantidade1,"\n")
    escreva ("  Refrigerantes= ",quantidade2,"\n")
    escreva ("  Sobremesas= ",quantidade3,"\n")
    escreva ("\nValor total gasto em cada categoria:\n")
    escreva ("  Sanduíches= R$ ",sanduiche_total,"\n")
    escreva ("  Refrigerantes= R$ ",refrigerante_total,"\n")
    escreva ("  Sobremesas= R$ ",sobremesa_total,"\n")
    escreva ("\nQuantidade total de itens comprados: ",itens_total,"\n")
    escreva ("\nValor total da compra: R$ ",total,"\n")
    escreva ("\nValor pago pelo cliente: R$ ",cliente,"\n")
    escreva ("\nValor do troco: R$ ",troco)
  }
}
