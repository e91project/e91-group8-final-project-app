# E91 GROUP 8 FINAL PROJECT APP

## Prerequisites

* Install Docker

## Docker

Build

```
docker build -t e91-final-project-app .
```

Run 

```
docker run -d -p 8080:80 --name e91-app e91-final-project-app
```

Curl Test
```
curl localhost:8080
```

HTML Parser Test

```
export TEST_HOST=localhost; export TEST_PORT=8080; python3 test/test_site.py
```

Clean up

```
docker rm e91-app -f
```