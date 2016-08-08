# API

### Get audio url from video

Send a GET request to `/g/<video_id>` where `video_id` is youtube video id. (Example `/g/8oGZTbeEhv4`)

A successful response is of the following format.

```js
{
	"status": 0,
	"url": "https://some.com/long/url"
}
```

The error response follows the same format but sets `status` to non-zero value.


### Get youtube search results

Send a GET request to `/search` with query param `q=<search term>`. (Example `/search?q=Back%20In%20Time`)

Response is of the following format.

```js
[
	{
		"id": "zaSZE194D4I",
		"length": "3:33",
		"thumb": "http://img.youtube.com/vi/zaSZE194D4I/0.jpg",
		"time": "3 years ago",
		"title": "Pitbull - Back in Time",
		"uploader": "PitbullVEVO",
		"views": "20,328,744"
	},
]
```
