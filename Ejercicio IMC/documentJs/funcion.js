//Definicion de una clase.
class Persona{
  constructor(rut, nombre, apellido, edad, peso, estatura){
    //Atributos
    this.rut = rut;
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
    this.peso = peso;
    this.estatura = estatura;
    this.imc = 0;
    this.estado = "";
  }

  calcImc(){

    this.imc = this.peso / Math.pow(this.estatura, 2);
    this.imc = this.imc.toFixed(2);
  }

  estado1(){

      if(this.imc < 18.50){
      if(this.imc < 16.00){
        this.estado = "Usted Tiene Delgadez Severa";
      }else if(this.imc > 16.00 && this.imc <= 16.99){
        this.estado = "Usted Tiene Delgadez Moderada";            
      }else if(this.imc > 17.00 && this.imc <= 18.49){
        this.estado = "Usted Tiene Delgadez Aceptable";
      }
      this.estado = "Bajo Peso";
    }else if(this.imc > 18.50 && this.imc <= 24.99){
      this.estado = "Ustes Esta En Su Peso Normal";
    }else if(this.imc >= 25.00 && this.imc <= 29.99){
      this.estado = "Usted tiene Pre-obeso (Riesgo)";
    }else if(this.imc >= 30.00){
      if(this.imc > 30.00 && this.imc <= 34.99){
        this.estado = "Usted Tiene Obesidad Tipo I (Riesgo Moderado)";
      }else if(this.imc > 35.00 && this.imc <= 39.99){
        this.estado = "Usted Tiene Obesidad Tipo II (Riesgo Severo)";
      }else if(this.imc >= 40.00){
        this.estado = "Usted Tiene Obesidad Tipo III (Riesgo Muy Severo)";
              
      }
    }
  }

  //Getters

  get getRut(){
    return this.rut;
  }

  get getNombre(){
    return this.nombre;
  }

  get getApellido(){
    return this.apellido;
  }

  get getEdad(){
    return this.edad;
  }

  get getPeso(){
    return this.peso;
  }

  get getEstatura(){
    return this.estatura;
  }


  get getImc(){
    return this.imc;
  }

  get getEstado(){
    return this.estado;
  }


}

//Código principal
//var p1 = new Persona("1-1","Sebastián","Pizarro",37);
//var p2 = new Persona("1-2", "Elena","Nito", 40);

//console.log("Nombre: "+p.nombre+" "+p.apellido);
//console.log("Nombre: "+p2.nombre+" "+p2.apellido);

var personas = [];

//Funcion para agregar personas a la lista.
var agregarPersona = function(){

    var p = new Persona(
      document.getElementById("rut").value,
      document.getElementById("nombre").value,
      document.getElementById("apellido").value,
      parseInt(document.getElementById("edad").value),
      parseFloat(document.getElementById("peso").value),
      parseFloat(document.getElementById("estatura").value),
    );
    document.getElementById("msjAgregado").innerHTML = "Persona Agregada Exitosamente";
    document.getElementById("color").style.backgroundColor = "green";

    p.calcImc();
    p.estado1();
    personas.push(p);
    console.log(personas);

}

var buscarPersona = function(){

  var b = document.getElementById("buscar").value;
  var per =  personas.find(i => i.rut == b);
  if(per != undefined){
    document.getElementById("colormsj").style.background = "green";
    document.getElementById("msj").innerHTML = "Persona Encontrada".toUpperCase();
    document.getElementById("rt").innerHTML = per.rut;
    document.getElementById("nom").innerHTML = per.nombre+" "+per.apellido;
    document.getElementById("ed").innerHTML = per.edad+" Años.";
    document.getElementById("imc").innerHTML = per.getImc;
    document.getElementById("est").innerHTML = per.getEstado;

  }else{
    document.getElementById("colormsj").style.background = "red";
    document.getElementById("msj").innerHTML = "Persona No Encontrada";
    document.getElementById("rt").innerHTML = "";
    document.getElementById("nom").innerHTML = "";
    document.getElementById("ed").innerHTML = "";
    document.getElementById("imc").innerHTML = "";
    document.getElementById("est").innerHTML = "";
  }

}
