programa {
  inclua biblioteca Matematica --> math
  funcao inicio() {
    real a , b , c , x
    escreva("digite um valor para ser usado em x na equação: ")
    leia(x)
    a = (2 * math.potencia(x,2) - 3 * math.potencia(x,x + 1)) / 2x
    b = (math.raiz(x+1,2) / 4)
    c = math.raiz(4 * x + math.potencia(2,x),2)
    escreva("o resultado é: ", (a + b) / c)
  }
}