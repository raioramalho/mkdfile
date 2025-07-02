class Mkdfile < Formula
  desc "Gerador de Dockerfile com suporte a multistage"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/releases/download/v0.1.0/mkdfile-macos.tar.gz"
  sha256 "INSIRA_O_HASH_AQUI"
  license "MIT"

  def install
    bin.install "mkdfile"
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end
