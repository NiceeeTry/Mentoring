FROM ubuntu:jammy
RUN apt-get update && apt-get install -y python3 --no-install-recommends
COPY webfiles/ /usr/share/webfiles
WORKDIR /usr/share/webfiles
EXPOSE 8000
ENTRYPOINT ["python3", "-m", "http.server"]
