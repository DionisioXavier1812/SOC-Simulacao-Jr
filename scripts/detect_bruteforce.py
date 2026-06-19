# scripts/detect_bruteforce.py
"""
Script de detecção de brute force em logs de autenticação.
Autor: Dionisio Xavier
Data: 19/06/2026
"""

from collections import Counter

def detectar_bruteforce(logs, limite=5):
    """
    Função que identifica usuários com falhas repetidas de login.
    :param logs: lista de strings com eventos de login
    :param limite: número máximo de falhas permitido
    :return: lista de usuários suspeitos
    """
    tentativas = Counter()
    for linha in logs:
        partes = linha.split()
        usuario = partes[1]  # supondo formato "timestamp usuario falha"
        tentativas[usuario] += 1
    
    suspeitos = [u for u, c in tentativas.items() if c > limite]
    return suspeitos

if __name__ == "__main__":
    exemplo_logs = [
        "2026-06-19 user1 falha",
        "2026-06-19 user1 falha",
        "2026-06-19 user1 falha",
        "2026-06-19 user1 falha",
        "2026-06-19 user1 falha",
        "2026-06-19 user1 falha",
    ]
    print("Usuários suspeitos:", detectar_bruteforce(exemplo_logs))
