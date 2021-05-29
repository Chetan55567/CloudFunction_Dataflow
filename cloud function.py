def startDataflowProcess(data, context):
	from googleapiclient.discovery import build
	#replace with your projectID
	project = "qwiklabs-gcp-04-14bcaee82d4a"
	job = project + " " + str(data['timeCreated'])
	#path of the dataflow template on google storage bucket
	template = "gs://dataflow-templates/latest/Word_Count"
	inputFile = "gs://" + str(data['bucket']) + "/" + str(data['name'])
	output = "gs://qwiklabs-gcp-04-14bcaee82d4t/output"
	#user defined parameters to pass to the dataflow pipeline job
	parameters = {
		'inputFile': inputFile,
		'output': output
	}
	#tempLocation is the path on GCS to store temp files generated during the dataflow job
	environment = {'tempLocation': 'gs://qwiklabs-gcp-04-14bcaee82d4at/temp',
					'zone': 'us-central1-f'}

	service = build('dataflow', 'v1b3', cache_discovery=False)
	#below API is used when we want to pass the location of the dataflow job
	request = service.projects().locations().templates().launch(
		projectId=project,
		gcsPath=template,
		location='us-central1',
		body={
			'jobName': job,
			'parameters': parameters,
			'environment':environment
		},
	)
	response = request.execute()
	print(str(response))