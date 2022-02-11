

cargarReloj = () =>{
  let fechaHora = new Date();

  let hora = fechaHora.getHours();
  let minuto = fechaHora.getMinutes();
  let segundo = fechaHora.getSeconds();
  
  hora = (hora < 10) ? "0" + hora : hora;
  minuto = (minuto < 10) ? "0" + minuto : minuto;
  segundo = (segundo < 10) ? "0" + segundo : segundo;

  const relojDigital = hora +":"+ minuto + ":"+ segundo

  document.getElementById("relojnumerico").textContent = relojDigital;
  
  setTimeout(cargarReloj,500)
}

cargarReloj();



console.log('El reloj esta haciendo las manijas')