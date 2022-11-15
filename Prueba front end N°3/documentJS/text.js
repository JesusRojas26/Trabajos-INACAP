// CLASS PERSONA
class Persona{

  constructor(rut , nombre , apellido , edad , correo , pais){

    this.rut = rut;
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
    this.correo = correo;
    this.pais = pais;

  }

  //Get
  get getRut(){
    return this.rut ;
  }
  get getNombre(){
    return this.nombre ;
  }
  get getApellido(){
    return this.apellido ;
  }
  get getEdad(){
    return this.edad ;
  }
  get getCorreo(){
    return this.correo ;
  }
  get getPais(){
    return this.pais ;
  }

  //Set
  set setRut(rut){
    this.rut = rut;
  }
  set setNombre(nomre){
    this.nombre = nombre;
  }
  set setApellido(apellido){
    this.apellido = apellido;
  }
  set setEdad(edad){
    this.edad = edad;
  }
  set setCorreo(correo){
    this.correo = correo;
  }
  set setPais(pais){
    this.pais = pais;
  }

}
 // CLASS INSCRIPCIÓN
class Inscripcion{

  constructor(idd , persona , tour , valorBase , seguro , valorFinal){

    this.idd = idd;
    this.persona = persona;
    this.tour = tour;
    this.valorBase = valorBase;
    this.seguro = seguro;
    this.valorFinal = valorFinal;
    this.descuento = 0;
    this.iva = 0;

  }

  //Get
  get getIdd(){
    return this.idd ;
  }
  get getPersona(){
    return this.persona ;
  }
  get getTour(){
    return this.tour ;
  }
  get getValorBase(){
    return this.valorBase ;
  }
  get getSeguro(){
    return this.seguro ;
  }
  get getValorFinal(){
    return this.valorFinal ;
  }
  get getDescuento(){
    return this.descuento ;
  }
  get getIva(){
    return this.iva ;
  }

  //Set
  set setIdd(idd){
    this.idd = idd;
  }
  set setPersona(persona){
    this.persona = persona;
  }
  set setTour(Tour){
    this.tour = tour;
  }
  set setValorBase(valorBase){
    this.valorBase = valorBase;
  }
  set setSeguro(seguro){
    this.seguro = seguro;
  }
  set setValorFinal(valorFinal){
    this.valorFinal = valorFinal;
  }
  set setDescuento(descuento){
    this.descuento = descuento;
  }
  set setIva(iva){
    this.iva = iva;
  }

  descuentosTour(){
    if(this.persona.edad < 18){
      this.descuento = this.tour.valorBase * 0.2;
    }else if(this.persona.edad > 60){
      this.descuento = this.tour.valorBase * 0.3;
    }
  }

  valorBase1(){
    this.valorBase = this.tour.valorBase
  }

  seguroTour(){
    this.seguro = this.tour.valorBase * 0.05;
  }

  valorIvaTour(){
    this.iva = this.tour.valorBase * 0.19;
  }

  valorFinalTour(){
    this.valorFinal = (this.tour.valorBase + this.iva) - this.descuento;
  }

}

// CLASS TOUR
class Tour{

  constructor(id, nombre, valorBase){

      this.id = id;
      this.nombre = nombre;
      this.valorBase = valorBase;

  }

  //Get
  get getId(){
      return this.id;
  }
  get getNombre(){
      return this.nombre;
  }
  get getValorBase(){
      return this.valorBase;
  }

}

//LISTA
var listaPersona = [];
var listaTour = [];
var listaInscripcion = [];

// LISTA_TOUR_PRE-CARGADOS
var tour1 = new Tour(1,"Valle de la Luna",37.5);
var tour2 = new Tour(2,"Geyers del Tatio",69);
var tour3 = new Tour(3,"Laguna Cejar, Ojos del Salado",55);


listaTour = [tour1,tour2,tour3];

//EJECUTADOR POR CONSOLA
console.log(listaTour);
console.log(listaPersona);
console.log(listaInscripcion);

//VARIABLE ALERT CON BOOTSTRAP
var colorAlert;

//FUNCION PARA GUARDAR REGISTRO DE PERSONA
var guardarPersona = function(){

  //CONDICION PARA COMPLETAR TODOS LOS CAMPOS 
  if(
    document.getElementById("rutP").value == "" ||
    document.getElementById("nombreP").value == ""||
    document.getElementById("apellidoP").value == ""||
    document.getElementById("edadP").value == ""||
    document.getElementById("correoP").value == ""||
    document.getElementById("paisP").value ==""
  ){
    //ALERT EN CASO DE NO COMPLETAR LAS CONDICIONES
    colorAlert = "alert alert-danger";
    document.getElementById("all").innerHTML = "Error Debe Ingresar Todos Los Datos REINTENTE...."
    document.getElementById("colorChange").className = colorAlert;
  }else{

    //VARIABLE PARA AGREGAR PERSONA A LA LISTA
    var p = new Persona(



      document.getElementById("rutP").value,
      document.getElementById("nombreP").value,
      document.getElementById("apellidoP").value,
      parseInt(document.getElementById("edadP").value),
      document.getElementById("correoP").value,
      document.getElementById("paisP").value,
    
    )

    colorAlert = "";
    document.getElementById("all").innerHTML = "";
    document.getElementById("colorChange").className = "";
   
    listaPersona.push(p)
    console.log(listaPersona)
  }

}


