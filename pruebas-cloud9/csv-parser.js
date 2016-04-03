    // librerías necesarias
var csv = require('csv');
var fs = require('fs');

    // nombre del archivo a procesar
var file = './FL_insurance_sample.csv';

    // function parseador
var parser = csv.parse({delimiter: ','}, function (err, data) {
    
    if(err) return;
        
        // variable donde almacenaremos el resultado    
    var output = [];
    
        // recorremos los datos
    for (var i = 0; i < data.length; i++) {
        
            // añado la cabecera
        if (i == 0) {
            output.push(data[i]);
            
            // y otras 5 lineas más
        } else if (i <= 5) {
            output.push(data[i]);
        }
    }
    
        // muestra el resultado
    console.log(output);
});

    // Lee el archivo y pasa como callback la funciona parseadora
fs.createReadStream(file).pipe(parser);