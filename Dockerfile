FROM ubuntu:lunar-20230420

RUN apt update
RUN apt install -y curl g++ zlib1g-dev

# install codon
RUN /bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
ENV PATH=$PATH:/root/.codon/bin

WORKDIR /root
COPY main.py .
RUN codon build -release -exe -o app main.py

CMD ["./app"]
