def cipher(s: str) -> str:
    slist =  [chr(219 - ord(c)) if ord('a') <= ord(c) <= ord('z') else c for c in s]
    return ''.join(slist)

s = "af;\\fl;adfv,l;d,va"
print(cipher(s))
print(cipher(cipher(s)))
