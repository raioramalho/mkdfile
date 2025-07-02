class Mkdfile < Formula
  include Language::Python::Virtualenv

  desc "Gerador de Dockerfile customizado"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "1a9031de1a293af147421760679fe6cb2d453b3f3793cee961d039ad911501dd"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end
