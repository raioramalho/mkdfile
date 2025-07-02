
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

```bash
python cli.py --image <node|python|nginx|go> [--multistage] [--output Dockerfile]
```

### Exemplos:

Gerar um Dockerfile simples para Node.js:

```bash
python cli.py --image node --output Dockerfile
```

Gerar com multistage:

```bash
python cli.py --image python --multistage --output Dockerfile
```

Gerar para nginx:

```bash
python cli.py --image nginx
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
