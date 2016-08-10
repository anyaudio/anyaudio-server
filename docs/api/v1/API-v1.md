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
	* **Response**:

	| Term | Explaination |
	|-----------|--------------|
	|`url`| URL to download the song from.|

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
