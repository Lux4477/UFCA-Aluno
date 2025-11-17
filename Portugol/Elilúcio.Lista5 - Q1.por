programa {
  inclua biblioteca Texto --> txt
  funcao inicio() {
    cadeia senha

    faca{
      escreva("Digite sua senha: ")
      leia(senha)
    }enquanto(txt.posicao_texto(" ", senha, 0)>=0 ou txt.numero_caracteres(senha)<=6 ou txt.numero_caracteres(senha)>=19)
    escreva("Acesso aprovado")
  }
}
