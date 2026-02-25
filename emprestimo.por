programa {
    funcao inicio() {
        real valorCasa, salario, prestacaoMensal, limite
        inteiro anos, meses

        escreva("Qual o valor da propriedade que você quer comprar?")
        leia(valorCasa)

        escreva("Quanto você ganha mensalmente?")
        leia(salario)

        escreva("Em quantos anos você pretende pagar?")
        leia(anos)

        meses = anos * 12
        prestacaoMensal = valorCasa / meses

        escreva("O valor da prestação é:", prestacaoMensal)

        limite = salario * 0.30

        se(prestacaoMensal <= limite) {
            escreva("\n Parabéns! Empréstimo Aprovado")
        }
        senao {
            escreva("\n Que pena! Empréstimo Negado")
        }
    }
}
