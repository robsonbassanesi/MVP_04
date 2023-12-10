from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np


class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Pedro"
    radius_mean: float = 17.99
    texture_mean: float = 10.38
    perimeter_mean: float = 122.8
    area_mean: float = 1001
    smoothness_mean: float = 0.1184
    compactness_mean: float = 0.2776
    concavity_mean: float = 0.3001
    concave_points_mean: float = 0.1471
    symmetry_mean: float = 0.2419
    fractal_dimension_mean: float = 0.07871
    radius_se: float = 1.095
    texture_se: float = 0.9053
    perimeter_se: float = 8.589
    area_se: float = 153.4
    smoothness_se: float = 0.006399
    compactness_se: float = 0.04904
    concavity_se: float = 0.05373
    concave_points_se: float = 0.01587
    symmetry_se: float = 0.03003
    fractal_dimension_se: float = 0.006193
    radius_worst: float = 25.38
    texture_worst: float = 17.33
    perimeter_worst: float = 184.6
    area_worst: float = 2019
    smoothness_worst: float = 0.1622
    compactness_worst: float = 0.6656
    concavity_worst: float = 0.7119
    concave_points_worst: float = 0.2654
    symmetry_worst: float = 0.4601
    fractal_dimension_worst: float = 0.1189


class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Pedro"
    radius_mean: float = 17.99
    texture_mean: float = 10.38
    perimeter_mean: float = 122.8
    area_mean: float = 1001
    smoothness_mean: float = 0.1184
    compactness_mean: float = 0.2776
    concavity_mean: float = 0.3001
    concave_points_mean: float = 0.1471
    symmetry_mean: float = 0.2419
    fractal_dimension_mean: float = 0.07871
    radius_se: float = 1.095
    texture_se: float = 0.9053
    perimeter_se: float = 8.589
    area_se: float = 153.4
    smoothness_se: float = 0.006399
    compactness_se: float = 0.04904
    concavity_se: float = 0.05373
    concave_points_se: float = 0.01587
    symmetry_se: float = 0.03003
    fractal_dimension_se: float = 0.006193
    radius_worst: float = 25.38
    texture_worst: float = 17.33
    perimeter_worst: float = 184.6
    area_worst: float = 2019
    smoothness_worst: float = 0.1622
    compactness_worst: float = 0.6656
    concavity_worst: float = 0.7119
    concave_points_worst: float = 0.2654
    symmetry_worst: float = 0.4601
    fractal_dimension_worst: float = 0.1189
    outcome: int = None


class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Pedro"


class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]


class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Pedro"

# Apresenta apenas os dados de um paciente


def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "radius_mean": paciente.radius_mean,
        "texture_mean": paciente.texture_mean,
        "perimeter_mean": paciente.perimeter_mean,
        "area_mean": paciente.area_mean,
        "smoothness_mean": paciente.smoothness_mean,
        "compactness_mean": paciente.compactness_mean,
        "concavity_mean": paciente.concavity_mean,
        "concave_points_mean": paciente.concave_points_mean,
        "symmetry_mean": paciente.symmetry_mean,
        "fractal_dimension_mean": paciente.fractal_dimension_mean,
        "radius_se": paciente.radius_se,
        "texture_se": paciente.texture_se,
        "perimeter_se": paciente.perimeter_se,
        "area_se": paciente.area_se,
        "smoothness_se": paciente.smoothness_se,
        "compactness_se": paciente.compactness_se,
        "concavity_se": paciente.concavity_se,
        "concave_points_se": paciente.concave_points_se,
        "symmetry_se": paciente.symmetry_se,
        "fractal_dimension_se": paciente.fractal_dimension_se,
        "radius_worst": paciente.radius_worst,
        "texture_worst": paciente.texture_worst,
        "perimeter_worst": paciente.perimeter_worst,
        "area_worst": paciente.area_worst,
        "smoothness_worst": paciente.smoothness_worst,
        "compactness_worst": paciente.compactness_worst,
        "concavity_worst": paciente.concavity_worst,
        "concave_points_worst": paciente.concave_points_worst,
        "symmetry_worst": paciente.symmetry_worst,
        "fractal_dimension_worst": paciente.fractal_dimension_worst,
        # "outcome": paciente.outcome
    }
# Apresenta uma lista de pacientes


def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "radius_mean": paciente.radius_mean,
            "texture_mean": paciente.texture_mean,
            "perimeter_mean": paciente.perimeter_mean,
            "area_mean": paciente.area_mean,
            "smoothness_mean": paciente.smoothness_mean,
            "compactness_mean": paciente.compactness_mean,
            "concavity_mean": paciente.concavity_mean,
            "concave_points_mean": paciente.concave_points_mean,
            "symmetry_mean": paciente.symmetry_mean,
            "fractal_dimension_mean": paciente.fractal_dimension_mean,
            "radius_se": paciente.radius_se,
            "texture_se": paciente.texture_se,
            "perimeter_se": paciente.perimeter_se,
            "area_se": paciente.area_se,
            "smoothness_se": paciente.smoothness_se,
            "compactness_se": paciente.compactness_se,
            "concavity_se": paciente.concavity_se,
            "concave_points_se": paciente.concave_points_se,
            "symmetry_se": paciente.symmetry_se,
            "fractal_dimension_se": paciente.fractal_dimension_se,
            "radius_worst": paciente.radius_worst,
            "texture_worst": paciente.texture_worst,
            "perimeter_worst": paciente.perimeter_worst,
            "area_worst": paciente.area_worst,
            "smoothness_worst": paciente.smoothness_worst,
            "compactness_worst": paciente.compactness_worst,
            "concavity_worst": paciente.concavity_worst,
            "concave_points_worst": paciente.concave_points_worst,
            "symmetry_worst": paciente.symmetry_worst,
            "fractal_dimension_worst": paciente.fractal_dimension_worst,
            # "outcome": paciente.outcome
        })

    return {"pacientes": result}
