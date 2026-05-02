#FROM alpine
#ENV LANG C.UTF-8

#RUN apk update && \
#  apk add --no-cache libstdc++ libgcc ca-certificates && \
#  rm -rf /var/cache/apk/*


#RUN mkdir /sdomotica
#COPY inimrpi /sdomotica
#RUN chmod a+x /sdomotica/inimrpi
#VOLUME /sdomotica
#EXPOSE 3040
#CMD ./sdomotica/inimrpi


#parte release

FROM sdomotica/inim:first
#VOLUME /sdomotica
EXPOSE 3040
CMD ./sdomotica/inimrpi







