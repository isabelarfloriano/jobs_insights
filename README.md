# Projeto Job Insights! 	:briefcase:

Projeto desenvolvido em Python e Flask onde os dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma disponiblizando conjuntos de dados para cientistas de dados. A Trybe criou as páginas inicial e de pesquisa por vaga, usando as funções que criaram e descreveram para filtrar os dados corretamente. Com base na estrutura já existente, desenvolvi a página de detalhes de uma vaga e desenvolvi alguns testes.

O Job Insights permite a análises a partir de um conjunto de dados sobre empregos.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
      <li>Utilizar o terminal interativo do Python.</li>
      <li>Utilizar estruturas condicionais e de repetição.</li>
      <li>Utilizar funções built-in do Python.</li>
      <li>Utilizar tratamento de exceções.</li>
      <li>Realizar a manipulação de arquivos.</li>
      <li>Escrever funções.</li>
      <li>Escrever testes com Pytest.</li>
      <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
    </ul>
</details>

<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para iniciar a aplicação criada com Flask, execute o comando <code>flask run</code> na raiz do projeto.</li>
    <li>Para parar a aplicação, pressione <code>CTRL+C</code>.</li>
    <li>A aplicação estará disponível na URL: <code>http://127.0.0.1:5000/</code>.</li>
    <li>Para executar todos os testes, execute o comando <code>python3 -m pytest</code> na raiz do projeto.</li>
    <li>Para executar os testes individualmente, execute um dos comandos a seguir na raiz do projeto:
      <ul>
        <li><code>python3 -m pytest -k test_counter</code></li>
        <li><code>python3 -m pytest -k test_brazilian_jobs</code></li>
        <li><code>python3 -m pytest -k test_sort_by_criteria</code></li>
      </ul>
    </li>
    <li>Para executar a aplicação com Docker, execute os comandos a seguir na raiz do projeto:
      <ul>
        <li><code>docker-compose up -d</code> para subir o container.</li>
        <li><code>docker-compose down</code> para parar o container.</li>
      </ul>
    </li>
  </ol>
</details>
<details>
  <summary><strong>Detalhes sobre Testes Desenvolvidos</strong></summary><br />
  <p>tests/counter/test_counter.py</p>
    <ul>
      <li>Implementação dos testes para função count_ocurrences</li>
      <li>Chamar a função `count_ocurrences` passando dois parâmetros:</li>
            <ul>
                 <li>`path` uma string com o caminho do arquivo (`data/jobs.csv`) </li>
                 <li>`word` uma string com a palavra a ser contabilizada </li>
             </ul>
      <li>Garante que a função retorna corretamente a quantidade de ocorrências da palavra solicitada </li>
    </ul>	
  <p>tests/brazilian/test_brazilian_jobs.py</p>
    <ul>
      <li>Implementação dos testes para função read_brazilian_file</li>
      <li>Chamar a função `read_brazilian_file` passando um parâmetro:</li>
            <ul>
                 <li>`path` uma string com o caminho do arquivo (`data/jobs.csv`) </li>
             </ul>
      <li>Garante que a função retorna uma lista de dicionários com as chaves em inglês </li>
    </ul>
  <p>tests/sorting/test_sorting.py</p>
    <ul>
      <li>Implementação dos testes para função sort_by</li>
      <li>Chamar a função `sort_by` passando dois parâmetros:</li>
            <ul>
                 <li>`jobs` uma lista de dicionários com os detalhes de cada emprego</li>
                 <li>`criteria` uma string com uma chave para ser usada como critério de ordenação.</li>
             </ul>
      <li>O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`</li>
      <li>A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.</li>
      <li>Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.</li>
    </ul>	
</details>
