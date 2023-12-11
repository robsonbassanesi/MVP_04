from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from datetime import datetime
from model import Base


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    radius_mean = Column("radius_mean", Float)
    texture_mean = Column("texture_mean", Float)
    perimeter_mean = Column("perimeter_mean", Float)
    area_mean = Column("area_mean", Float)
    smoothness_mean = Column("smoothness_mean", Float)
    compactness_mean = Column("compactness_mean", Float)
    concavity_mean = Column("concavity_mean", Float)
    concave_points_mean = Column("concave_points_mean", Float)
    symmetry_mean = Column("symmetry_mean", Float)
    fractal_dimension_mean = Column("fractal_dimension_mean", Float)
    radius_se = Column("radius_se", Float)
    texture_se = Column("texture_se", Float)
    perimeter_se = Column("perimeter_se", Float)
    area_se = Column("area_se", Float)
    smoothness_se = Column("smoothness_se", Float)
    compactness_se = Column("compactness_se", Float)
    concavity_se = Column("concavity_se", Float)
    concave_points_se = Column("concave_points_se", Float)
    symmetry_se = Column("symmetry_se", Float)
    fractal_dimension_se = Column("fractal_dimension_se", Float)
    radius_worst = Column("radius_worst", Float)
    texture_worst = Column("texture_worst", Float)
    perimeter_worst = Column("perimeter_worst", Float)
    area_worst = Column("area_worst", Float)
    smoothness_worst = Column("smoothness_worst", Float)
    compactness_worst = Column("compactness_worst", Float)
    concavity_worst = Column("concavity_worst", Float)
    concave_points_worst = Column("concave_points_worst", Float)
    symmetry_worst = Column("symmetry_worst", Float)
    fractal_dimension_worst = Column("fractal_dimension_worst", Float)
    outcome = Column("Diagnostic", Integer)
    data_insercao = Column(DateTime, default=datetime.now())


class Paciente:
    def __init__(self, name: str, radius_mean: float, texture_mean: float,
                 perimeter_mean: float, area_mean: float, smoothness_mean: float,
                 compactness_mean: float, concavity_mean: float, concave_points_mean: float,
                 symmetry_mean: float, fractal_dimension_mean: float, radius_se: float,
                 texture_se: float, perimeter_se: float, area_se: float, smoothness_se: float,
                 compactness_se: float, concavity_se: float, concave_points_se: float,
                 symmetry_se: float, fractal_dimension_se: float, radius_worst: float,
                 texture_worst: float, perimeter_worst: float, area_worst: float,
                 smoothness_worst: float, compactness_worst: float, concavity_worst: float,
                 concave_points_worst: float, symmetry_worst: float,
                 fractal_dimension_worst: float, outcome: int,
                 data_insercao: Union[datetime, None] = None):
        """
        Cria um Paciente

        Arguments:
        name: nome do paciente
        radius_mean: média do raio
        texture_mean: média da textura
        perimeter_mean: média do perímetro
        area_mean: média da área
        smoothness_mean: média da suavidade
        compactness_mean: média da compacidade
        concavity_mean: média da concavidade
        concave_points_mean: média dos pontos côncavos
        symmetry_mean: média da simetria
        fractal_dimension_mean: média da dimensão fractal
        radius_se: erro padrão do raio
        texture_se: erro padrão da textura
        perimeter_se: erro padrão do perímetro
        area_se: erro padrão da área
        smoothness_se: erro padrão da suavidade
        compactness_se: erro padrão da compacidade
        concavity_se: erro padrão da concavidade
        concave_points_se: erro padrão dos pontos côncavos
        symmetry_se: erro padrão da simetria
        fractal_dimension_se: erro padrão da dimensão fractal
        radius_worst: pior valor do raio
        texture_worst: pior valor da textura
        perimeter_worst: pior valor do perímetro
        area_worst: pior valor da área
        smoothness_worst: pior valor da suavidade
        compactness_worst: pior valor da compacidade
        concavity_worst: pior valor da concavidade
        concave_points_worst: pior valor dos pontos côncavos
        symmetry_worst: pior valor da simetria
        fractal_dimension_worst: pior valor da dimensão fractal
        data_insercao: data de quando o paciente foi inserido à base
        outcome: diagnóstico
        """
        self.name = name
        self.radius_mean = radius_mean
        self.texture_mean = texture_mean
        self.perimeter_mean = perimeter_mean
        self.area_mean = area_mean
        self.smoothness_mean = smoothness_mean
        self.compactness_mean = compactness_mean
        self.concavity_mean = concavity_mean
        self.concave_points_mean = concave_points_mean
        self.symmetry_mean = symmetry_mean
        self.fractal_dimension_mean = fractal_dimension_mean
        self.radius_se = radius_se
        self.texture_se = texture_se
        self.perimeter_se = perimeter_se
        self.area_se = area_se
        self.smoothness_se = smoothness_se
        self.compactness_se = compactness_se
        self.concavity_se = concavity_se
        self.concave_points_se = concave_points_se
        self.symmetry_se = symmetry_se
        self.fractal_dimension_se = fractal_dimension_se
        self.radius_worst = radius_worst
        self.texture_worst = texture_worst
        self.perimeter_worst = perimeter_worst
        self.area_worst = area_worst
        self.smoothness_worst = smoothness_worst
        self.compactness_worst = compactness_worst
        self.concavity_worst = concavity_worst
        self.concave_points_worst = concave_points_worst
        self.symmetry_worst = symmetry_worst
        self.fractal_dimension_worst = fractal_dimension_worst
        self.outcome = outcome

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
