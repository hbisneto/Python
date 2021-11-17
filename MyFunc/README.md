# Funções

Uma função é um pedaço de código que faz alguma tarefa específica e pode ser chamado de qualquer parte do programa quantas vezes desejarmos.

#### Clareza do código:
Separando pedaços de código em funções, podemos entender mais facilmente o que cada parte do código faz. Além disso, para procurarmos por uma certa ação feita pelo programa, basta buscar a função correspondente. Isso torna muito mais fácil o ato de procurar por erros.

#### Reutilização:

Muitas vezes queremos executar uma certa tarefa várias vezes ao longo do programa. Repetir todo o código para essa operação é muito trabalhoso, e torna mais difícil a manutenção do código: se acharmos um erro nesse código, teremos que corrigí-lo em todas as repetições do código. Chamar uma função diversas vezes contorna esses dois problemas.

#### Independência:

Uma função é relativamente independente do código que a chamou. Uma função pode modificar variáveis globais ou ponteiros, mas limitando-se aos dados fornecidos pela chamada de função.


## Definindo uma função

Uma função pode necessitar de alguns dados para que possa realizar alguma ação baseada neles. Esses dados são chamados parâmetros da função. Além disso, a função pode retornar um certo valor, que é chamado valor de retorno. Os parâmetros (e seus tipos) devem ser especificados explicitamente, assim como o tipo do valor de retorno.

#### Funções sem argumentos:

Como o próprio nome diz, é uma função que não tem argumentos. Quando a função for chamada, o programa apenas irá imprimir "Hello World" na tela.

```
def hello_world():
	print("Hello World!")
```
Output:

```
Hello World!
```

#### Funções com argumentos obrigatórios:

Quando uma função necessita de argumentos para retornar um valor, chamamos ela de **Função com argumentos obrigatórios**

```
def Diga_Algo(msg, nome):
    print('{}, {}!'.format(msg, nome))
```

- Se tentarmos chamar a função com menos argumentos ela simplesmente não será executada!

```
>>> Diga_Algo('Olá')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Diga_Algo('Olá')
TypeError: Diga_Algo() missing 1 required positional argument: 'nome'
```

- Se errarmos a ordem dos argumentos, a função interpretará **nome** como **msg** e **msg** como **nome**:

```
>>> Diga_Algo('Olá', 'Fulano')
Olá, Fulano!
```

#### Funções com argumentos nomeados na chamada:

É possível inverter a ordem dos argumentos, desde que esses argumentos sejam tratados como argumentos nomeados:

```
>>> Diga_Algo(nome = 'Fulano', msg = 'Olá')
Olá, Fulano!
```

Embora o nome tenha passado antes da mensagem, as variáveis foram usadas na ordem certa, pois os parâmetros foram nomeados

#### Função declarada com valores padrão:

Também é possível definir valores padrão para argumento(s) de uma função:

```
def Diga_Algo(nome, msg = 'Tudo bem'):
	print('{}, {}!'.format(msg, nome))
```

Dessa forma podemos omitir o argumento msg na chamada, pois ele assumirá seu valor padrão:

```
>>> Diga_Algo('Fulano')
```
Output:

```
Tudo bem, Fulano!
```

#### Observação:

O argumento com valor padrão não ficou por último por acaso, é obrigatório que seja assim! Ou todos têm valor padrão, ou os com valor padrão ficam por último.

# Reforçando

```
# Obrigatórios e na ordem certa:
Diga_Algo(msg, nome)

# Nomeados, ordem arbitrária:
Diga_Algo(nome = 'Fulano', msg = 'Olá')

# Valor padrão, permite omissão:
def Diga_Algo(nome, msg = 'Olá')
```
