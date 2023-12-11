export const HandleForm = ({ form, handleDataForm }) => {
  const campos = [
    'name',
    'radius_mean',
    'texture_mean',
    'perimeter_mean',
    'area_mean',
    'smoothness_mean',
    'compactness_mean',
    'concavity_mean',
    'concave_points_mean',
    'symmetry_mean',
    'fractal_dimension_mean',
    'radius_se',
    'texture_se',
    'perimeter_se',
    'area_se',
    'smoothness_se',
    'compactness_se',
    'concavity_se',
    'concave_points_se',
    'symmetry_se',
    'fractal_dimension_se',
    'radius_worst',
    'texture_worst',
    'perimeter_worst',
    'area_worst',
    'smoothness_worst',
    'compactness_worst',
    'concavity_worst',
    'concave_points_worst',
    'symmetry_worst',
    'fractal_dimension_worst'
  ];

  const label = [
    'Paciente',
    'Raio Médio',
    'Textura Média',
    'Perímetro Médio',
    'Área Média',
    'Suavidade Média',
    'Compacidade Média',
    'Cavidade Média',
    'Pontos Côncavos Médios',
    'Simetria Média',
    'Dimensão Fractal Média',
    'Raio SE',
    'Textura SE',
    'Perímetro SE',
    'Área SE',
    'Suavidade SE',
    'Compacidade SE',
    'Cavidade SE',
    'Pontos Côncavos SE',
    'Simetria SE',
    'Dimensão Fractal SE',
    'Pior Raio',
    'Pior Textura',
    'Pior Perímetro',
    'Pior Área',
    'Pior Suavidade',
    'Pior Compacidade',
    'Pior Cavidade',
    'Piores Pontos Côncavos',
    'Pior Simetria',
    'Pior Dimensão Fractal'
  ];

  const formatarLabel = campo => {
    return campo.replace('_', ' ');
  };

  return (
    <div>
      {campos.map(campo => (
        <div
          key={campo}
          className="flex p-2 border-x-0 border-t-0 border-dashed border-4 justify-between items-center mb-4"
        >
          <label htmlFor={label} className=" text-xl text-gray-600">
            {formatarLabel(label[campos.indexOf(campo)])}{' '}
          </label>
          <input
            type={campo === 'name' ? 'text' : 'float'}
            id={campo}
            name={campo}
            className="px-3 py-2 border rounded"
            required
            value={form[campo]}
            onChange={e => handleDataForm(e)}
          />
        </div>
      ))}
    </div>
  );
};
