FROM nginx

# Configs
COPY manifesto.html  /usr/share/nginx/html/index.html
#COPY nginx.conf
RUN apt update 
RUN apt install -y openssh-server
COPY sshd_config /etc/ssh/sshd_config


# Setup mentor user
RUN useradd -s /bin/bash -m mentor
RUN echo "mentor:curiosity" | chpasswd

# Set flag
RUN echo "flag{h4ck3r_man1fest0}" > /home/mentor/flag.txt

