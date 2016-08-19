$(document).ready(function(){
	$('#ymp3-search').submit(function(e){
		$('#search-preloader').show();
		$('#result-keyword').hide();
		var $this  = $(this);
		e.preventDefault();
		var searchInput = $this.find('.search-btn').val();
		console.log(searchInput);
		$('#search-result').html('');

		$.getJSON('/api/v1/search?q=' + searchInput, success=function(data, textStatus, jqXHR){
			var dataResult = data['results'];
			var searchKeyword = data['metadata']['q'];
			$('#result-keyword h4').text('Showing results for "'+searchKeyword+'"');
			console.log(searchKeyword);
			//console.log(dataResult);

			dataResult.forEach(function(res){
				var resHtml;
				$('#search-result').append(getCardHtml(res));
				//console.log(getCardHtml(res));
			});
			$('#result-keyword').show();
			$('#search-preloader').hide();
		})
	});

	function getCardHtml(data){
		return ' <div class="col s6 m4 l3"><div class="card card--ym3"><div class="card-image waves-effect waves-block waves-light"><img class="activator" src="'+data["thumb"]+'"><div class="overlay overlay--dark"></div><div class="meta-duration ">'+data["length"]+'</div><a href="#!" class="btn-dwn valign-wrapper"><i class="valign fa fa-arrow-down" aria-hidden="true"></i></a></div><div class="card-content"><span class="activator card--ym3--title flow-text">'+data["title"]+'</span><div class="meta"><div class="channel color-primary"><i class="fa fa-bullseye" aria-hidden="true"></i>'+data["uploader"]+'</div><div class="views color-primary"><i class="fa fa-eye" aria-hidden="true"></i>'+data["views"]+'</div></div></div><div class="card-reveal"><span class="card-title activator grey-text text-darken-4"><i class="fa fa-times right"></i>'+data["title"]+'</span><p>Here is some more information about this product that is only revealed once clicked on.</p></div></div></div>';
	}
});