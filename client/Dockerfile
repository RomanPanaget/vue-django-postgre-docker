FROM node:10-alpine
WORKDIR /code

COPY . .
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]