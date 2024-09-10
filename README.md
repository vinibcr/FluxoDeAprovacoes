# FluxoDeAprovacoes
API do Jira: Busco automaticamente todos os chamados que necessitam de aprovação e envio e-mails para o superior, incluindo cópias. Análise de Comentários: A solução extrai e-mails de superiores diretamente dos chamados, agilizando o processo de notificação e evitando falhas manuais.  Adiciona comentários automáticos em todos os chamados.

Explicação breve das funções:

buscar_chamados_do_filtro: Busca os chamados abertos no Jira com base em um filtro.
obter_comentarios_chamado: Obtém todos os comentários de um chamado específico.
extrair_email_superior: Extrai o e-mail do superior imediato e um e-mail adicional a partir dos comentários.
adicionar_comentario: Adiciona um comentário no Jira sobre o chamado.
enviar_email: Envia um e-mail relacionado ao chamado para os e-mails extraídos.
email_enviado_hoje: Verifica se o e-mail já foi enviado no dia atual para o chamado.
verificar_chamados_e_iniciar_processo: Função principal que faz toda a verificação e acionamento dos processos de e-mail e comentários.
iniciar_interface_grafica: Configura e controla a interface gráfica com botões para iniciar/parar o programa e exibe logs.
