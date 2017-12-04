import paramiko
import os

def env_setup():
    os.system("scp -i login.pem -r my_code/ ec2-user@ec2-****.compute-1.amazonaws.com");

    k = paramiko.RSAKey.from_private_key_file("login.pem") # must be in your current directory
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    c.connect( hostname="ec2-***.compute-1.amazonaws.com", username="ec2-user", pkey=k)

    # These commands will execute in series
    commands = [
        'sudo pip install beautifulsoup4',
        'sudo pip install requests',
        'sudo pip install numpy',
        'sudo pip install bottle',
        'sudo pip install Beaker',
        'sudo pip install weather-api',
        'sudo pip install httplib2',
        'sudo pip install pymongo',
        'sudo pip install nytimesarticle',
        'sudo pip install boto',
        'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6',
        'echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list',
        'sudo apt-get update',
        'sudo apt-get install -y mongodb-org',
        'git clone https://github.com/trishamrkt/csc326-project.git',
        'cd csc326-project',
        'git fetch origin',
        'git checkout origin/AWS-Integration-Lab4',
        'sudo service mongod start',
        'mongo',
        "db.createCollection('docId_to_url')",
        "db.createCollection('inbound')",
        "db.createCollection('num_links')",
        "db.createCollection('outbound')",
        "db.createCollection('page_rank')",
        "db.createCollection('url_to_description')",
        "db.createCollection('url_to_title')",
        "db.createCollection('wordId_to_docIds')",
        "db.createCollection('wordId_to_word')",
        "db.createCollection('word_to_url')",
        'exit',
        "cd /",
        "cd csc326-project/Datafiles",
        "mongoimport --db GoogaoDB --collection docId_to_url --file docId_to_url.json",
        "mongoimport --db GoogaoDB --collection inbound --file inbound.json",
        "mongoimport --db GoogaoDB --collection num_links --file num_links.json",
        "mongoimport --db GoogaoDB --collection outbound --file outbound.json",
        "mongoimport --db GoogaoDB --collection page_rank --file page_rank.json",
        "mongoimport --db GoogaoDB --collection url_to_description --file url_to_description.json",
        "mongoimport --db GoogaoDB --collection url_to_title --file url_to_title.json",
        "mongoimport --db GoogaoDB --collection wordId_to_docIds --file wordId_to_docIds.json",
        "mongoimport --db GoogaoDB --collection wordId_to_word --file wordId_to_word.json",
        "mongoimport --db GoogaoDB --collection word_to_url --file word_to_url.json'",
        "cd ..",
        'git pull origin AWS-Integration-Lab4',
        'sudo nohup python MainApp.py &',
        'logout'
    ]

    for command in commands:
        print "Executing {}".format( command )
        stdin, stdout, stderr = c.exec_command(command) #This command is executed on remote server
        print stdout.read()
        print "Errors"
        print stderr.read()

    c.close()
