programa {
  funcao inicio() {
    real A,B,C,D,E,F,X,Y,den
    escreva("Digite um valor para A: ")
    leia(A)
    escreva("Digite um valor para B: ")
    leia(B)
    escreva("Digite um valor para C: ")
    leia(C)
    escreva("Digite um valor para D: ")
    leia(D)
    escreva("Digite um valor para E: ")
    leia(E)
    escreva("Digite um valor para F: ")
    leia(F)

    den = A * E - B * D
    se(den == 0){
      escreva("O denominador das divisões se igualou a zero, rode novamente o programa com novos valores.")
    }senao{
      escreva("X será igual a " , (C * E - B * F) / den , "e o Y será igual a " , (A * F - C * D) / den)
    }
  }
}
