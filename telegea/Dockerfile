#FROM alpine
#ENV LANG C.UTF-8

#RUN apk update && \
#  apk add --no-cache libstdc++ libgcc ca-certificates && \
#  rm -rf /var/cache/apk/*


#RUN mkdir /sdomotica
#COPY sdomoticatelegea /sdomotica
#RUN chmod a+x /sdomotica/sdomoticatelegea
#VOLUME /sdomotica
#EXPOSE 3501 3502
#CMD ./sdomotica/sdomoticatelegea

FROM sdomotica/telegea:first
VOLUME /sdomotica
EXPOSE 3501 3502
CMD ./sdomotica/sdomoticatelegea







