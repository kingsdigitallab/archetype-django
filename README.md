# archetype-django

2020 PLEASE NOTE - though you are welcome to use the Archetype framework for your own research, KDL will no longer be supporting or hosting new Archetype projects. We will continue to develop the ideas and tools that have made Archetype such a powerful tool for DH research through new projects and through complementary development of focussed, modular, software tools.

This is the repository for the archetype project at [https://kdl.kcl.ac.uk](King's Digital Lab)

This project is configured to use [Vagrant](https://www.vagrantup.com/) for local development and [Fabric](http://www.fabfile.org/) for deployment. 

## Getting started
1. Enter the project directory: `cd $PROJECT_KEY-django`
2. Start the virtual machine: `vagrant up`
3. SSH into the virtual machine: `vagrant ssh`
4. Run the local development server: `./manage.py runserver 0:8000`

You can then access the site locally at [http://localhost:8000](http://localhost:8000)

If the project is ldap-enabled, you can login using your LDAP credentials. Note: LDAP authentication will only work within the college firewall. Alternatively, use the default superuser login:

username: `vagrant`
password: `vagrant`

Note: This login will only work on a locally deployed virtual machine.

## Requirements
* Ansible >= 2.3
* NodeJS
* Vagrant >= 1.9
* VirtualBox >= 5.0
