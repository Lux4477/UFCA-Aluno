programa {
  funcao inicio() {
    inteiro x, par, impar
    par = 0
    impar = 0
    faca{
      escreva("Digite valores inteiros e, no final, o programa calculará quantos são pares e quantos são ímpares, para encerrar o programa digite '-1': ")
      leia(x)
      se(x%2==0){
        par +=1
        escreva("\n")
      }senao{
        impar +=1
        escreva("\n")
        }
    }enquanto(x!=-1)
    impar -=1
    escreva(par, " são pares e ", impar, " são ímpares.")
  }
}
