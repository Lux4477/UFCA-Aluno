programa {
  funcao inicio() {
    inteiro a,b,i,j,E
    E = 0
    escreva("digite valores, respectivamente, para a e b: ")
    leia(a, b)
    para(i=1; i <= a; i++){
      para(j=1; j <= b; j++){
       E+=(a*b)+(i+j)*(i+j)
      }
    }
   escreva("o resultado da expressão é ",E)
  }
}
