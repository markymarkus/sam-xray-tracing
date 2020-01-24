# sam-xray-tracing
sam build --use-container -m ./requirements.txt
sam package --s3-bucket BUCKET_NAME --output-template-file packaged.yaml --region eu-west-1
sam deploy --template-file ./packaged.yaml --stack-name CLOUDFORMATION_STACK_NAME --capabilities CAPABILITY_IAM --region eu-west-1
