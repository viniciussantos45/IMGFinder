# IMGFinder

IMGFinder é uma classe em Python desenvolvida para automatizar tarefas baseadas em reconhecimento de imagem. A classe permite analisar imagens na tela e executar funções predefinidas com base nas imagens encontradas, usando técnicas de processamento de imagem e automação de GUI.

## Instalação

Antes de começar, instale as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar a classe IMGFinder, siga os passos abaixo:

1. Coloque as imagens que deseja analisar na pasta `Images`.

2. No arquivo `example.py`, defina as funções que devem ser executadas quando uma imagem específica for encontrada. Os nomes das funções devem corresponder ao nome da imagem, sem o prefixo de ordenação e a extensão `.png`. Por exemplo, se o nome da imagem for `1-exemplo_um.png`, o nome da função deve ser `exemplo_um()`. Quando a imagem for encontrada na tela, a função correspondente será executada automaticamente.

3. Importe a classe IMGFinder e instancie-a com o diretório das imagens e as funções globais:

```python
from IMGFinder.IMGFinder import IMGFinder

# Directory of your images
directoryImgs = '.\\Images\\'

img = IMGFinder(directoryImgs, globals())
```

4. Chame o método `run()` para iniciar a análise das imagens e executar as funções correspondentes:

```python
img.run(True, ['curte.png', 'proxima.png'])
```

### Opções de análise

IMGFinder oferece dois modos de análise de imagem: ordenado e aleatório.

- Para análise ordenada, siga o padrão de nomenclatura das imagens: `1-exemplo.png`, `2-observacao.png`, etc. O método `run()` analisa as imagens na ordem numérica. Por padrão, o método `run()` realiza a análise ordenada, podendo ser chamado sem parâmetros: `run()`.

- Para análise aleatória, passe `False` como parâmetro no método `run()`: `run(False)`. Neste modo, a ordem numérica das imagens é ignorada e as imagens são analisadas em uma ordem não especificada.

**Nota:** Os nomes das imagens não devem conter espaços. Substitua espaços por underscores ( `_` ).

## Funcionamento da Classe IMGFinder

A classe IMGFinder utiliza bibliotecas como `pyautogui`, `cv2`, e `numpy` para realizar o reconhecimento de imagem e automação de GUI. Ela captura a tela do computador e compara com as imagens fornecidas, identificando a posição das imagens na tela. Quando uma imagem é encontrada, a função correspondente é executada automaticamente, permitindo a automação de tarefas específicas baseadas nas imagens encontradas.

## Exemplo

No arquivo `example.py`, você encontrará um exemplo de como utilizar a classe IMGFinder para automatizar tarefas baseadas em reconhecimento de imagem, como clicar em posições específicas na tela com base nas imagens encontradas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.
