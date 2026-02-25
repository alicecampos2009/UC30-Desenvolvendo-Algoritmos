programa {
    funcao inicio() {
        inteiro numero, i, soma

        soma = 0

        escreva("Digite um número:")
        leia(numero)

        para(i = 1; i <= numero; i++) {
            soma = soma + i 
        }

        escreva("A soma é igual a:", soma)
    }
}    