//FUNCION PARA GUARDAR REGISTRO DE INSCRIPCION
var guardarInscripcion = function(){

  //CONDICION PARA COMPLETAR TODOS LOS CAMPOS 
  if(
    document.getElementById("buscar").value == ""||
    document.getElementById("buscart").value == ""||
    document.getElementById("id").value == ""
  ){
    //ALERT EN CASO DE NO COMPLETAR LAS CONDICIONES
    colorAlert = "alert alert-danger";
    document.getElementById("all1").innerHTML = "Error Debe Ingresar Todos Los Datos REINTENTE...."
    document.getElementById("colorChange1").className = colorAlert;
  }else{

    //VAIABLE PARA BUSCAR EL RUT DE PERSONA
    var b = document.getElementById("buscar").value;
    var per =  listaPersona.find(i => i.rut == b);
    //VAIABLE PARA BUSCAR EL ID DE TOUR
    var t = document.getElementById("buscart").value;
    var tur = listaTour.find(i => i.id == t);

    var vbt = tur.getValorBase;

    var ins = new Inscripcion(
    document.getElementById("id").value,
    per,
    tur,
    vbt
  );

  colorAlert = "";
  document.getElementById("all1").innerHTML = "";
  document.getElementById("colorChange1").className = "";

  ins.valorBase1();
  ins.descuentosTour();
  ins.seguroTour();
  ins.valorIvaTour();
  ins.valorFinalTour();
  listaInscripcion.push(ins);
  crearLista();
  console.log(listaInscripcion)
  }


}


//FUNCION DE BUSQUEDA DE LAS INSCRIPCIONES
var buscarInscripcion = function(){

  //CONDICION PARA COMPLETAR TODOS LOS CAMPOS 
  if(
    document.getElementById("buscarins").value == ""
  ){
    //ALERT EN CASO DE NO COMPLETAR LAS CONDICIONES
    colorAlert = "alert alert-danger";
    document.getElementById("all2").innerHTML = "Error Debe Ingresar Todos Los Datos REINTENTE...."
    document.getElementById("colorChange2").className = colorAlert;
  }else{

    //BUSCADOR DE ID DE LA INSCRIPCIÓN
    var bI = document.getElementById("buscarins").value;
    var inscripcion1 =  listaInscripcion.find(i => i.idd == bI);
    if(inscripcion1 != undefined){
      document.getElementById("idI").innerHTML = inscripcion1.getIdd;
      document.getElementById("personaI").innerHTML = inscripcion1.getPersona.getNombre +" "+ inscripcion1.getPersona.getApellido;
      document.getElementById("tourI").innerHTML = inscripcion1.getTour.getNombre;
      document.getElementById("valorbaseI").innerHTML = "$" + inscripcion1.getTour.valorBase * 850;
      document.getElementById("descuentoI").innerHTML = "$" + inscripcion1.getDescuento * 850;
      document.getElementById("seguroI").innerHTML = "$" + inscripcion1.getSeguro * 850;
      document.getElementById("ivaI").innerHTML = "$" + inscripcion1.getIva * 850;
      document.getElementById("valorfinalI").innerHTML = "$" + inscripcion1.getValorFinal * 850;
      document.getElementById("all3").innerHTML = "";
      document.getElementById("colorChange3").className = "";

    }else{

      colorAlert = "alert alert-danger";
      document.getElementById("all3").innerHTML = "N° De Ficha No Encontrado REINTENTE...."
      document.getElementById("colorChange3").className = colorAlert;

      document.getElementById("idI").innerHTML = "";
      document.getElementById("personaI").innerHTML = "";
      document.getElementById("tourI").innerHTML = "";
      document.getElementById("valorbaseI").innerHTML = "";
      document.getElementById("descuentoI").innerHTML = "";
      document.getElementById("seguroI").innerHTML = "";
      document.getElementById("ivaI").innerHTML = "";
      document.getElementById("valorfinalI").innerHTML = "";
    }

    colorAlert = "";
    document.getElementById("all2").innerHTML = "";
    document.getElementById("colorChange2").className = "";
  }

  
}

//FUNCION PARA CREAR LA LISTA
var crearLista = function(){

  document.getElementById("laLista").innerHTML = "";
  var miLista = document.createElement("ul");

  for (let index = 0; index < listaInscripcion.length; index++) {
    
    var item = document.createElement("li");
    item.innerHTML = "Rut: "+ listaInscripcion[index].getPersona.getRut +", Nombre: "+ listaInscripcion[index].getPersona.getNombre+" "+ listaInscripcion[index].getPersona.getApellido+", Edad: "+ listaInscripcion[index].getPersona.getEdad+" | Tour: "+ listaInscripcion[index].getTour.getNombre+", Valor Base: $"+listaInscripcion[index].getTour.getValorBase*850;

    miLista.appendChild(item);
    
  }

  colorAlert = "alert alert-info";
  document.getElementById("colorAlertLista").className = colorAlert;
  document.getElementById("laLista").appendChild(miLista);

}
