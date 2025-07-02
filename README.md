
# 🐳 mkdfile - Make DockerFile

Gerador de `Dockerfile` customizado com suporte a multistage build.  
Escrito em **Python + Click + Jinja2** para facilitar a criação de imagens Docker para projetos comuns.

## 🚀 Imagens suportadas

- `node`
- `python`
- `nginx`
- `go`

## 🛠️ Requisitos

- Python 3.8+
- pip

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## 📦 Como usar

Cada imagem possui um subcomando específico. Execute `python cli.py --help` para ver todas as opções.

### Node.js

```bash
python cli.py node [--tag 18] [--variant alpine] [--multistage] [--output Dockerfile]
```

### Python

```bash
python cli.py python [--multistage] [--output Dockerfile]
```

### Nginx

```bash
python cli.py nginx [--multistage] [--output Dockerfile]
```

### Go

```bash
python cli.py go [--multistage] [--output Dockerfile]
```

## 📁 Estrutura

```
.
├── cli.py                # Entrada principal da CLI
├── generators/           # Lógicas de geração para cada linguagem
├── templates/            # Templates Jinja2 de Dockerfile
├── requirements.txt      # Dependências
└── README.md             # Este arquivo
```

## 📄 Licença

MIT © Alan Ramalho

## 🙏 Créditos

Projeto mantido por [Alan Ramalho](https://github.com/raioramalho) <ramalho.sit@gmail.com>.
