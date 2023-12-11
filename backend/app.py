from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from flask import request
from model import Session, Paciente, Model
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(
    name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.

    Args:
        nome (str): nome do paciente

    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()

    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()

    if not pacientes:
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict():
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.

    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    form_data = request.form
    form = PacienteSchema(**form_data)
    # Carregando modelo
    path = 'modelo/modelo_finalizado.pkl'
    modelo = Model.carrega_modelo(path)

    paciente = Paciente(
        name=form.name.strip(),
        radius_mean=form.radius_mean,
        texture_mean=form.texture_mean,
        perimeter_mean=form.perimeter_mean,
        area_mean=form.area_mean,
        smoothness_mean=form.smoothness_mean,
        compactness_mean=form.compactness_mean,
        concavity_mean=form.concavity_mean,
        concave_points_mean=form.concave_points_mean,
        symmetry_mean=form.symmetry_mean,
        fractal_dimension_mean=form.fractal_dimension_mean,
        radius_se=form.radius_se,
        texture_se=form.texture_se,
        perimeter_se=form.perimeter_se,
        area_se=form.area_se,
        smoothness_se=form.smoothness_se,
        compactness_se=form.compactness_se,
        concavity_se=form.concavity_se,
        concave_points_se=form.concave_points_se,
        symmetry_se=form.symmetry_se,
        fractal_dimension_se=form.fractal_dimension_se,
        radius_worst=form.radius_worst,
        texture_worst=form.texture_worst,
        perimeter_worst=form.perimeter_worst,
        area_worst=form.area_worst,
        smoothness_worst=form.smoothness_worst,
        compactness_worst=form.compactness_worst,
        concavity_worst=form.concavity_worst,
        concave_points_worst=form.concave_points_worst,
        symmetry_worst=form.symmetry_worst,
        fractal_dimension_worst=form.fractal_dimension_worst,
        outcome=Model.preditor(modelo, form)
    )

    try:
        # Criando conexão com a base
        session = Session()

        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            return {"message": error_msg}, 409

        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        return apresenta_paciente(paciente), 200

    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400


# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente

    Returns:
        dict: representação do paciente e diagnóstico associado
    """

    paciente_nome = query.name
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(
        Paciente.name == paciente_nome).first()

    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200


# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente

    Returns:
        msg: Mensagem de sucesso ou erro
    """

    paciente_nome = unquote(query.name)

    # Criando conexão com a base
    session = Session()

    # Buscando paciente
    paciente = session.query(Paciente).filter(
        Paciente.name == paciente_nome).first()

    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200
