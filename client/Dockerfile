FROM node:18 AS build

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install

COPY . /app/
RUN npm run build

FROM nginx:latest AS serve

COPY --from=build /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
