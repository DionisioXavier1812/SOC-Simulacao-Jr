# Relatório de Incidente - Tentativa de Brute Force

**Data:** 19/06/2026  
**Analista:** Dionisio Xavier  

---

## Resumo
Foi detectado um número elevado de falhas de login para o usuário `user1`.

## Evidências
- 6 falhas consecutivas em menos de 5 minutos.
- Origem: IP 192.168.0.45.

## Ações tomadas
- Conta bloqueada temporariamente.
- IP adicionado à lista de bloqueio.
- Usuário notificado para redefinição de senha.

## Conclusão
Tentativa de brute force mitigada com sucesso.  
Recomendação: habilitar autenticação multifator (MFA) para todos os usuários.
