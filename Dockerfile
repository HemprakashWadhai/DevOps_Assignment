# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y cowsay fortune && \
    rm -rf /var/lib/apt/lists/*

# Add Wisecow application script
COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port
EXPOSE 4499

# Command to run the application
CMD ["/usr/local/bin/wisecow.sh"]
