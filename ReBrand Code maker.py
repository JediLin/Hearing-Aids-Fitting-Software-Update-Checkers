import rot_codec

with open("ReBrand Unlock Code.md", "r+", encoding="utf-8") as src:
    content = src.read()
    enc = rot_codec.rot47_encode(content)

with open("ReBrand Unlock Code.enc", "w", encoding="utf-8") as target:
    target.write(enc)

