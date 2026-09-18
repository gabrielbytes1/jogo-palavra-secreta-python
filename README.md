# Jogo da Palavra Secreta em Python

Um jogo de adivinhação de palavras desenvolvido em Python a partir de um exercício do curso de [**Python 3 do básico ao avançado - com projetos reais**](https://www.udemy.com/course/python-3-do-zero-ao-avancado/?srsltid=AU7gw4VJQqQfrkyGAWxrJJWCgm6DDAmLewgUkoEx3NsJ9CNsVm_9CbDr&couponCode=KEEPLEARNING), do professor [**Luiz Otávio Miranda**](https://www.youtube.com/channel/UCORZcu08VQiRCKpVGHTWwAA).

A proposta original do exercício era criar um jogo no qual um jogador tenta descobrir uma palavra secreta digitando uma letra por tentativa. A partir dessa proposta, o projeto foi expandido com novas regras, validações e mecânicas próprias, transformando o exercício em um pequeno jogo de **2 jogadores**, com configuração da palavra secreta, limite de tentativas e condições de vitória e derrota.

---

## 🎮 Sobre o jogo

O **Jogo da Palavra Secreta** funciona em duas etapas:

1. **Jogador 1** define a palavra secreta e configura a quantidade máxima de tentativas.
2. **Jogador 2** tenta descobrir a palavra digitando uma letra por vez.

Durante a partida, o jogo mostra quais letras já foram descobertas e substitui as demais por `*`.

Por exemplo, se a palavra secreta for:

```text
PYTHON
```

e o jogador descobrir as letras `P`, `T` e `O`, a tela poderá mostrar:

```text
P*T*O*
```

O jogador vence quando todas as letras da palavra forem descobertas.

Caso o número máximo de tentativas seja atingido antes disso, o jogador perde.

---

## 🕹️ Como jogar

### 1. Escolha da palavra secreta

O primeiro jogador informa uma palavra.

A palavra precisa:

- conter pelo menos um caractere;
- possuir somente letras;
- não conter espaços;
- ser aceita pelo programa como uma palavra única.

O jogo converte a entrada para **letras maiúsculas**, padronizando as comparações durante a partida.

### 2. Definição das tentativas

Depois da palavra ser definida, o primeiro jogador informa quantas tentativas estarão disponíveis.

O jogo calcula a quantidade de **letras diferentes** existentes na palavra e utiliza esse número como limite mínimo para que seja possível vencer.

Por exemplo:

```text
BANANA
```

possui 6 caracteres, mas somente 3 letras diferentes:

```text
B
A
N
```

Portanto, uma partida precisa permitir pelo menos 3 tentativas para que exista a possibilidade de descobrir a palavra somente com acertos de letras.

### 3. Início da partida

Depois que a configuração é concluída, a palavra secreta é ocultada da tela.

O segundo jogador começa digitando uma letra.

A entrada é validada para garantir que seja:

- exatamente um caractere;
- uma letra.

### 4. Letras já descobertas

Uma letra que já foi descoberta anteriormente não é adicionada novamente e **não consome uma tentativa**.

Exemplo:

```text
Tentativa 1 → P
Tentativa 2 → T
Tentativa 3 → P
```

Na terceira tentativa, o jogo informa que a letra `P` já foi descoberta e solicita uma nova jogada sem consumir uma tentativa.

### 5. Descoberta da palavra

Depois de cada tentativa, o programa percorre a palavra secreta e monta uma representação visual:

- letras já descobertas aparecem normalmente;
- letras ainda não descobertas aparecem como `*`.

Exemplo:

```text
Palavra secreta: PYTHON

Depois de descobrir P:
P*****

Depois de descobrir T:
P*T***

Depois de descobrir O:
P*T*O*
```

A mesma lógica funciona com palavras que possuem letras repetidas. Por exemplo:

```text
BANANA
```

Ao descobrir a letra `A`, todas as ocorrências de `A` são reveladas:

```text
*A*A*A
```

### 6. Vitória

O jogador vence quando a palavra formada passa a ser igual à palavra secreta.

Nesse momento, o jogo informa a vitória e mostra:

- a palavra secreta;
- o número de tentativas utilizadas.

### 7. Derrota

Caso o jogador atinja o número máximo de tentativas antes de descobrir a palavra, o jogo encerra a partida e informa:

- que o jogador perdeu;
- o número de tentativas disponíveis;
- qual era a palavra secreta.

---

## ⚙️ Principais funcionalidades

- Definição da palavra secreta pelo jogador.
- Ocultação da palavra secreta após sua definição.
- Conversão automática das entradas para letras maiúsculas.
- Validação da palavra secreta.
- Bloqueio de palavras vazias.
- Bloqueio de números e símbolos na palavra secreta.
- Validação da letra digitada.
- Bloqueio de entradas com mais de um caractere.
- Bloqueio de números e símbolos durante a partida.
- Definição personalizada do número máximo de tentativas.
- Cálculo da quantidade de letras diferentes da palavra.
- Limite mínimo de tentativas baseado nas letras diferentes.
- Letras repetidas não consomem tentativas.
- Exibição das letras descobertas.
- Exibição de `*` para letras ainda ocultas.
- Sistema de vitória.
- Sistema de derrota.
- Contador de tentativas.
- Limpeza da tela para esconder informações da rodada anterior.

---

## 🧠 Lógica do jogo

O funcionamento pode ser resumido desta forma:

```text
Jogador 1 define a palavra
          ↓
Validação da palavra
          ↓
Cálculo das letras diferentes
          ↓
Jogador 1 define o número de tentativas
          ↓
Validação do número de tentativas
          ↓
Palavra secreta é ocultada
          ↓
Começa a partida
          ↓
Jogador 2 digita uma letra
          ↓
Validação da letra
          ↓
A letra já foi descoberta?
       ↙         ↘
     SIM          NÃO
      ↓             ↓
Não consome      Consome
 tentativa        tentativa
                    ↓
             A letra existe?
               ↙       ↘
             SIM        NÃO
              ↓           ↓
       Adiciona às      Mantém
       descobertas      escondido
              ↓
       Monta a palavra
              ↓
      Palavra completa?
          ↙        ↘
        SIM        NÃO
         ↓           ↓
      Vitória      Continua
                    partida
                       ↓
              Acabaram tentativas?
                 ↙          ↘
               SIM          NÃO
                ↓             ↓
             Derrota       Continua
```

---

## 🔢 Por que o jogo considera as letras diferentes?

A quantidade de caracteres de uma palavra não representa necessariamente o número mínimo de tentativas necessário para descobri-la.

Por exemplo:

```text
ABACAXI
```

possui 7 caracteres, mas possui apenas 5 letras diferentes:

```text
A
B
C
X
I
```

Isso acontece porque uma única tentativa pode revelar **todas as ocorrências** de uma determinada letra.

O projeto utiliza:

```python
len(set(palavra_secreta))
```

para calcular a quantidade de letras diferentes e definir um limite mínimo de tentativas.

Essa regra evita configurar uma partida que seja matematicamente impossível de vencer apenas descobrindo letras.

---

## 🛡️ Validações

O jogo possui validações para reduzir entradas inválidas.

### Palavra secreta

A palavra precisa ser preenchida e conter somente letras.

Exemplos inválidos:

```text
""
"casa azul"
"casa123"
"casa!"
```

### Letra

A tentativa precisa conter exatamente uma letra.

Exemplos inválidos:

```text
"ab"
"123"
"@"
" "
```

### Número de tentativas

A quantidade de tentativas precisa ser informada como um número inteiro e respeitar o limite mínimo estabelecido pelo jogo.

---

## 📚 Conceitos de Python utilizados

O projeto foi desenvolvido utilizando conceitos estudados durante o aprendizado de Python, incluindo:

- `input()`
- `print()`
- variáveis
- `if / elif / else`
- `while`
- `for`
- strings
- `len()`
- `in`
- `not in`
- `isalpha()`
- `isdigit()`
- `upper()`
- `set()`
- `int()`
- f-strings
- `break`
- `continue`
- módulo `os`

O objetivo foi desenvolver a lógica utilizando principalmente os conceitos já estudados no curso, sem transformar um jogo simples em uma aplicação desnecessariamente complexa.

---

## 💻 Como executar

### Requisitos

- [Python 3 instalado](https://www.python.org/downloads/)

### Executando pelo terminal

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/jogo-palavra-secreta-python.git
```

Entre na pasta:

```bash
cd jogo-palavra-secreta-python
```

Execute o programa:

```bash
python palavra_secreta.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 palavra_secreta.py
```

---

## 📁 Estrutura do projeto

```text
jogo-palavra-secreta-python/
│
├── README.md
└── palavra_secreta.py
```

---

## 🎯 Origem do projeto

Este projeto começou como um exercício do curso de Python do professor **Luiz Otávio Miranda**.

O exercício original propunha um jogo simples de palavra secreta, no qual o usuário deveria descobrir a palavra digitando letras e visualizando `*` nas posições ainda não descobertas.

A partir dessa atividade, foram desenvolvidas novas mecânicas e validações de forma independente, incluindo:

- escolha da palavra secreta;
- configuração das tentativas;
- regras de vitória e derrota;
- validações adicionais;
- controle de letras repetidas;
- cálculo de letras diferentes;
- experiência para uma partida entre dois jogadores.

O objetivo deste projeto é registrar a evolução do aprendizado e praticar **lógica de programação, estruturas de controle, strings e validação de entradas**.

---

## 🚀 Possíveis evoluções futuras

O projeto pode receber novas funcionalidades conforme novos conceitos de programação forem estudados, por exemplo:

- sistema de pontuação;
- níveis de dificuldade;
- categorias de palavras;
- banco de palavras;
- histórico de partidas;
- ranking;
- funções para organizar melhor o código;
- interface gráfica;
- versão web.

Essas funcionalidades não fazem parte da versão atual porque o objetivo desta versão é manter o projeto compatível com o nível de conhecimento utilizado durante seu desenvolvimento.

---

## 👤 Autor

[**Gabriel Castro Azevedo**]([www.linkedin.com/in/gabrielcastro-dev](https://github.com/gabrielbytes1))

Estudante de Sistemas de Informação e desenvolvedor em formação, utilizando projetos práticos para consolidar conhecimentos de programação.

---

## 📌 Status

**Versão:** 1.0  
**Status:** Concluído

Projeto desenvolvido para fins de estudo, prática e construção de portfólio.
