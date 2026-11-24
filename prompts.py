def preparar_prompt(meu_campeao: str, campeao_inimigo: str, rota: str) -> str:
    return (
        "Atue como um coach de League of Legends nível Desafiante.\n"
        f"Faça uma análise tática rápida da seguinte matchup: {meu_campeao} (meu campeão) "
        f"contra {campeao_inimigo} (inimigo) na rota {rota}.\n\n"
        "Responda estritamente em português, formatando EXATAMENTE com os 3 tópicos abaixo "
        "(sem texto antes ou depois):\n"
        "- Vantagem Inicial: (explique quem é mais forte nos primeiros níveis)\n"
        "- Condição de Vitória: (explique o que fazer para ganhar a rota)\n"
        "- Cuidado Máximo: (diga qual habilidade inimiga evitar)\n"
    )