$(document).ready(function () {
	console.log("Hello World!");
	e = $("#nbHabitants");
	
	$.get("/affiche_hab").done(function (data) {
		$("#nbHabitants").text(data);
	});
	$.get("/affiche_maisons").done(function (data) {
		$("#nbMaisons").text(data);
	});
	
	$.get("/affiche_nbFer").done(function (data) {
		$("#nbFer").text(data);
	});
	$.get("/affiche_nbNouritture").done(function (data) {
		 $("#nbNouritture").text(data);
	});
	$.get("/affiche_nbBois").done(function (data) {
		$("#nbBois").text(data);
	});
	$.get("/affiche_nbPierre").done(function (data) {
		$("#nbPierre").text(data);
	});
	
	$.get("/affiche_nbFermes").done(function (data) {
		$("#nbFermes").text(data);
	});
	$.get("/affiche_nbScieries").done(function (data) {
		$("#nbScieries").text(data);
	});
	$.get("/affiche_nbCarrieres").done(function (data) {
		$("#nbCarrières").text(data);
	});
	$.get("/affiche_nbMines").done(function (data) {
		$("#nbMines").text(data);
	});
	
	$.get("/affiche_nivEntrepot").done(function (data) {
		$("#nivEntrepot").text(data);
	});
	
	$.get("/affiche_login").done(function (data) {
		$("#Username").text(data);
	});
	
    $.get("/affiche_nomVillage").done(function (data) {
		$("#nomVillage").text(data);
	});
    
    let popup = document.getElementById('popup');

    function openPopup(){
      popup.classList.add('open-popup');
    }

    function closePopup(){
      popup.classList.remove('open-popup');
    }
	
});
