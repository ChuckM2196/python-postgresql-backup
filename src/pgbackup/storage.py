def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


# Remote storage
def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
