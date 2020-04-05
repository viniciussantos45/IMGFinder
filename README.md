# IMGFinder
Classe em Python para robotização 

Instalar bibliotecas localizadas no arquivo requirements.txt

----V 0.2----

1- Agora é possivel fazer analise de imagens ordenadamente, e aleatóriamente. Para análise aleatória bastar passar False no parametro do método, exemplo: run(False).

OBS: Por padrão o método RUN analisa ordenadamente, pode ser instanciado sem parametros exemplo: run().

2-  O nome das imagens devem seguir o seguinte padrão caso deseja ordenação: (1-exemplo.png, 2-observacao.png, ....)

OBS: Os nomes das imagens NÃO DEVEM CONTER ESPAÇOS,  os substituam por "_".

OBS 2: Os nomes das funções devem ser iguais ao nome da imagem SEM O PREFIXO DE ORDENAÇÃO, exemplo: Se o nome da imagem é 1-exemplo_um.png
o nome da função deverá ser exemplo_um()

