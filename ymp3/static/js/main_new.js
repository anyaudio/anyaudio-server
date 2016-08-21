$(document).ready(function(){

	//Search event listener
	$('#ymp3-search').submit(function(e){
		$('#search-preloader').show();
		$('#result-keyword').hide();
		var $this  = $(this);
		e.preventDefault();
		var searchInput = $this.find('.search-btn').val();
		console.log(searchInput);
		loadResult(searchInput);
	});

	//Fetches url and starts dowload in new tab
	$('body').on('click','.ymp3-download',function(e){
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

	//Nav Overlay trigger
	$('#menu-bar').click(function(e){
		e.preventDefault();
		document.getElementById("nav-overlay").style.width = "100%";
	});
	$('#nav-overlay .closebtn').click(function(e){
		e.preventDefault();
		document.getElementById("nav-overlay").style.width = 0;
	});

});

function getCardHtml(data){
	return '<div class="col s6 m4 l3"><div class="card card--ym3"><a data-get-url="'+data['get_url']+'" class="card-image waves-effect waves-block waves-light ymp3-download"><img class="activator" src="'+data["thumb"]+'"><div class="overlay overlay--dark"></div><div class="meta-duration ">'+data["length"]+'</div><span href="#!" class="btn-dwn valign-wrapper"><i class="valign fa fa-spinner fa-pulse fa-3x fa-fw"></i><i class="valign fa fa-arrow-down" aria-hidden="true"></i><i class="valign fa fa-check fa-2x" aria-hidden="true"></i></span></a><div class="card-content"><span class="activator card--ym3--title flow-text">'+data["title"]+'</span><div class="meta"><div class="channel color-primary"><i class="fa fa-bullseye" aria-hidden="true"></i>'+data["uploader"]+'</div><div class="views color-primary"><i class="fa fa-eye" aria-hidden="true"></i>'+data["views"]+'</div></div></div><div class="card-reveal"><span class="card-title color-primary activator"><i class="fa fa-times right"></i>'+data["title"]+'</span><p class="flow-text">'+data['description']+'</p></div></div></div>';
}

function getTrendingHtml(data,type){
	return '<div class="trending"><div class="trending-title"><h4 class="title-deco title-deco--sm">'+type+'</h4></div><div class="white-space space-mini"></div><div class="trending-list row">'+data+'</div><div class="white-space space-mini"></div><a href="/explore?p='+type+'" class="no-shadow waves-effect waves-light btn red trending-more">More</a></div>';
}

function loadResult(searchInput,resType){

	/*Result Type
	0:For Search
	1:for PlayList*/
	var resAPI = ['/api/v1/search?q=','/api/v1/trending?type='];

	resType = typeof resType !=='undefined'?resType:0;

	$('#search-result').html('');

	$.getJSON(resAPI[resType] + searchInput, success=function(data, textStatus, jqXHR){
		var dataResult = data['results'];
		//var searchKeyword = data['metadata']['q'];

		if(!dataResult.length) {
			$('#result-keyword h4').html('No <span class="color-primary">"result" </span>found');
			$('#result-keyword').show();
			$('#search-preloader').hide();
			return false;
		}

		if(resType === 1) {
			$('#result-keyword h4').html('Showing top results for <span class="color-primary">"'+data['metadata']['type']+'"</span>');
		}
		else
			$('#result-keyword h4').html('Showing results for <span class="color-primary">"'+data['metadata']['q']+'"</span>');

		dataResult.forEach(function(res){
			var resHtml;
			$('#search-result').append(getCardHtml(res));
		});
		$('#result-keyword').show();
		$('#search-preloader').hide();
	})
}

function loadTrending(type,number){
	$.getJSON('/api/v1/trending?type=' + type+'&number='+number, success=function(data, textStatus, jqXHR){
		var dataResult = data['results'];
		var searchKeyword = data['metadata']['type'];
		var trendingCard = '';

		dataResult.forEach(function(res){
			trendingCard += getCardHtml(res);
		});
		$('#home-trending').append(getTrendingHtml(trendingCard,type));
	})
}

function trendingInit(count){
	$.getJSON('/api/v1/playlists', success=function(data, textStatus, jqXHR){
		var results = data['results'];
		for (var i = 0;i<count;i++){
			loadTrending(results[i]['playlist'],4);
		}
	})
}
