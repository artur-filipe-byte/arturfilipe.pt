from PIL import Image
src = "/home/artur/Documentos/cERTS/iso_27001_foundation.png"
dst = "/home/artur/arturfilipe.pt/assets/certs/iso27001-foundation.pdf"
img = Image.open(src).convert("RGB")
img.save(dst, "PDF", resolution=100.0)
print("saved", dst, img.size)
