class Mkdfile < Formula
  desc "Gerador de Dockerfile com suporte a multistage"
  homepage "https://github.com/raioramalho/mkdfile"
  url "https://github.com/raioramalho/mkdfile/releases/download/v0.1.0/mkdfile-macos.tar.gz"
  sha256 "a92d648149fc494f78db01490542ae695e64bbf07e5051a470379469c26d2ea7"
  license "MIT"

  def install
    bin.install "mkdfile"
  end

  test do
    system "#{bin}/mkdfile", "--help"
  end
end
