import os

PROVEEDOR = os.getenv("PROVEEDOR_MODELO", "bedrock")

def get_model():
    """Crea el modelo del asistente según la variable de entorno PROVEEDOR_MODELO.

    Valores soportados: "bedrock" (default), "ollama", "gemini", "openai_compatible".
    """
    if PROVEEDOR == "bedrock":
        from strands.models import BedrockModel
        return BedrockModel(
            model_id=os.getenv("BEDROCK_MODEL_ID", "TU_MODEL_ID"),
            region_name="us-east-2",
            temperature=0.3,
            max_tokens=1024,
        )

    if PROVEEDOR == "ollama":
        from strands.models.ollama import OllamaModel
        return OllamaModel(
            host="http://localhost:11434",
            model_id=os.getenv("OLLAMA_MODEL_ID", "llama3.1"),
        )

    if PROVEEDOR == "gemini":
        from strands.models.gemini import GeminiModel
        return GeminiModel(
            client_args={"api_key": os.environ["GEMINI_API_KEY"]},
            model_id="gemini-2.5-flash",
            params={"temperature": 0.3},
        )

    if PROVEEDOR == "openai_compatible":
        # Sirve para Groq, OpenRouter, GitHub Models, Cerebras... (ver la guía de la descripción)
        from strands.models.openai import OpenAIModel
        return OpenAIModel(
            client_args={
                "api_key": os.environ["OPENAI_COMPAT_API_KEY"],
                "base_url": os.environ["OPENAI_COMPAT_BASE_URL"],
            },
            model_id=os.environ["OPENAI_COMPAT_MODEL_ID"],
            params={"temperature": 0.3, "max_tokens": 1024},
        )

    raise ValueError(
        f"PROVEEDOR_MODELO='{PROVEEDOR}' no soportado. "
        "Usa: bedrock, ollama, gemini u openai_compatible."
    )