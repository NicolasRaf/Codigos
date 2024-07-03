const notas = {
    "História da Computação": [8, 2, 9, 1, 10, 5, 5, 6, 5, 1],
    "Estatística": [8, 2, 4, 7, 4, 6, 5, 6, 8, 3],
    "TCC": [8, 1, 3, 6, 5, 8, 6, 7, 8, 4]
  };
  
  function calcularMedia(notas) {
    const soma = notas.reduce((acc, nota) => acc + nota, 0);
    return soma / notas.length;
  }
  
  function calcularVariancia(notas) {
    const media = calcularMedia(notas);
    const somaDiferencasQuadradas = notas.reduce((acc, nota) => acc + Math.pow(nota - media, 2), 0);
    return somaDiferencasQuadradas / notas.length;
  }
  
  for (const materia in notas) {
    const media = calcularMedia(notas[materia]);
    const variancia = calcularVariancia(notas[materia]);
    console.log(`Média de ${materia}: ${media.toFixed(2)}`);
    console.log(`Variância de ${materia}: ${variancia.toFixed(2)}`);
    console.log("");
  }
  