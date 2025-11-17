programa {
  funcao inicio() {
    real n,i,r             //respectivamente, valor de entrada, variável suporte, resultado, variável suporte
    r = 0
    escreva("Digite um número inteiro ímpar: ")
    leia(n)
    se(n % 2 == 0){          //check de números pares
      escreva("O número digitado é par, por favor rode novamente o programa e insira um novo número")
    }
    senao se(n == 1){
      r = 1/n + n
      escreva("O resultado da equação será ",r)
    }
    senao {
      para(i=1;i<=n;i=i+2){
       r = r + (i/(n-(i-1)))
      }
      para(i=1;i<n;i=i+2){
        r = r -(i+1)/(n-i)
      }
      escreva("O resultado da equação será ",r)
  }
  }
}
