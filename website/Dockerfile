FROM arm32v7/node:16-alpine3.11 as builder

WORKDIR /frontend

COPY package.json ./

COPY package-lock.json ./

RUN npm install

COPY . ./

RUN npm run build

FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /frontend/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
