# E91 GROUP 8 FINAL PROJECT APP
Test on 12/16/2018 at 2014 EST

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

Test
```
curl localhost:8080
```

Clean up

```
docker rm e91-app -f
```
