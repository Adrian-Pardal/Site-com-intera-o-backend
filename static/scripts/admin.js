










// Uso esse codigo que quando um arquivo for escolido em send files aparecera na tela o nome do arquivo ex: "boleto.pdf" 
   const inputFile = document.getElementById("document-input");
    const labelInputFile = document.getElementById('document-label');

    inputFile.addEventListener("input", () => {
        if (inputFile.files.length > 0) {
            const file = inputFile.files[0];
            labelInputFile.innerText = file.name;
        } else {
            labelInputFile.innerText = "Click to choose file";
        }
    });
// final do COdigo Send Files
//-----------------------------------------------------------------------------------------------------------------------    