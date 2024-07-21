# Use an official Ubuntu base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat && \
    apt-get clean

# Copy the application script
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port the application runs on
EXPOSE 4499

# Run the application
CMD ["/usr/local/bin/wisecow.sh"]
