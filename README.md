# Linha Lógica
Neste código, a rede neural tenta adivinhar a regra para converter temperaturas de Celsius (°C) para Fahrenheit (°F). Existe uma fórmula matemática para isso, mas ela não sabe qual é. Então, o código faz com que ela aprenda a relação tentando e errando.

No começo, como ela não faz ideia de como funciona, chuta uma fórmula qualquer. Mas, quando testa essa fórmula, os resultados ficam errados. Por exemplo, se °C = 0, a fórmula dela diz que °F = 10, mas na verdade deveria ser 32. Isso acontece porque os números usados foram chutes aleatórios.

Ela pega vários exemplos de temperaturas reais (como 0°C = 32°F, 10°C = 50°F, etc.) e compara com suas previsões. Em seguida, calcula o quanto errou usando uma função que basicamente mede a diferença entre o seu chute e o valor real. Quanto maior o erro, pior foi o chute.

Agora vem a parte inteligente: em vez de continuar chutando aleatoriamente, ela usa matemática para descobrir como ajustar seus números e errar menos. Se o resultado ficou abaixo do esperado, ela aumenta um pouco os números; se ficou acima, ela diminui. A rede neural faz isso usando derivadas para descobrir quanto ajustar os números. Esse processo se chama backpropagation e gradiente descendente.

Ela não acerta de primeira, então repete esse processo centenas ou milhares de vezes, sempre seguindo os passos:

1. Chuta um resultado.

2. Calcula o erro.

3. Ajusta os números para errar menos na próxima.

No final, depois de muitas tentativas, a fórmula fica quase igual à verdadeira.

<br>

# Code

### Ambiente Virtual
```py
$ pyenv local 3.12.1
```
```py
$ python -m venv .venv
```
```py
$ source .venv/Scripts/activate
```

### Configurando o Ambiente na Janela Interativa
(Se necessário)

```py
$ which python
```
```py
$ pip install ipykernel
```
```py
$ python -m ipykernel install --user --name nome_do_seu_ambiente --display-name "Python (Ambiente)"
```
