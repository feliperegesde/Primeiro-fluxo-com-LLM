import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

from config import AppConfig
from exceptions import (
    CredencialInvalidaError,
    FalhaComunicacaoError,
    RespostaInvalidaError,
    ServicoIndisponivelError,
    TimeoutLLMError,
)


def chamar_modelo(prompt: str, config: AppConfig):
    genai.configure(api_key=config.api_key)
    model = genai.GenerativeModel(config.model_name)

    try:
        return model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=config.temperature
            ),
            request_options={"timeout": config.timeout},
        )
    except google_exceptions.DeadlineExceeded as exc:
        raise TimeoutLLMError(
            f"O serviço demorou mais de {config.timeout}s para responder (timeout). Tente novamente."
        ) from exc
    except (google_exceptions.Unauthenticated, google_exceptions.PermissionDenied) as exc:
        raise CredencialInvalidaError(
            "Credencial inválida ou sem permissão. Verifique sua GEMINI_API_KEY no arquivo .env."
        ) from exc
    except google_exceptions.InvalidArgument as exc:
        if "api key" in str(exc).lower():
            raise CredencialInvalidaError(
                "Credencial inválida: a chave informada no .env foi rejeitada pelo provedor."
            ) from exc
        raise FalhaComunicacaoError(
            "A solicitação foi recusada pelo serviço por conter parâmetros inválidos."
        ) from exc
    except (google_exceptions.ServiceUnavailable, google_exceptions.ResourceExhausted) as exc:
        raise ServicoIndisponivelError(
            "O serviço do LLM está temporariamente indisponível ou atingiu o limite de requisições. Tente mais tarde."
        ) from exc
    except (google_exceptions.GoogleAPICallError, ConnectionError, OSError) as exc:
        raise FalhaComunicacaoError(
            "Falha de comunicação com o serviço do LLM. Verifique sua conexão com a internet."
        ) from exc
    except Exception as exc:
        raise FalhaComunicacaoError(
            "Ocorreu uma falha inesperada ao se comunicar com o serviço do LLM."
        ) from exc


def tratar_resposta(response) -> str:
    if response is None:
        raise RespostaInvalidaError("O modelo não retornou nenhuma resposta.")

    try:
        texto = (response.text or "").strip()
    except ValueError as exc:
        raise RespostaInvalidaError(
            "A resposta foi bloqueada ou retornada em formato inesperado pelo modelo."
        ) from exc

    if not texto:
        raise RespostaInvalidaError("O modelo retornou uma resposta vazia.")

    return texto