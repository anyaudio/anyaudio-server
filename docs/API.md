# API


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
		"views": "20,328,744",
		"get_url": "/g/someLoNgUrl"
	},
]
```


### Get download url of a search result

Send a GET request to `get_url` that you got in search API response. It will return the download `url`.

A successful response is of the following format.

```js
{
	"status": 0,
	"url": "https://some.com/long/url"
}
```

The error response follows the same format but sets `status` to non-zero value.
