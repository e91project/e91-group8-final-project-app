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

Clean up

```
docker rm e91-app -f
```
