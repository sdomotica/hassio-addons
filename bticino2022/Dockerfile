#FROM alpine
#ENV LANG C.UTF-8

#RUN apk update && \
#  apk add --no-cache libstdc++ libgcc ca-certificates && \
#  rm -rf /var/cache/apk/*


#RUN mkdir /sdomotica
#COPY sdomoticarpi /sdomotica
#RUN chmod a+x /sdomotica/sdomoticarpi
#VOLUME /sdomotica
#EXPOSE 3100 3000 3300
#CMD ./sdomotica/sdomoticarpi

FROM sdomotica/sdomotica2022:test
#VOLUME /sdomotica
EXPOSE 3100 3000 3300
CMD ./sdomotica/sdomoticarpi







