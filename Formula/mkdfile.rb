class Mkdfile < Formula
  desc "Gerador de Dockerfile com suporte a multistage"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/releases/download/v0.1.0/mkdfile-macos.tar.gz"
  sha256 "795e6ba84cc66e86db5c5c18b8d265ebbb3fe20469078487db8a3b1e7797309d"
  license "MIT"

  def install
    bin.install "mkdfile"
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end