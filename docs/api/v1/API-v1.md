## API Documentation

API v1.

---


### Common Response Fields

All responses will include these common fields -

| Term | Explaination |
|-----------|--------------|
|`status`| HTTP status code.|
|`requestLocation`| Location where request was made.|
|`developerMessage`| Verbose for debugging. Set only if there is an error.|
| `userMessage`| Error message for user.|
|`errorCode`| Platform specific error code.|

Example -
```json
{
	"status": 200,
	"requestLocation": "/api/v1/g"
}
```
```json
{
	"status": 500,
	"requestLocation": "/api/v1/g",
	"developerMessage": "URLOpen: Timeout",
	"userMessage": "Server problem, please try again later.",
	"errorCode": "500-004"
}
```

* ### Getting Audio from Video ID

	* **Type:** `GET`
	* **Location:** `/api/v1/g`
	* **Parameters**:

	| Term | Explaination |
	|-----------|--------------|
	|`video_id`| Video ID as on Youtube.|
	|`bitrate`| Upper Limit of song bitrate in kbps. Defaults to 140.|

	Example -
	```json
	{
		"video_id": "f0DkVn-joQc",
		"bitrate": 320
	}
	```

	* **Response**:

	| Term | Explaination |
	|-----------|--------------|
	|`url`| URL to download the song from.|

	Example -
	```json
	{
		"url": "/d/fSR3dG4kPCIkanZ2cnU8MTF0NDIvLy91cC9yN3NudXBuOTBpcXFpbmd4a2ZncTBlcW8xeGtmZ3FybmN7ZGNlbUFoZ3pyPzs2Mzs2NzMnNEU7NjQ0Nzs4JzRFOzY0OjU7Oic0RTs2NTI7MzInNEU7NjUzMjM0JzRFOzY1NTI7OCc0RTs2NTU0NDUnNEU7NjU1OzY4JzRFOzY1Nzc0OCc0RTs2NTc6OzQnNEU7NjU5NDg0JzRFOzY1OTc3NCc0RTs2NTk7NjsnNEU7NjU6NTQ5JzRFOzY1Ojg4NCc0RTs2NTo6MjYnNEU7NjU6OjQ0JzRFOzY1Ozc6Mic0RTs2NjI1ODsnNEU7NjYyNzU2JzRFOzY2Mjo1Myc0RTs2NjMzNjInNEU7NjYzNzQ5JzRFOzY2Mzo3NSc0RTs2NjQ2NDYnNEU7NjY0Njs5JzRFOzY2NDk6Mic0RTs2NjYyOTIob3U/Y3cob3g/byhvdj8zNjkyOjQ3ODk0KGZ3dD80OTUwMzM1KHdycD9XS3t8Ok96VU5xUyhvcD91cC9yN3NudXBuOSh1cXd0ZWc/e3F3dndkZyhlbmdwPzY1NTo0OjUodXhndD81KGtwa3ZleXBmZHJ1Pzo6NzIyMjIodXJjdGNvdT9lbmdwJzRFZnd0JzRFZ2snNEVpZXQnNEVpa3QnNEVrZic0RWtwa3ZleXBmZHJ1JzRFa3InNEVrcmRrdnUnNEVrdmNpJzRFbWdncmNua3hnJzRFbm92JzRFb2tvZyc0RW9vJzRFb3AnNEVvdSc0RW94JzRFcGonNEVybic0RXRnc3drdGd1dW4nNEV1cXd0ZWcnNEV3cnAnNEVnenJrdGcoa2Y/cS9DRVNXZVczU0k4SWFmZ0lPa1FXYUtrYVxsbWcyeENrWVtrWUx2S3NpaG11NChnaz9FaWd0WDk0TEYvWUs6aVZSMnJtUyhvbz81Myhrcj83NjA6NjAyMDM6OyhpZXQ/d3UodGdzd2t0Z3V1bj97Z3UobWdncmNua3hnP3tndShybj8zNyhwaj9LaXJ5ZWxDfE5vbmpcRks0TWkyNU9rNnpQRTZ7T0ZPd09WS3ooZ3pya3RnPzM2OTI6Njk6NzIoaWt0P3tndShub3Y/MzY2NTg5ODQ5OjQ7OTQ4NihrcmRrdnU/MihrdmNpPzM2MihtZ3s/e3Y4KG9rb2c/Y3dma3EnNEhvcjYodWtpcGN2d3RnPzkzM0RFNUQ4NTtFOjo7Q0ZHOzZHRDQyRjI3Mzg0ODQ7MzYyQ0czMjowREcyNzU6RDVGOjhGNzQ2REdERUM3RDc0Nzc7ODU0Ojo7Ojk6QzM1Nyh0Y3ZnZHtyY3V1P3tndSQuIiRrZiQ8IiR1blBnZFE5W2tydSQuIiR2a3ZuZyQ8IiRQd2VuZ3tjIi8iRENVVSJUY3BrIi8iQ2NsYyJoZ2N2IkN4cGdndiJNand0b2siKGNvcj0iSXd0ayJJY3BpdXZjJH8%3D"
	}
	```

