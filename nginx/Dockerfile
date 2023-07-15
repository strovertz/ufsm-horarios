# Use a imagem base do Nginx
FROM nginx

# Remova o arquivo de configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copie o arquivo de configuração personalizado para o contêiner
COPY nginx.conf /etc/nginx/conf.d/

# Copie o diretório html para o diretório raiz do servidor Nginx
COPY html /usr/share/nginx/html

# Expõe a porta 80 para permitir o acesso ao servidor Nginx
EXPOSE 80

# Inicia o servidor Nginx quando o contêiner for iniciado
CMD ["nginx", "-g", "daemon off;"]
