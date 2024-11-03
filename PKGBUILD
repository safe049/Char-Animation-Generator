pkgname=char-animation-generator
pkgver=r26.866a2c6
pkgrel=1
pkgdesc="Char Animation Generator"
arch=('x86_64')
url="https://github.com/safe049/Char-Animation-Generator"
license=('GPL3')
source=("CharAnimationGen::git+${url}.git")
sha256sums=('SKIP')


package() {
  install -Dm755 "${srcdir}/Char-Animation-Generator/dist/CharAnimationGen" "${pkgdir}/usr/bin/char-animation-generator"

}


