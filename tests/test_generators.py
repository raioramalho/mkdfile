import generators.node as node_gen
import generators.python as python_gen
import generators.nginx as nginx_gen
import generators.go as go_gen


def test_node_generate():
    content = node_gen.generate(multistage=False, tag="18")
    assert "FROM node:18" in content


def test_python_generate():
    content = python_gen.generate(multistage=True, tag="3.11", variant="slim")
    assert "python:3.11-slim" in content


def test_nginx_generate():
    content = nginx_gen.generate(tag="1.25", variant="alpine")
    assert "nginx:1.25-alpine" in content


def test_go_generate():
    content = go_gen.generate(multistage=True, tag="1.20", variant="alpine")
    assert "golang:1.20-alpine" in content

