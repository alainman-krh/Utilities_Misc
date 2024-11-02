symbollist = ["⚠", "⚠️", "👍", "✨", "🚀", "🤷‍♂️"]
emojisuffix = b"\xef\xb8\x8f".decode("utf-8")

for symb in symbollist:
    print(symb)
    code = symb.encode("utf-8")
    print(code)
    if emojisuffix not in symb:
        symb += emojisuffix
        code = symb.encode("utf-8")
    print(code, symb)