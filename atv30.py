def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificar_resultados(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

# Solicitação das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
resultado_media = calcula_media(nota1, nota2, nota3)

# Exibindo a média
print(f"Média: {resultado_media:.2f}")  # Formatação para mostrar duas casas decimais

# Verificando e exibindo o resultado final
resultado_final = verificar_resultados(resultado_media)
print(f"Status: {resultado_final}")