* ### Getting Youtube Search Results

	* **Type**: `GET`
	* **Location**: `/api/v1/search`
	* **Terms**:

	| Term | Explaination |
	|-----------|--------------|
	|`q`| Search query.|

	Example -
	```json
	{
		"q": "Bass%20Rani"
	}
	```

	* **Response**:

	| Term | Explaination |
	|-----------|--------------|
	|`metadata`| Data about fetched data. <br/>&nbsp;&nbsp;&nbsp;&nbsp;`q`: Searched query.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`count`: Numner of results returned.|
	|`results`| Actual result set contains a list of items with following attributes : <br/>&nbsp;&nbsp;&nbsp;&nbsp;`get_url`: URL to get song from.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`title`: Title of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`id`: Youtube ID of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`length`: Length of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`thumb`: Link to video thumbnail.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`time`: Time since upload. e.g. `3 years ago`.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`uploader`: Youtube uploader ID.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`views`: View count for the video in comma separated number format.|

	Example -
	```json
	{
		"metadata": {
			"q": "Bass%20Rani",
			"count": 3
		},
		"results" : [
			{
				"get_url": "/g/fSRrZiQ8IiR1blBnZFE5W2tydSQuIiR2a3ZuZyQ8IiRQd2VuZ3tjIi8iRENVVSJUY3BrIi8iQ2NsYyJoZ2N2IkN4cGdndiJNand0b2siKGNvcj0iSXd0ayJJY3BpdXZjJH8=",
				"id": "slNebO7Yips",
				"length": "4:34",
				"thumb": "http://img.youtube.com/vi/slNebO7Yips/0.jpg",
				"time": "10 months ago",
				"title": "Nucleya - BASS Rani - Aaja feat Avneet Khurmi &amp; Guri Gangsta",
				"uploader": "NUCLEYA",
				"views": "1,078,918"
			},
			{
				"get_url": "/g/fSRrZiQ8IiRmc1RJOFJbTXl6eSQuIiR2a3ZuZyQ8IiROY3dwaSJJY3ljZWpjIkh2IkN4cGdndiJNand0b2sifiJQV0VOR1tDIn4iRENVVSJUQ1BLIn4iSHdubiJDbmR3byR/",
				"id": "dqRG6PYKwxw",
				"length": "3:35",
				"thumb": "http://img.youtube.com/vi/dqRG6PYKwxw/0.jpg",
				"time": "10 months ago",
				"title": "Laung Gawacha Ft Avneet Khurmi | NUCLEYA | BASS RANI | Full Album",
				"uploader": "Lyrics Arena",
				"views": "575,811"
			},
			{
				"get_url": "/g/fSRrZiQ8IiR5bll1S0phZFdNVyQuIiR2a3ZuZyQ8IiRQV0VOR1tDIi8iQ0NMQyJ+IkRDVVUiVENQSyJ+IlFISEtFS0NOIkpTIkNXRktRIn4kfw==",
				"id": "wlWsIH_bUKU",
				"length": "4:35",
				"thumb": "http://img.youtube.com/vi/wlWsIH_bUKU/0.jpg",
				"time": "10 months ago",
				"title": "NUCLEYA - AAJA | BASS RANI | OFFICIAL HQ AUDIO |",
				"uploader": "Prasad Kedar",
				"views": "1,862,495"
			}
		]
	}
	```

* ### Getting Trending Songs

	* **Type**: `GET`
	* **Location**: `/api/v1/latest`
	* **Response**

	| Term | Explaination |
	|-----------|--------------|
	|`metadata`| Data about fetched data.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`count`: Number of results shown.|
	|`results`| Actual result set contains a list of items with following attributes : <br/>&nbsp;&nbsp;&nbsp;&nbsp;`id`: Youtube ID of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`length`: Length of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`thumb`: Link to video thumbnail.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`time`: Time since upload. e.g. `3 years ago`.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`uploader`: Youtube uploader ID.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`views`: View count for the video.|

	Example -
	```json
	{
		"metadata": {
			"count": "2"
		},
		"results" : [
			{
				"get_url": "/g/fSRrZiQ8IiR1blBnZFE5W2tydSQuIiR2a3ZuZyQ8IiRQd2VuZ3tjIi8iRENVVSJUY3BrIi8iQ2NsYyJoZ2N2IkN4cGdndiJNand0b2siKGNvcj0iSXd0ayJJY3BpdXZjJH8=",
				"id": "slNebO7Yips",
				"length": "4:34",
				"thumb": "http://img.youtube.com/vi/slNebO7Yips/0.jpg",
				"time": "10 months ago",
				"title": "Nucleya - BASS Rani - Aaja feat Avneet Khurmi &amp; Guri Gangsta",
				"uploader": "NUCLEYA",
				"views": "1,078,918"
			},
			{
				"get_url": "/g/fSRrZiQ8IiRmc1RJOFJbTXl6eSQuIiR2a3ZuZyQ8IiROY3dwaSJJY3ljZWpjIkh2IkN4cGdndiJNand0b2sifiJQV0VOR1tDIn4iRENVVSJUQ1BLIn4iSHdubiJDbmR3byR/",
				"id": "dqRG6PYKwxw",
				"length": "3:35",
				"thumb": "http://img.youtube.com/vi/dqRG6PYKwxw/0.jpg",
				"time": "10 months ago",
				"title": "Laung Gawacha Ft Avneet Khurmi | NUCLEYA | BASS RANI | Full Album",
				"uploader": "Lyrics Arena",
				"views": "575,811"
			},
		]
	}
	```
