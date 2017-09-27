import picamera
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json
camera = picamera.PiCamera()



while True:
	input("Press enter to start camera!")
	camera.start_preview()
	input("")
	camera.capture("test2.jpg")
	camera.stop_preview()
	
	
	
	########### Python 3.6 #############
	
	
	
	###############################################
	#### Update or verify the following values. ###
	###############################################
	
	# Replace the subscription_key string value with your valid subscription key.

	
	# Replace or verify the region.
	#
	# You must use the same region in your REST API call as you used to obtain your subscription keys.
	# For example, if you obtained your subscription keys from the westus region, replace
	# "westcentralus" in the URI below with "westus".
	#
	# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
	# a free trial subscription key, you should not need to change this region.

	
	
	
	# Body. The URL of a JPEG image to analyze.
	subscription_key = 'f438d07bba884963833fd1a18a4f7fcf'
	uri_base = 'https://westcentralus.api.cognitive.microsoft.com'
	# Request headers.
	headers = {
	    'Content-Type': 'application/octet-stream',
	    'Ocp-Apim-Subscription-Key': subscription_key,
	}
	
	# Request parameters.
	params = {
	    'returnFaceId': 'true',
	    'returnFaceLandmarks': 'false',
	    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
		}
	
	face_id_1 = "";
	# First image file
	filename = '/home/pi/Desktop/SECapstone/test.jpg'
		
	f = open(filename, "rb")
		
	body = f.read()
	
	f.close()
	
	try:
	# Execute the REST API call and get the response.
		response = requests.request('POST', uri_base + '/face/v1.0/detect', json=None, data=body, headers=headers, params=params)
		#print ('Response:')
		parsed = json.loads(response.text)
		#print (json.dumps(parsed, sort_keys=True, indent=2))
		face_id_1 = parsed[0]['faceId']
	except Exception as e:
		print('Error:')
		print(e)
	
	face_id_2 = ""
	
	
	
	
	
	
	# Second image file
	filename = '/home/pi/Desktop/SECapstone/test2.jpg'
	
	f = open(filename, "rb")
	
	body = f.read()
	
	f.close()
	
	try:
	    # Execute the REST API call and get the response.
	    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=None, data=body, headers=headers,
	                                params=params)
	
	    #print('Response:')
	    parsed = json.loads(response.text)
	    #print(json.dumps(parsed, sort_keys=True, indent=2))
	    face_id_2 = parsed[0]['faceId']
	
	except Exception as e:
	    print('Error:')
	    print(e)
	
	
	# Compare Faces
	try:
	    headers = {
	        'Content-Type': 'application/json',
	        'Ocp-Apim-Subscription-Key': subscription_key,
	    }
	    body = {'faceId1': face_id_1,
	            'faceId2': face_id_2};
	    print("1 --- " + face_id_1)
	    print("2 --- " + face_id_2)
	    response = requests.request('POST', uri_base + '/face/v1.0/verify', json=body, data=None, headers=headers,
	                                params=None)
	    print('Response:')
	    parsed = json.loads(response.text)
	    print(json.dumps(parsed, sort_keys=True, indent=2))
	    if parsed['isIdentical']:
	        print('Face accepted.')
		
	except Exception as e:
	    print('Error:')
	    print(e)
####################################