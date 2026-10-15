from pypdf import PdfReader

base = "/home/artur/arturfilipe.pt/"
files = [
    "cv-artur-filipe-pt.pdf",
    "cv-artur-filipe-en.pdf",
    "cv-artur-filipe-hospitality-pt.pdf",
    "cv-artur-filipe-hospitality-en.pdf",
]
for f in files:
    try:
        r = PdfReader(base + f)
        t = "\n".join((p.extract_text() or "") for p in r.pages)
    except Exception as e:
        print(f, "ERR", e); continue
    tl = t.lower()
    print("=" * 50)
    print(f, "| chars:", len(t))
    print("  ISO:", tl.count("iso"), "| 27001:", t.count("27001"),
          "| PMS:", tl.count("pms"), "| hotel:", tl.count("hotel"),
          "| A+ :", tl.count("a+"))
    print("-" * 50)
    print(t[:700])
    print()
