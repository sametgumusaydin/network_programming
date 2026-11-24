import zlib

MAX_OUTPUT = 100_000

def safe_decompress(data):
    decompressor = zlib.decompressobj()

    result = decompressor.decompress(
        data,
        MAX_OUTPUT + 1
    )

    if len(result) > MAX_OUTPUT:
        raise ValueError("Veri boyutu sınırı aşıldı")

    if decompressor.unconsumed_tail:
        raise ValueError("Sıkıştırılmış veri sınırı aşıyor")

    remaining = MAX_OUTPUT + 1 - len(result)
    result += decompressor.flush(remaining)

    if len(result) > MAX_OUTPUT:
        raise ValueError("Veri boyutu sınırı aşıldı")

    if not decompressor.eof:
        raise ValueError("Eksik veya sınırı aşan veri")

    if decompressor.unused_data:
        raise ValueError("Beklenmeyen ek veri")

    return result



message = b"A" * 50000

compressed = zlib.compress(message)

print("Orijinal:", len(message))
print("Sıkıştırılmış:", len(compressed))

result = safe_decompress(compressed)

print("Açılmış:", len(result))