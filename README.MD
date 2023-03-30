<h1 align="center">pRPG</h1git >

Descrição 
Esse é um projeto de um gerenciador de fichas para o jogo de RPG de mesa
Dungeons and Dragons 5e, nesse projeto o usuário poderá criar, editar e 
deletar as fichas de seus personagens assim como adicionar e remover,
itens comuns, equipamentos de defesa e de ataque, contando também com 
uma área para a adição da descrição das habilidades do personagem, 
visando uma melhor usabilidade
Espero que este site seja útil para a comunidad de jogadores de RPG.

Contribuiçães 
caso deseje contribuir ou reportar falhas.
mande um email para : jhony.prf@gmail.com
com o titulo : reporte pRPG

Instruções para rodar o site em sua maquina

1 - clone o projeto em sua maquina 
  $ git clone https://github.com/ataabi/pRPG

2 - Criando um ambiente virtual
  navegue até o diretorio em que o projeto está salvo 
  e usamos o seguinte comando :
  $ python -m venv ./venv

3 -  Instalando as dependências do projeto
  $ pip install -r requirements.txt

4 - Iniciando o ambiente virtual 
  no diretorio do projeto 
  CMD :
   $ <venv>\Scripts\activate.bat
  PowerShell :
   $ <venv>\Scripts\Activate.ps1
  Bash
   $ <venv>/bin/activate

5 - Inicializando o servidor 
  $ python manage.py runserver 

extra :
para adicionar os itens comuns do jogos execute o arquivo 
"popula_loja.py" dentro do ambiente virtual do projeto