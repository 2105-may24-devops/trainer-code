FROM node:14

WORKDIR /app

RUN npm install -g serve

COPY package.json package-lock.json ./
RUN npm install

ENV REACT_APP_BACKEND_URL http://localhost:8080

COPY . ./
RUN npm run build

CMD [ "serve", "-n", "-s", "-l", "5000", "build" ]

EXPOSE 5000
