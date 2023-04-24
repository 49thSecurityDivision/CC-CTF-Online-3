FROM php:7.4-apache

# Copy the challenge files to the container
COPY . /var/www/html/

# Change the ownership of the files to the www-data user
RUN chown -R www-data:www-data /var/www/html/

# Enable Apache's rewrite module
RUN a2enmod rewrite

# Expose the HTTP port
EXPOSE 80
