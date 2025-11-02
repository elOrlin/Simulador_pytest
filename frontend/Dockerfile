FROM node:20-alpine

COPY ./package.json package-lock.json /app/

COPY --from=production-dependencies-env /app/node_modules /app/node_modules

COPY --from=build-env /app/build /app/build

WORKDIR /app

RUN npm install -g @react-router/serve

expose 3000

CMD ["npm", "run", "start"]
