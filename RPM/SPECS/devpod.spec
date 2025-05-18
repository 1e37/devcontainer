Name: devpod
Version: 1.0
Release: 1%{?dist}
Summary: DevPod Application
License: Proprietary
URL: https://example.com
Source0: DevPod_linux_x86_64.tar.gz

%description
DevPod is a development environment tool.

%prep
mkdir -p devpod-1.0
tar -xzf %{SOURCE0} -C devpod-1.0
cd devpod-1.0

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/icons/hicolor/32x32/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256@2/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/16x16/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/64x64/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps
mkdir -p %{buildroot}/usr/share/applications

# Copy binary files
cp devpod-1.0/usr/bin/dev-pod-desktop %{buildroot}/usr/bin/
cp devpod-1.0/usr/bin/devpod-cli %{buildroot}/usr/bin/

# Copy icon files
cp devpod-1.0/usr/share/icons/hicolor/32x32/apps/dev-pod-desktop.png %{buildroot}/usr/share/icons/hicolor/32x32/apps/
cp devpod-1.0/usr/share/icons/hicolor/256x256@2/apps/dev-pod-desktop.png %{buildroot}/usr/share/icons/hicolor/256x256@2/apps/
cp devpod-1.0/usr/share/icons/hicolor/128x128/apps/dev-pod-desktop.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/

# Copy desktop file
cp devpod-1.0/usr/share/applications/DevPod.desktop %{buildroot}/usr/share/applications/

%post
gtk-update-icon-cache /usr/share/icons/hicolor

%files
/usr/bin/dev-pod-desktop
/usr/bin/devpod-cli
/usr/share/icons/hicolor/32x32/apps/dev-pod-desktop.png
/usr/share/icons/hicolor/256x256@2/apps/dev-pod-desktop.png
/usr/share/icons/hicolor/128x128/apps/dev-pod-desktop.png
/usr/share/applications/DevPod.desktop

%changelog
* Wed May 14 2025 Your Name <your.email@example.com> - 1.0-1
- Initial package.
