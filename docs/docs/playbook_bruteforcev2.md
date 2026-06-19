# Playbook de Resposta a Brute Force

## Objetivo
Detectar e responder a tentativas de acesso não autorizado por força bruta.

## Escopo
Este playbook se aplica a incidentes de autenticação em sistemas internos.

## Passos de Resposta
1. **Detecção**  
   - Identificar usuários com múltiplas falhas de login em curto período.
   - Confirmar origem (IP, dispositivo).

2. **Contenção**  
   - Bloquear temporariamente a conta suspeita.
   - Adicionar IP à lista de bloqueio.

3. **Erradicação**  
   - Revisar logs para confirmar se não houve acesso bem-sucedido.
   - Alterar credenciais comprometidas.

4. **Recuperação**  
   - Liberar conta após redefinição de senha.
   - Implementar autenticação multifator (MFA).

5. **Lições aprendidas**  
   - Documentar o incidente.
   - Atualizar regras de monitoramento.
