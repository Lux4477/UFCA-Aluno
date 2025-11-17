programa {
  inclua biblioteca Matematica --> math
  funcao inicio() {
    real x1, y1, x2, y2
    escreva("Digite a coordenada x do ponto P1: ")
    leia(x1)
    escreva("Digite a coordenada y do ponto P1: ")
    leia(y1)
    escreva("Digite a coordenada x do ponto P2: ")
    leia(x2)
    escreva("Digite a coordenada y do ponto P2: ")
    leia(y2)
    escreva("A distância entre os dois pontos é: ", math.raiz(math.potencia(x2 - x1, 2) + math.potencia(y2 - y1, 2), 2))
  }
}