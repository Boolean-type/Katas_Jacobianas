import re

def validar_contrasena(contrasena: str) -> bool:
    errores = []
    
    if len(contrasena) < 8:
        errores.append("La contraseña es demasiado corta")
        
    if not re.search(r'\d', contrasena):
        errores.append("La contraseña debe contener al menos un número")
    
    if errores:
        raise ValueError("\n".join(errores))
        
    return True


# Ejemplos de uso
if __name__ == "__main__":
    pruebas = [
        "1234567",           # corta
        "12345678",          # válida
        "abcdefgh",          # sin número
        "abc123",            # corta + sin número suficiente
        "Password123",       # válida
        "short",             # corta y sin número
        "a" * 8,             # válida (aunque solo letras)
        ""                   # vacía
    ]
