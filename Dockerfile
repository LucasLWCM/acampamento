# Usa uma imagem oficial leve do Nginx baseada no Alpine Linux
FROM nginx:alpine

# Remove o index default do nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do projeto para o diretório padrão que o Nginx usa para servir arquivos estáticos
COPY . /usr/share/nginx/html

# Copia o nginx.conf customizado para habilitar GZIP e Cache
COPY nginx.conf /etc/nginx/nginx.conf

# Expõe a porta 80, que é a porta padrão onde o Nginx roda
EXPOSE 80

# Inicia o Nginx e mantém o container rodando em primeiro plano
CMD ["nginx", "-g", "daemon off;"]
