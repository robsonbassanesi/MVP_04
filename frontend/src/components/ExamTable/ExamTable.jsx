import { useState, useEffect } from 'react';
import axios from 'axios';
import { HandleForm } from './Elements';

//função para exibir, cadastrar e excluir os exames além de exibi-los
export function ExamTable() {
  const [diagnosis, setDiagnosis] = useState(null);
  const [form, setForm] = useState({});

  const dataForm = e => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  //função para cadastrar um novo exames e enviar para o backend
  async function createExam(e) {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('name', form.name);
      formData.append('radius_mean', form.radius_mean);
      formData.append('texture_mean', form.texture_mean);
      formData.append('perimeter_mean', form.perimeter_mean);
      formData.append('area_mean', form.area_mean);
      formData.append('smoothness_mean', form.smoothness_mean);
      formData.append('compactness_mean', form.compactness_mean);
      formData.append('concavity_mean', form.concavity_mean);
      formData.append('concave_points_mean', form.concave_points_mean);
      formData.append('symmetry_mean', form.symmetry_mean);
      formData.append('fractal_dimension_mean', form.fractal_dimension_mean);
      formData.append('radius_se', form.radius_se);
      formData.append('texture_se', form.texture_se);
      formData.append('perimeter_se', form.perimeter_se);
      formData.append('area_se', form.area_se);
      formData.append('smoothness_se', form.smoothness_se);
      formData.append('compactness_se', form.compactness_se);
      formData.append('concavity_se', form.concavity_se);
      formData.append('concave_points_se', form.concave_points_se);
      formData.append('symmetry_se', form.symmetry_se);
      formData.append('fractal_dimension_se', form.fractal_dimension_se);
      formData.append('radius_worst', form.radius_worst);
      formData.append('texture_worst', form.texture_worst);
      formData.append('perimeter_worst', form.perimeter_worst);
      formData.append('area_worst', form.area_worst);
      formData.append('smoothness_worst', form.smoothness_worst);
      formData.append('compactness_worst', form.compactness_worst);
      formData.append('concavity_worst', form.concavity_worst);
      formData.append('concave_points_worst', form.concave_points_worst);
      formData.append('symmetry_worst', form.symmetry_worst);
      formData.append('fractal_dimension_worst', form.fractal_dimension_worst);

      axios
        .post('http://127.0.0.1:5000/paciente', formData)
        .then(response => {
          console.log(form);
          // O resultado pode ser acessado via response.data
          // Se necessário, você pode manipular ou armazenar o resultado aqui
        })
        .catch(error => {
          console.error('Erro ao enviar o formulário:', error);
        });
    } catch (error) {
      console.error('Erro ao enviar o formulário:', error);
    }
  }

  const fetchDiagnosis = async () => {
    try {
      // Faça uma solicitação GET para a rota correspondente no seu backend
      const response = await axios.get(
        'http://127.0.0.1:5000/obter_resultado_predicao'
      );

      // Se o backend retornar o resultado da predição, armazene no estado
      if (response.data.resultado_predicao !== undefined) {
        setDiagnosis(response.data.resultado_predicao);
      }
    } catch (error) {
      console.error('Erro ao obter o resultado da predição:', error);
    }
  };
  // Chame a função de busca quando o componente for montado
  useEffect(() => {
    fetchDiagnosis();
  }, []); // O segundo argumento vazio [] garante que isso seja executado apenas uma vez, equivalente a componentDidMount

  return (
    <div className="p-8 bg-gray-100 ">
      <div className="flex items-center justify-around">
        <h1 className="text-3xl font-bold ">Predição exames de mama</h1>
      </div>
      <div className=" mt-4 bg-white rounded-lg shadow-md">
        <form onSubmit={createExam} className="p-4">
          <HandleForm form={form} handleDataForm={dataForm} />
          <div className="text-right items-center">
            <button
              type="submit"
              className="items-end px-4 py-2 text-white bg-blue-500 rounded-full"
            >
              Realizar predição
            </button>
          </div>
        </form>
        <div className="text-2xl font-bold flex p-2 border-x-0 border-dashed border-4 justify-around items-center m-4">
          <h1>Resultado da Predição</h1>
          <span>{diagnosis}</span>
        </div>
      </div>
    </div>
  );
}
