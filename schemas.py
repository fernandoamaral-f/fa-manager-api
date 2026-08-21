import re

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class Cliente(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nome: str = Field(min_length=2, max_length=100)
    idade: int = Field(gt=0, le=120)
    email: EmailStr
    telefone: str = Field(pattern=r"^\d{10,11}$")

    @field_validator("telefone", mode="before")
    @classmethod
    def limpar_telefone(cls, valor):
        if isinstance(valor, str):
            if not re.fullmatch(r"[\d\s()+-]+", valor):
                raise ValueError("Telefone contém caracteres inválidos")

            return re.sub(r"\D", "", valor)

        return valor