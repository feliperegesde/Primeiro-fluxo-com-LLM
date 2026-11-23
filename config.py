import os
from dataclasses import dataclass
from dotenv import load_dotenv
from exceptions import ConfiguracaoError, CredencialAusenteError


@dataclass(frozen=True)
class AppConfig:
    api_key: str
    model_name: str = "gemini-1.5-flash"
    timeout: int = 30
    temperature: float = 0.4


def carregar_configuracao() -> AppConfig:
    load_dotenv(override=True)

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise CredencialAusenteError(
            "Credencial ausente: defina GEMINI_API_KEY no arquivo .env antes de executar."
        )

    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()
    if not model_name:
        raise ConfiguracaoError(
            "Configuração inválida: GEMINI_MODEL não pode ficar vazio."
        )

    timeout_str = os.getenv("GEMINI_TIMEOUT", "30").strip()
    try:
        timeout = int(timeout_str)
        if timeout <= 0:
            raise ValueError
    except ValueError:
        raise ConfiguracaoError(
            "Configuração inválida: GEMINI_TIMEOUT deve ser um número inteiro positivo."
        )

    return AppConfig(
        api_key=api_key,
        model_name=model_name,
        timeout=timeout,
    )