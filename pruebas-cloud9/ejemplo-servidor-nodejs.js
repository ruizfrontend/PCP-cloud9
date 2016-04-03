// módulos requeridos
var http = require('http');

// Código a ejecutar cada vez que se solicite una página
function handleRequest(request, response){
    response.end('Hello server! Url solicitada: ' + request.url);
}

// Crea el server ...
var server = http.createServer(handleRequest);

// y lo inicia
server.listen(8080, function(){
    // Callback lanzado al iniciar el servidor
    console.log('Servidor iniciado');
});