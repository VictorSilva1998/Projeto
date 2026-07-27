from pathlib import Path

BASE_DIR = Path (__file__).resolve ().parent.parent
IMAGEM_LOGIN = BASE_DIR / "login.png"
IMAGEM_PERFIL = BASE_DIR / "Foto de Perfil.jpg"

__all__ = ["BASE_DIR", "IMAGEM_LOGIN", "IMAGEM_PERFIL"]