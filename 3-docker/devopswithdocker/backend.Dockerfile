FROM golang:1.16

WORKDIR /app

COPY . ./

RUN go build

RUN go test ./...

ENV PORT 8080
ENV REQUEST_ORIGIN http://localhost:5000

CMD [ "./server" ]
