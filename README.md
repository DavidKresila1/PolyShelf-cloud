#PolyShelf-cloud

PolyShelf-cloud is a file storage software that allows you to store and manage your files in the cloud. It is an open source project that is designed to be easy to install and use.
Installation

PolyShelf-cloud can be installed using the install.sh script provided in the repository. Here are the steps to install PolyShelf-cloud:

Clone the repository from GitHub:


    git clone https://github.com/DavidKresila1/PolyShelf-cloud.git

Navigate to the directory:


    cd PolyShelf-cloud

Run the install.sh script:

    ./install.sh

The installation script will install all the necessary dependencies and create a virtual environment for PolyShelf-cloud.
Running PolyShelf-cloud

PolyShelf-cloud can be run using the run.sh script provided in the repository. Here are the steps to run PolyShelf-cloud:

    Navigate to the directory:

bash

cd PolyShelf-cloud

    Run the run.sh script:

bash

./run.sh

The run script will start the PolyShelf-cloud server and you will be able to access it by visiting http://ip-adress:8000/ in your web browser.
Running PolyShelf-cloud with Apache

PolyShelf-cloud can also be run using Apache. Here are the steps to run PolyShelf-cloud with Apache:

    Install Apache and mod_wsgi:

bash

sudo apt-get install apache2 libapache2-mod-wsgi-py3

    Configure Apache to run PolyShelf-cloud:

bash

sudo nano /etc/apache2/sites-available/polyshelf-cloud.conf

Add the following lines to the file:

xml

<VirtualHost *:80>
    ServerName your-domain.com

    WSGIDaemonProcess polyshelf-cloud python-home=/path/to/virtualenv python-path=/path/to/project
    WSGIProcessGroup polyshelf-cloud
    WSGIScriptAlias / /path/to/project/wsgi.py process-group=polyshelf-cloud

    <Directory /path/to/project>
        Require all granted
    </Directory>
</VirtualHost>

    Enable the configuration:

bash

sudo a2ensite polyshelf-cloud.conf

    Restart Apache:

bash

sudo systemctl restart apache2

You should now be able to access PolyShelf-cloud by visiting http://your-domain.com/ in your web browser.
Running PolyShelf-cloud with Docker

PolyShelf-cloud can also be run using Docker. Here are the steps to run PolyShelf-cloud with Docker:

    Build the Docker image:

bash

docker build -t polyshelf-cloud .

    Run the Docker container:

bash

docker run -p 8000:8000 polyshelf-cloud

You should now be able to access PolyShelf-cloud by visiting http://localhost:8000/ in your web browser.
Conclusion

PolyShelf-cloud is a powerful file storage software that can be installed and run in various ways. Whether you prefer to run it with the install.sh and run.sh scripts, Apache, or Docker, PolyShelf-cloud is designed to be easy to use and maintain.
