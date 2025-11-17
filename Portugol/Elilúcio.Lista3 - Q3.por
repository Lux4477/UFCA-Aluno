programa {
  inclua biblioteca Tipos
  inclua biblioteca Texto
  funcao inicio() {
    cadeia a,lista
    leia(a)
    lista = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    se(Texto.numero_caracteres(a) > 1){
      escreva("Texto inválido, escreva apenas um caractere")
    }senao se(Tipos.cadeia_e_inteiro(a,10) == verdadeiro){
      escreva("O caractere digitado é um número")
    }senao se(Texto.posicao_texto( a, lista, 0) < 26){
      escreva("o caractere digitado é minúsculo")
    }senao se(Texto.posicao_texto(a, lista, 0) >= 26){
      escreva("o caractere digitado é maiúsculo")
    }senao se(Texto.posicao_texto( ";", a, 0) == 0){
      escreva("O caractere digitado já deu muita raiva a programadores")
    }senao se(Texto.posicao_texto( " ",  a,  0) == 0){
      escreva("O caractere digitado é a barra de espaço")
    }senao escreva("O caractere digitado é um caractere especial ou não reconhecido pelo programa")
    }
  }
