programa {
  inclua biblioteca Matematica --> math
  funcao inicio() {
    inteiro A,B,C,R,S
    escreva("digite um número para o valor de A: ")
    leia(A)
    escreva("digite um número para o valor de B: ")
    leia(B)
    escreva("digite um número para o valor de C: ")
    leia(C)
    R = math.potencia(A + B,2)
    S = math.potencia(B + C,2)
    escreva("o resultado é: ", (R + S) / 2)
  }
}
