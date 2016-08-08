// search button on click
// gets search results
$('#searchBtn').click(function(){
	search_text = $('#search').val();
	console.log(search_text);
	$('#loading_text').show();
	// remove old data
	search_temp = $('.search_result').first().clone();
	// reset
	search_temp.show();
	search_temp.find('.download').text('Get Link');
	search_temp.find('.download').attr('href', '#');
	search_temp.unbind('click');
	// delete
	$('.search_result').remove();
	// get new results
	$.getJSON('/search?q=' + search_text, success=function(data, textStatus, jqXHR){
		// create new
		for (i=0; i<data.length; i++){
			search_x = search_temp.clone();
			search_x.attr('id', 'result' + i);
			// set values
			$(search_x).find('.thumb').attr('src', data[i]['thumb']);
			$(search_x).find('.thumb_link').attr('href', 'https://youtube.com/watch?v=' + data[i]['id']);
			$(search_x).find('.title').text(data[i]['title']);
			$(search_x).find('.length').text(data[i]['length']);
			$(search_x).find('.uploader').text(data[i]['uploader']);
			$(search_x).find('.time').text(data[i]['time']);
			$(search_x).find('.views').text(data[i]['views'] + ' views');
			$(search_x).find('.download').attr('data-video', data[i]['id']);
			$(search_x).find('.download').click(get_download_link);
			// set d/l filename
			$(search_x).find('.download').attr('download', data[i]['title']);
			// console.log(search_x);
			$(search_x).addClass('flex_force'); // just flex doesn't work
			search_x.appendTo('#container');
		}
		// hide loading
		$('#loading_text').hide();
	});
});

// gets the download link for a video
function get_download_link(event){
	event.preventDefault();
	elem = $(event.target);
	elem.text('Fetching...');
	$.getJSON('/g/' + elem.attr('data-video'), success=function(data, textStatus, jqXHR){
		$(elem).unbind('click');
		if (data['status'] != 0){
			elem.text('Failed');
			elem.removeAttr('href');
			return false;
		}
		elem.text('Download');
		elem.click(download_start);
		elem.attr('href', data['url']);
		elem.attr('target', '_blank');
		return false;
	});
}

// after download button is clicked
function download_start(event){
	$(event.target).text('Starting..');
}

$(document).ready(function(){
	$('.search_result').hide();
	$('#search').keyup(function(e){
		if(e.keyCode == 13){
			$(this).trigger("enterKey");
		}
	});

	$('#search').bind('enterKey', function(e){
		$('#searchBtn').click();
	});
});
