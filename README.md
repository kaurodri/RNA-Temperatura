## Ambiente Virtual
```py
$ pyenv local 3.12.1
```
```py
$ python -m venv .venv
```
```py
$ source .venv/Scripts/activate
```

## Configurando o Ambiente na Janela Interativa
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
