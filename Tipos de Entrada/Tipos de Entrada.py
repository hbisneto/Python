from datetime import date
AnoAtual = date.today().year
SoftwareName = "TIPOS DE ENTRADA"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2019 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

#Para que o usuário possa digitar algo, é necessário usar o comando "input"
#Existem 3 tipos de entradas mais usadas: String, Integer e Float. (str, int e float)

#O exemplo abaixo explica como permitir que usuário insira uma entrada do tipo str
Nome = str(input("Insira o seu nome: "))
print("O nome inserido foi:", Nome)

#O exemplo abaixo explica como permitir que o usuário insira uma entrada do tipo int
Idade = int(input("Insira sua Idade: "))
print("Você tem:", Idade, "anos.")

#Usando a variável 'Idade' combinada com o mesmo tipo de entrada, é possivel fazer cálculos matemáticos
print("")
Ano_Atual = int(input("Em que ano estamos? "))
Data_Nasc = (Ano_Atual - Idade)
print("Estamos no ano de", Ano_Atual)
print("Isso significa que você nasceu em", Data_Nasc)
#Linha em branco
print("")
#Ao invés de usar o comando 'print()' duas vezes, é possível mostrar o resultado usando quebra de linha
print("*Exemplo de mensagem em uma linha de código*\n\nEstamos no ano de:", Ano_Atual,"\nIsso significa que você nasceu em:", Data_Nasc)

#O exemplo abaixo explica como permitir que o usuário insira uma entrada do tipo float (lembre-se de usar ponto '.' ao invés de virgula ','
Peso = float(input("\nInsira o seu peso: "))
print("Seu peso é:", Peso, " Kgs")

#Usando o mesmo tipo de entrada (float) é possível fazer cálculos. Assim como no exemplo do tipo de entrada 'Int'
#Também é possível combinar cálculos usando variáveis do tipo 'int' e 'float'

Max_Pessoas = int(7) #Lembre-se: O usuário tem a opção de inserção dessa informação
Peso_Pessoa = float(80.2) #Lembre-se: O usuário tem a opção de inserção dessa informação
Max_Peso = (Max_Pessoas * Peso_Pessoa)
print("\nO elevador do seu prédio suporta até", Max_Pessoas, "pessoas de", Peso_Pessoa, "Kgs.\n(Seu elevador suporta o peso total de", Max_Peso, "Kgs)")


print("")
print("")
print("Nesse exemplo foi abordado:")
print("- Tipos de entrada: str;")
print("- Tipos de entrada: int;")
print("- Tipos de entrada: float;")
print("- Inserção de informações por parte do usuário (input);")
print("- Quebra de linha;")
print("")
print("Bonus:")
print("- Fazer comentários no código;")
