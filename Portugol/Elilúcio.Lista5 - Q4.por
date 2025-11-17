programa {
  funcao inicio() {
    inteiro id, idm, entrg
    real  dist, distm, distt
    id =0
    idm = 0
    entrg = 0
    dist = 0
    distm = 0
    distt = 0
    faca{
      faca{
        faca{
         escreva("digite o id do motorista(caso o valor seja negativo será desconsiderado): ")
         leia(id)
         escreva("digite a distância percorrida(caso o valor seja negativo será desconsiderado): ")
         leia(dist)
        }enquanto(id < 0)
      }enquanto(dist < 0)
    se(id != 0){
     entrg +=1
     distt += dist
     se(dist > distm){
       idm = id
       distm = dist
     }
    }
    }enquanto(id != 0)
    escreva("o total de entregas será ", entrg, ", a distância total percorrida será ", distt, ", e o motorista que percorreu a maior distância em uma única corrida foi o com o id ", idm, ".")
  }
}
