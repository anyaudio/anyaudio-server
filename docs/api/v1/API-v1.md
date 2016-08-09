## API Documentation

API v1.

---
* ### Getting Audio From Video ID

	##### Request

	* **Type** - `GET`
	* **Location** - `/api/v1/g`
	* **Parameters** -
	```json
	{
		"video_id": "Video ID as on Youtube",
		"bitrate": "Upper limit of bitrate in kbps. Defaults to 128."
	}
	```
	* **Response** -
	```json
	{
		"status": 400,  # HTTP status code
		"developerMessage": "Verbose for debugging. Set only if there is an error.",
		"userMessage": "Error message for user."
		"errorCode": 12345  # Platform defined error code
		"moreInfo": "/developer/error/12345"
	}
	```
