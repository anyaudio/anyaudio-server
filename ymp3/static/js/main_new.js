$(document).ready(function(){
	$('#ymp3-search').submit(function(e){
		$('#search-preloader').show();
		$('#result-keyword').hide();
		var $this  = $(this);
		e.preventDefault();
		var searchInput = $this.find('.search-btn').val();
		console.log(searchInput);
		loadResult(searchInput);
	});

	$('#search-result').on('click','.ymp3-download',function(e){
		e.preventDefault();
		$this = $(this);
		$this.addClass('dwn-ready-card');

		if($this.hasClass('dwn-done'))
			$this.removeClass('dwn-done');

		$.getJSON($this.attr('data-get-url'), success=function(data, textStatus, jqXHR){
			if (data['status'] != 200){
				$this.text('Failed');
				$this.removeAttr('href');
				return false;
			}
			console.log($this.attr('data-get-url'));
			window.open(data['url']);
			//window.location.href = data['url'];
			$this.addClass('dwn-done');
			$this.unbind('click');
		});
	});

	$('#menu-bar').click(function(e){
		e.preventDefault();
		document.getElementById("nav-overlay").style.width = "100%";
	});

	$('#nav-overlay .closebtn').click(function(e){
		e.preventDefault();
		document.getElementById("nav-overlay").style.width = 0;
	})

});

function getCardHtml(data){
	return '<div class="col s6 m4 l3"><div class="card card--ym3"><a data-get-url="'+data['get_url']+'" class="card-image waves-effect waves-block waves-light ymp3-download"><img class="activator" src="'+data["thumb"]+'"><div class="overlay overlay--dark"></div><div class="meta-duration ">'+data["length"]+'</div><span href="#!" class="btn-dwn valign-wrapper"><i class="valign fa fa-spinner fa-pulse fa-3x fa-fw"></i><i class="valign fa fa-arrow-down" aria-hidden="true"></i><i class="valign fa fa-check fa-2x" aria-hidden="true"></i></span></a><div class="card-content"><span class="activator card--ym3--title flow-text">'+data["title"]+'</span><div class="meta"><div class="channel color-primary"><i class="fa fa-bullseye" aria-hidden="true"></i>'+data["uploader"]+'</div><div class="views color-primary"><i class="fa fa-eye" aria-hidden="true"></i>'+data["views"]+'</div></div></div><div class="card-reveal"><span class="card-title color-primary activator"><i class="fa fa-times right"></i>'+data["title"]+'</span><p class="flow-text">Here is some more information about this product that is only revealed once clicked on.</p></div></div></div>';
}

function loadResult(searchInput){
	$('#search-result').html('');

	$.getJSON('/api/v1/search?q=' + searchInput, success=function(data, textStatus, jqXHR){
		var dataResult = data['results'];
		var searchKeyword = data['metadata']['q'];
		$('#result-keyword h4').html('Showing results for <span class="color-primary">"'+searchKeyword+'"</span>');
		console.log(searchKeyword);
		//console.log(dataResult);

		dataResult.forEach(function(res){
			var resHtml;
			$('#search-result').append(getCardHtml(res));
		});
		$('#result-keyword').show();
		$('#search-preloader').hide();
	})
}

//Adding Navbar dynamic class

(function($) {
	"use strict";

	var $navbar = $(".nav--custom"),
		y_pos = $navbar.offset().top,
		height = $navbar.height();

	$(document).scroll(function() {
		var scrollTop = $(this).scrollTop();

		if (scrollTop > y_pos + height) {
			$navbar.addClass("nav-white").animate({
				top: 0
			});
			$navbar.removeClass("nav--transparent");
		} else if (scrollTop <= y_pos) {
			$navbar.removeClass("nav-white").clearQueue().animate({
				top: "-80px"
			}, 0);
			$navbar.addClass("nav--transparent");
		}
	});

})(jQuery, undefined);