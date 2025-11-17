programa {
  funcao inicio() {
    inteiro produto, venda
    escreva("Digite a quantia de produtos que há no estoque: ")
    leia(produto)
    enquanto(produto >0){
    escreva("Digite a quantia de produtos vendidos: ")
    leia(venda)
    se(venda>0)
      produto -= venda
    senao
      escreva("Valor negativo inserido, digite outro.","\n")
    }
    escreva("EStoque esgotado. Vendas encerradas.")
  }
}
