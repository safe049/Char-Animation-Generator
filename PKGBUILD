
pkgname=char-animation-gen
pkgver=0.1.0
pkgrel=1
pkgdesc="Character Animation Generator"
arch=("any")
url="https://github.com/safe049/Char-Animation-Generator"
license=("MIT")
source=("https://github.com/safe049/Char-Animation-Generator/archive/refs/heads/main.zip")
sha256sums=('SKIP') # Calculate this later

package() {
  # Extract the source
  unzip -q "${srcdir}/${pkgname}-main.zip" -d "${srcdir}"

  # Install the binary
  install -Dm755 "${srcdir}/Char-Animation-Generator-main/dist/CharAnimationGen" "${pkgdir}/usr/bin/CharAnimationGen"

}