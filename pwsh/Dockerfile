from alpine:latest

# install the requirements
RUN apk add --no-cache \
    ca-certificates \
    less \
    ncurses-terminfo-base \
    krb5-libs \
    libgcc \
    libintl \
    libssl1.1 \
    libstdc++ \
    tzdata \
    userspace-rcu \
    zlib \
    icu-libs \
    curl && apk -X https://dl-cdn.alpinelinux.org/alpine/edge/main add --no-cache \
    lttng-ust 

# Download the powershell '.tar.gz' archive
RUN curl -L https://github.com/PowerShell/PowerShell/releases/download/v7.3.4/powershell-7.3.4-linux-alpine-x64.tar.gz -o /tmp/powershell.tar.gz

# Create the target folder where powershell will be placed
RUN mkdir -p /opt/microsoft/powershell/7

# Expand powershell to the target folder
RUN tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7

# Set execute permissions
RUN chmod +x /opt/microsoft/powershell/7/pwsh &&  ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh
# Create the symbolic link that points to pwsh

ENV GROUP_NAME=MyADGroup
# Start PowerShell
COPY  check_ad2.ps1  /apps
CMD chmod 755 /apps/check_ad2.ps1 
CMD /usr/bin/pwsh  /apps/check_ad2.ps1 
