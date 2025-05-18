###Integration of Devcontainer using DevPod & Vscodium @ Fedora 42 
https://containers.dev/

>DevContainers are isolated development environments that run in clean containers, avoiding conflicts with other builds or system dependencies. They are easy to reproduce and provide a stable base for CI/CD pipelines. By mounting local workspaces, they enable remote development without bloating its own system.



First, you can eather compile Devpod from its source by using the rpmbuild enviroment, or just install the precompiled .rpm file for x86_64 systems from the RPM folder.

###Compile yourself:
**sudo dnf install rpm-build rpmdevtools**
**rpmdev-setuptree**
**rpmbuild -ba devpod.spec**

After Devpod is up and running, check if the enviroment variable in ~/.bashrc exists : "export PATH=$PATH:/usr/sbin/devpod-cli"

Now its time install the VsCodium extension "3timeslazy.vscodium-devpodcontainers"

After Installing you can start VsCodium from the DevContainer folder and the plugin will create a new container. our current local workdir is also the remote dir. 
enjoy :)
