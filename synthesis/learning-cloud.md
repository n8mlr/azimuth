# Going cloud

## Python tricks

### Virtual Environments

#### Creating a virtual environment

```python
py -m venv MODULE
```

#### Installing requirements

```
pip3 install -r requirements.txt
```







### Logging to cloud watch

```python
from __future__ import print_function
print("This will show up in cloud watch log")
```



## Serverless



### Creating a stack

```bash
serverless create --template aws-python3 --name hello-serverless
```

### Defining serverless.yml

A complete reference of configuration options [found here](https://github.com/serverless/serverless/blob/master/docs/providers/aws/guide/serverless.yml.md)

```yaml
service: hello-serverless

provider:
  name: aws
  runtime: python3.6
  stage: prod
  region: us-west-2
  deploymentBucket:
    name: n8mlr
    serverSideEncryption: AES256

functions:
  hello:
    handler: handler.hello
    events:
      - http:
          path: hello
          method: get
```

