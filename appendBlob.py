
# sample code covers in creating a append blob and appending contents

blobconnection = "connectionstring"
blob_service_client = BlobServiceClient.from_connection_string(blobconnection)
foldername = "folder1"
containername = 'mycontainer'
filename = foldername +'/appendblobtest' + '.csv'
blob_client = blob_service_client.get_blob_client(container=containername, blob=filename)
df = pd.DataFrame(columns = ['Name', 'Age'])
blob_client.upload_blob(data=df.to_csv(index=False),overwrite =True, blob_type= 'AppendBlob')
data = [{'Name': "name1", 'Age' : 10}, {'Name': "name2", 'Age' : 20}]
df = df.append(data)
print (df)
blob_client.upload_blob(data=df.to_csv(index=False, header=False),overwrite =False, blob_type= 'AppendBlob' )
data = [{'Name': "name3", 'Age' : 30}, {'Name': "name4", 'Age' : 40}]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
blob_client.upload_blob(data=df.to_csv(index=False, header=False),overwrite =False, blob_type= 'AppendBlob')
