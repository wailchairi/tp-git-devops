def saluer(nom):
    return f"Bonjour, {nom} !"

def additionner(a, b):
    return a + b

if __name__ == "__main__":
    print(saluer("DevOps"))

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b

def moyenne(liste):
    if not liste:
        raise ValueError("Liste vide")
    return sum(liste) / len(liste)

def mediane(liste):
    s = sorted(liste)
    n = len(s)
    return s[n//2] if n % 2 else (s[n//2-1] + s[n//2]) / 2
