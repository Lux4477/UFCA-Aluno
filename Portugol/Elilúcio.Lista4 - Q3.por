programa {
  funcao inicio() {
    inteiro th,tm,ts         //variáveis de tempo(hora, minuto e segundo) e peso
    real peso
    ts = 0                   //colocando o valor 0 na variável ts
    escreva("Insira um valor para a massa do material radioativo: ")
    leia(peso)
    para(peso;peso >= 1;peso = peso/2){
      ts = ts + 50           //repetição até o número ser menor que 1 para aumentar o valor dos segundos por 50 e diminuir o peso pela metade
    }
    tm = ts/60
    ts = ts%60
    th = tm/60
    tm = tm%60
    escreva("Irá demorar aproximadamente ", th, "h, ", tm, "m e ", ts, "s para o material radioativo reduzir para menos de um grama de massa")
  }
}
