const os = require('os');
//console.log(os.cpus())

var memoriaLibre =os.freemem();

function convertidor(x1){
    return x1/1000000000

}
var memFinal=(convertidor(memoriaLibre));
console.log("la memoria libre que tienes es " + memFinal+"GB")