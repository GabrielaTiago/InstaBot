<p align = "center"><img src="src/assets/favicon.png" alt="insta favicon" height="80px" align = "center"/></p>

<!-- Nome do Projeto -->
# <p align = "center">InstaBot</p>

<!-- Apontamento do projeto -->
<h3  align = "center">Bot de Curtidas e Comentários</h3>

<!-- Tecnologias utlizadas no projeto -->
<div align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python badge" heigth="30px"/>
</div>

<!-- Imagem Da Aplicação -->
<!-- <center>
![NomeDaImagem](screens/images/print.png)
</center> -->

<!-- Espaço entre conteúdos -->
$~$

## :clipboard: Descrição

O projeto "InstaBot" é uma robô que possibilida interações automatizadas com a última postagem de um perfil. Com esta aplicação, o usuário insere suas credenciais de login, e a automação realiza o login, acessa o perfil definido, seleciona o último post e ralizando as interações definidas.

<!-- Link de Acessa à aplicação -->
<!-- ### :emoji: [Acesse aqui](https://link/) -->

<!-- Espaço entre conteúdos -->
$~$

## :bookmark_tabs: Características do projeto

- Usuário:
  - Defini suas credenciais de login - email e senha
- Robô:
  - Verifica arquivo com as credenciais de login
    - Caso não exista, solicita email e senha, cria arquivo com estes dados
    - Caso exista, pega email e senha armazenados
  - Efetua o login utilizando o email e senha
  - Busca pelo perfil definido
  - Acessa o peril
  - Identifica a última postagem
  - Verifica se o post já foi curtido
    - Caso falso - curte e comenta
  - Realiza logout
  - Pausa automação por 24h

<!-- Espaço entre conteúdos -->
$~$

## :rocket: Rodando o projeto localmente

Este projeto foi feito com [Python 3](https://www.python.org), portanto, certifique-se de ter a última versão estável rodando localmente. Como também o [pip](https://pypi.org/project/pip/).

:warning: Caso você utilize os seguintes sistemas operacionais `MacOS` ou `Linux`, utilize o `python3` e `pip3` nos lugares de **python** e **pip**, respectivamente, nos comandos abaixo.

1. Realizar o clone deste projeto, no terminal de sua máquina, utilize o [git](https://git-scm.com/) e insira o seguinte comando:

    ``` bash
    git clone git@github.com:GabrielaTiago/InstaBot.git
    ```

2. Entre na pasta do projeto, usando o coamndo `cd`:

    ``` bash
    cd /caminho/oara/InstaBot
    ```

3. Crie um ambiente virtual, de acordo com seu sistema operacional:

    ``` bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - Windows:

        ``` bash
        .\venv\Scripts\activate
        ```

    - MacOS/Linux:

        ``` bash
        source venv/bin/activate
        ```

5. Instale as dependências necessárias

    ``` bash
    pip install -r requirements.txt
    ```

6. Rode o arquivo `main.py`

    ``` bash
    python src/main.py
    ```

A aplicação será iniciada.

<!--
## 🎮 Demonstração

<center>

</center> -->

<!-- Espaço entre conteúdos -->
$~$

## :bulb: Reconhecimentos

- [Badges para Github](https://github.com/alexandresanlim/Badges4-README.md-Profile#-database-)
- [README Inspiração de README](https://gist.github.com/luanalessa/7f98467a5ed62d00dcbde67d4556a1e4#file-readme-md)

<!-- Espaço entre conteúdos -->
$~$

## 👩‍🦱 Autora

Gabriela Tiago de Araújo

- email: <gabrielatiagodearaujo@outlook.com>
- linkedin: <https://www.linkedin.com/in/gabrielatiago/>
- portfolio: <https://gabrielatiago.vercel.app>

<!-- Espaço entre conteúdos -->
$~$

[🔝 De volta ao topo](#instabot)
