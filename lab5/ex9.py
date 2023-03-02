import re

text = "SalamAleikumOtandastar"
pattern = r"(\w)([A-Z])"

print(re.sub(pattern, r"\1 \2", text))

