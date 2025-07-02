class Mkdfile < Formula
  desc "Gerador de Dockerfile com suporte a multistage"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/releases/download/v0.1.0/mkdfile-macos.tar.gz"
  sha256 "085f4b051fb6deb8c26d14320ec2a291333060d5aabb1c7cc2cc343349ff10ba"
  license "MIT"

  def install
    bin.install "mkdfile"
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end
