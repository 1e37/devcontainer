###Integration of Devcontainer using DevPod & VSCodium @ Fedora 42 
https://containers.dev/

>DevContainers are isolated development environments that run in clean containers, avoiding conflicts with other builds or system dependencies. They are easy to reproduce and provide a stable base for CI/CD pipelines. By mounting local workspaces, they enable remote development without bloating its own system.



First, you can eather compile Devpod from its source by using the rpmbuild enviroment, or just install the precompiled .rpm file for x86_64 systems from the rpmbuild folder.

###Compile yourself: ###

- **sudo dnf install rpm-build rpmdevtools**
- **rpmdev-setuptree**
- **rpmbuild -ba devpod.spec**


After Devpod is up and running, check if the enviroment variable in ~/.bashrc exists : - **"export PATH=$PATH:/usr/sbin/devpod-cli"**

Now its time install the VSCodium extension "3timeslazy.vscodium-devpodcontainers"

After installing, you can start VSCodium from the DevContainer folder and the plugin will create a new docker/podman container. Our current local workdir will be mounted in the remote directory of the container. All dependencys and dev tools are now seperated from the host system. Atuin is installed too btw!
Enjoy! :)
