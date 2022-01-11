import qrcode

img = qrcode.make("https://www.instagram.com/thevisiblechurch/?hl=en")
img.save("visibleINSTA.jpg")

img = qrcode.make("https://linktr.ee/VisibleChurch")
img.save("visibleLinkTree.jpg")

img = qrcode.make("https://pushpay.com/g/visiblekissimmee?src=fp")
img.save("visibleGive.jpg")