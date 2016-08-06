// search button on click
// gets search results
$('#searchBtn').click(function(){
	search_text = $('#search').val();
	console.log(search_text);
	$.getJSON('/search?q=' + search_text, success=function(data, textStatus, jqXHR){
		// display `data`
		// remove old data
		search_temp = $('.search_result').first().clone();
		search_temp.show();
		$('.search_result').remove();
		// create new
		for (i=0; i<data.length; i++){
			search_x = search_temp.clone();
			search_x.attr('id', 'result' + i);
			// set values
			$(search_x).find('.thumb').attr('src', data[i]['thumb']);
			$(search_x).find('.title').text(data[i]['title']);
			$(search_x).find('.length').text(data[i]['length']);
			$(search_x).find('.uploader').text(data[i]['uploader']);
			$(search_x).find('.time').text(data[i]['time']);
			$(search_x).find('.views').text(data[i]['views']);
			$(search_x).find('.download').attr('data-video', data[i]['id']);
			$(search_x).find('.download').click(get_download_link);
			// set d/l filename
			$(search_x).find('.download').attr('download', data[i]['title']);
			// console.log(search_x);
			search_x.appendTo('#container');
		}
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
		elem.attr('href', data['url']);
		elem.attr('target', '_blank');
		return false;
	});
}
