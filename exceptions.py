class MatchupCoachError(Exception):
    """Erro base da aplicação."""


class ConfiguracaoError(MatchupCoachError):
    """Configuração de acesso ausente ou inválida."""


class CredencialAusenteError(ConfiguracaoError):
    """Chave de API não encontrada no ambiente."""


class CredencialInvalidaError(MatchupCoachError):
    """Chave de API rejeitada pelo provedor."""


class ServicoIndisponivelError(MatchupCoachError):
    """Serviço do LLM temporariamente indisponível ou limite atingido."""


class FalhaComunicacaoError(MatchupCoachError):
    """Falha de rede ou comunicação com a API."""


class TimeoutLLMError(MatchupCoachError):
    """Tempo limite excedido ao aguardar resposta do LLM."""


class RespostaInvalidaError(MatchupCoachError):
    """Resposta vazia, bloqueada ou em formato inesperado."""