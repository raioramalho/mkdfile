class Mkdfile < Formula
  desc "Gerador de Dockerfile com suporte a multistage"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/releases/download/v0.1.0/mkdfile-macos.tar.gz"
  sha256 "ff4e1d45dcaa0621523510b694f104ffba49ff78e0fad6374f8f6c70cdc57491"
  license "MIT"

  def install
    bin.install "mkdfile"
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end
