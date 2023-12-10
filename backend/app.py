from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Paciente, Model
from logger import logger
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

# Rota de listagem de pacientes


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteSchema, "404": ErrorSchema})
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
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.

    Args:
        name (str): nome do paciente
        radius_mean (float): média dos raios
        texture_mean (float): média da textura
        perimeter_mean (float): média do perímetro
        area_mean (float): média da área
        smoothness_mean (float): média da suavidade
        compactness_mean (float): média da compacidade
        concavity_mean (float): média da concavidade
        concave_points_mean (float): média dos pontos côncavos
        symmetry_mean (float): média da simetria
        fractal_dimension_mean (float): média da dimensão fractal
        radius_se (float): erro padrão do raio
        texture_se (float): erro padrão da textura
        perimeter_se (float): erro padrão do perímetro
        area_se (float): erro padrão da área
        smoothness_se (float): erro padrão da suavidade
        compactness_se (float): erro padrão da compacidade
        concavity_se (float): erro padrão da concavidade
        concave_points_se (float): erro padrão dos pontos côncavos
        symmetry_se (float): erro padrão da simetria
        fractal_dimension_se (float): erro padrão da dimensão fractal
        radius_worst (float): pior valor do raio
        texture_worst (float): pior valor da textura
        perimeter_worst (float): pior valor do perímetro
        area_worst (float): pior valor da área
        smoothness_worst (float): pior valor da suavidade
        compactness_worst (float): pior valor da compacidade
        concavity_worst (float): pior valor da concavidade
        concave_points_worst (float): pior valor dos pontos côncavos
        symmetry_worst (float): pior valor da simetria
        fractal_dimension_worst (float): pior valor da dimensão fractal
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
# Carregando modelo
    path = 'modelo/modelo_finalizado.pkl'
    modelo = Model.carrega_modelo(path)
    try:
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

        print(paciente)
        logger.debug(f"Adicionando paciente de nome: '{paciente.name}'")

        # Criando conexão com a base
        session = Session()
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        # Caso a adição ocorra com sucesso
        return apresenta_paciente(paciente), 200

    # Caso ocorra algum erro na adição
    except IntegrityError as e:
        error_msg = "Erro de integridade, verifique os valores inseridos"
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(
            f"Erro ao adicionar paciente '{paciente.name}', {error_msg}, {str(e)}")
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
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(
        Paciente.name == paciente_nome).first()

    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(
            f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
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
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")

    # Criando conexão com a base
    session = Session()

    # Buscando paciente
    paciente = session.query(Paciente).filter(
        Paciente.name == paciente_nome).first()

    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(
            f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200
