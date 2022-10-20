# Processamento de Linguagem Natural: Sumarizador de textos online

#### Vídeo: [Projeto Final- Sumarização de textos online](https://youtu.be/IE8n49D7ykA)

## Um breve resumo
Nosso projeto foi a criação de um site para resumos de textos. Ele apresenta duas possíveis alternativas para o usuário:
colar ou fazer upload de textos de sua escolha, ou procurar por textos dentro da base de dados do Dicionário Histórico 
Bibliográfico Brasileiro. O usuário, após informar a quantidade de sentenças que deseja, pode escolher por uma breve explicação
de seu texto, ou pela visualização completa do arquivo, ressaltando suas sentenças mais importantes.

## Sobre a ideia do projeto
A ideia veio por conta de um problema muito comum de estudantes: lidar com **grande volume de textos e pouco tempo**. 
Conversando com alguns colegas, percebemos que seria muito útil para cursos de graduação, que dependem de uma grande 
quantidade de horas dedicadas à leitura, uma ferramenta que simplificasse essa atividade. Ao extrair informação de grandes artigos
de maneira rápida e eficiente seria possível aumentar a produtividade do estudante, além de auxiliar no entendimento de textos mais complexos.

## A execução

### ferramentas utilizadas

- Python
- [Google Translate API](https://pypi.org/project/googletrans/)
- [OpenAI API](https://openai.com/)
- [Textos DHBB](https://github.com/cpdoc/dhbb/tree/master/text)
- Flask
- JavaScript
- AJAX
- HTML
- CSS

### sumarização
Códigos produzidos estão em: `resumo.py`, `tradutor.py` e `sumarizacao.py`

Realizamos a sumarização de duas formas, a depender do especificado pelo usuário. Primeiro, quando o texto é inserido, 
realizamos um resumo que mescla diferentes partes do documento explicando-o de forma fácil e breve. Isso é feito
por meio da API OpenAI. Como ela funciona melhor em inglês, qubramos o texto em sentenças e utilizamos a
API do Google Translate para traduzir cada uma, uma vez que a tradução seria menos eficiente se lidasse com o texto 
inteiro de uma vez. Em seguida, ela é resumida e traduzida de volta para o português. O resumo aparece na tela sem necessidade
de recarregar ou redirecionar a página. Para isso utilizamos do objeto XMLHttpRequest para se comunicar com os scripts em flask
do servidor e, assim, garantir uma resposta imediata. Esta parte está mais detalhada em [backend](https://github.com/emap-ic/assignment-f-nlp/edit/main/README.md#backend).

Logo após feito o resumo, o usuário tem a opção de ver o texto por completo. Nessa página, aparece o texto inserido com as sentenças mais importantes
marcadas em amarelo. O número de sentenças é um parâmetro informado pelo usuário. O código que fizemos está em `sumarizacao.py` e é baseado na técnica de
sumarização por frequência das palavras. Primeiro, removemos palavras consideradas stopwords, deixando apenas palavras significativas. Em seguida, realizamos a frequência relativa de cada palavra a fim de obter uma métrica a respeito da importância de cada sentença. Assim, conseguimos criar um ranking das sentenças
consideradas mais importantes.

### backend
Código em: `app.py`

Para a comunicação entre o usuário e o servidor, utilizamos Flask. A informação passada pelo usário nos formulários em HTML é passada para o formato JSON 
para posteriormente poder ser tradata por nossos códigos em python. Escolhemos esse formato de arquivo, pois é comum tanto para Javascript (quem envia as 
informações para o backend) quanto para Python. Dessa forma, conseguimos criar uma aplicação que responde de forma assíncrona, de modo a tornar o site mais 
dinâmico.

### frontend
Para o frontend utilizamos CSS. Os códigos que fizemos estão em: `static/style.css`

### integração com DHBB
Página HTML em: `templates/cpdoc.html` 

#### busca dinâmica
Ao escolher a opção de "Acervo do CPDOC" o usuário é redirecionado para uma página na qual
pode pesquisar pelo título do documento da base de dados do DHBB. Fizemos um programa em JavaScript que mostra
os possíveis títulos de forma dinâmica à medida que o usurário digita. Para isso, criamos um programa `make_list.py`
que, ao ler todos os títulos do acervo, produziu como saída uma lista com todos esses nomes. Essa lista foi utilizada
pelo código em JavaScript e, assim, conseguimos criar essa busca dinâmica.

#### sumarização
Selecionado o nome do título, o próximo passo é encontrar o texto referente a ele. Para isso criamos o código `find.py`, que
recebe como parâmetro o nome digitado e devolve o texto referente a esse título. Como alguns títulos são nomes de pessoas
e estão no formato `SOBRENOME, nome`, tivemos que consertar isso para facilitar a busca do usuário. A sumarização segue a 
mesma forma da explicada anteriormente. A dificuldade enfrentada nessa etapa foi detalhada no issue [problema#6](https://github.com/emap-ic/assignment-f-nlp/issues/6).

<h2 id=equipe>Colaboradores:</h2>
  
  * [Matheus Araripe](https://github.com/MatheusAraripe)
  
  * [Rafael dos Santos](https://github.com/rafael1509)
  
  * [Davi Pestana](https://github.com/DaviPestana)
