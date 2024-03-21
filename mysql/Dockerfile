# Use the official MySQL 8.0 image as a parent image
FROM mysql:8.0

# Copy the MySQL custom configuration file into the container
COPY my.cnf /etc/mysql/my.cnf

# Expose port 3306 to allow external connections
EXPOSE 3306

# Set the default command to run when the container starts
CMD ["mysqld"]
