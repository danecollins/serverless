# Serverless HTTP endpoint on AWS


This page documents how to create an HTTP endpoint on AWS that can interact with other AWS services.



Follow requirements on [this page](https://blog.sicara.com/deploy-serverless-rest-api-lambda-s3-aws-2cf99b8f34ae) including:

1. install node
2. install serverless toolkit
3. install python 3.6 or above

4. Then create the application

        > brew install node
        > npm install -g serverless
        > <create virtual environment (skye)>
        > serverless create?—-template aws-python3?—-name auto-update-rest
        > serverless plugin install -n serverless-python-requirements

5. Edit the .yml file to define the endpoints
6. Create the code pointed to by the endpoints
7. Deploy the code
