## API Documentation

API v1.

---


* ### Common Response Fields

All responses will include these common fields -

| Term | Explaination |
|-----------|--------------|
|`status`| HTTP status code.|
|`developerMessage`| Verbose for debugging. Set only if there is an error.|
| `userMessage`| Error message for user.|
|`errorCode`| Platform specific error code.|

Example -
```json
{
	"status": 200
}
```
```json
{
	"status": 500,
	"developerMessage": "FFMPEG: Error converting m4a to mp3",
	"userMessage": "The download couldn't be processed, please try again. Contact support@musicgenie.com if problem persists.",
	"errorCode": "500-006"
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
		"url": "http://ymp3.aavi.me/d/fSR3dG4kPCIkanZ2cnU8MTF0NDIvLy91cC9yN3NudXBuOTBpcXFpbmd4a2ZncTBlcW8xeGtmZ3FybmN7ZGNlbUFoZ3pyPzs2Mzs2NzMnNEU7NjQ0Nzs4JzRFOzY0OjU7Oic0RTs2NTI7MzInNEU7NjUzMjM0JzRFOzY1NTI7OCc0RTs2NTU0NDUnNEU7NjU1OzY4JzRFOzY1Nzc0OCc0RTs2NTc6OzQnNEU7NjU5NDg0JzRFOzY1OTc3NCc0RTs2NTk7NjsnNEU7NjU6NTQ5JzRFOzY1Ojg4NCc0RTs2NTo6MjYnNEU7NjU6OjQ0JzRFOzY1Ozc6Mic0RTs2NjI1ODsnNEU7NjYyNzU2JzRFOzY2Mjo1Myc0RTs2NjMzNjInNEU7NjYzNzQ5JzRFOzY2Mzo3NSc0RTs2NjQ2NDYnNEU7NjY0Njs5JzRFOzY2NDk6Mic0RTs2NjYyOTIob3U/Y3cob3g/byhvdj8zNjkyOjQ3ODk0KGZ3dD80OTUwMzM1KHdycD9XS3t8Ok96VU5xUyhvcD91cC9yN3NudXBuOSh1cXd0ZWc/e3F3dndkZyhlbmdwPzY1NTo0OjUodXhndD81KGtwa3ZleXBmZHJ1Pzo6NzIyMjIodXJjdGNvdT9lbmdwJzRFZnd0JzRFZ2snNEVpZXQnNEVpa3QnNEVrZic0RWtwa3ZleXBmZHJ1JzRFa3InNEVrcmRrdnUnNEVrdmNpJzRFbWdncmNua3hnJzRFbm92JzRFb2tvZyc0RW9vJzRFb3AnNEVvdSc0RW94JzRFcGonNEVybic0RXRnc3drdGd1dW4nNEV1cXd0ZWcnNEV3cnAnNEVnenJrdGcoa2Y/cS9DRVNXZVczU0k4SWFmZ0lPa1FXYUtrYVxsbWcyeENrWVtrWUx2S3NpaG11NChnaz9FaWd0WDk0TEYvWUs6aVZSMnJtUyhvbz81Myhrcj83NjA6NjAyMDM6OyhpZXQ/d3UodGdzd2t0Z3V1bj97Z3UobWdncmNua3hnP3tndShybj8zNyhwaj9LaXJ5ZWxDfE5vbmpcRks0TWkyNU9rNnpQRTZ7T0ZPd09WS3ooZ3pya3RnPzM2OTI6Njk6NzIoaWt0P3tndShub3Y/MzY2NTg5ODQ5OjQ7OTQ4NihrcmRrdnU/MihrdmNpPzM2MihtZ3s/e3Y4KG9rb2c/Y3dma3EnNEhvcjYodWtpcGN2d3RnPzkzM0RFNUQ4NTtFOjo7Q0ZHOzZHRDQyRjI3Mzg0ODQ7MzYyQ0czMjowREcyNzU6RDVGOjhGNzQ2REdERUM3RDc0Nzc7ODU0Ojo7Ojk6QzM1Nyh0Y3ZnZHtyY3V1P3tndSQuIiRrZiQ8IiR1blBnZFE5W2tydSQuIiR2a3ZuZyQ8IiRQd2VuZ3tjIi8iRENVVSJUY3BrIi8iQ2NsYyJoZ2N2IkN4cGdndiJNand0b2siKGNvcj0iSXd0ayJJY3BpdXZjJH8%3D"
	}
	```

* ### Getting Youtube Search Results

	* **Type**: `GET`
	* **Location**: `/api/v1/search`
	* **Terms**:

	| Term | Explaination |
	|-----------|--------------|
	|`q`| Search query.|
	|`offset`| Number of items to skip. e.g. if `offset = 10`, results start from 11<sup>th</sup> item.|
	|`number`| Maximum number of results to fetch.|
	* **Response**:

	| Term | Explaination |
	|-----------|--------------|
	|`metadata`| Data about fetched data. <br/>&nbsp;&nbsp;&nbsp;&nbsp;`query`: Searched query.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`offset`: Offset of results shown<br/>&nbsp;&nbsp;&nbsp;&nbsp;`number`: Number of results requested<br/>`count`: Number of results shown.|
	|`results`| Actual result set contains a list of items with following attributes : <br/>&nbsp;&nbsp;&nbsp;&nbsp;`id`: Youtube ID of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`length`: Length of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`thumb`: Link to video thumbnail.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`time`: Time since upload. e.g. `3 years ago`.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`uploader`: Youtube uploader ID.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`views`: View count for the video.|

* ### Getting Trending Songs

	* **Type**: `GET`
	* **Location**: `/api/v1/latest`
	* **Parameters**:

	| Term | Explaination |
	|-----------|--------------|
	|`number`| Maximum number of results to return|
	* **Response**

	| Term | Explaination |
	|-----------|--------------|
	|`metadata`| Data about fetched data.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`count`: Number of results shown.|
	|`results`| Actual result set contains a list of items with following attributes : <br/>&nbsp;&nbsp;&nbsp;&nbsp;`id`: Youtube ID of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`length`: Length of video.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`thumb`: Link to video thumbnail.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`time`: Time since upload. e.g. `3 years ago`.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`uploader`: Youtube uploader ID.<br/>&nbsp;&nbsp;&nbsp;&nbsp;`views`: View count for the video.|
