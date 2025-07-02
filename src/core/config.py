from pydantic import BaseModel


class Coefficient(BaseModel):
    inertia: float
    cognitive: float
    social: float
    repel: float


class Patience(BaseModel):
    _base: float
    restart: float


class Config(BaseModel):
    swarm_size: int
    step_length: int
    step_length_schedule: int
    max_iter: int
    coefficient: Coefficient
    patience: Patience
