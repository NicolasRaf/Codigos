import { readdir } from 'fs/promises';
import { stat } from 'fs/promises';
import path from 'path';

async function listarArquivos() {
    let allFiles = ""

  try {
    // Obtém o diretório de trabalho atual
    const pasta = process.cwd();

    // Lê os arquivos na pasta
    const files = await readdir(pasta);

    for (const file of files) {
      const filePath = path.join(pasta, file);
      const fileStat = await stat(filePath);

      if (fileStat.isFile()) {
        allFiles += file + "\n"
      }
    }
  } catch (err) {
    console.error('Erro ao ler a pasta:', err);
  }
  console.log(allFiles)
}

listarArquivos();
