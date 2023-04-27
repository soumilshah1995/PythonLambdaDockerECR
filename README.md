# PythonLambdaDockerECR
PythonLambdaDockerECR

* Learn how to run lambda on docker container and deploy Base image on ECR and use on Lambda 


#### Commands 
```
docker build -t random-letter .


docker run -p 9000:8080 random-letter:latest

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"msg\":\"hello\"}"

```
