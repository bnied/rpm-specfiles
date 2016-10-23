Name: packer	
Version: 0.11.0
Release: 1%{?dist}
Summary: Create machine and container images for multiple platforms
Group: Development/Tools
License: MPLv2.0
URL: https://www.packer.io/

Source0: https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

%description
Packer is a tool for creating machine and container images for
multiple platforms from a single source configuration. 

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

# Rename to packerio since packer conflicts with Fedora
pushd %{buildroot}%{_bindir}
  mv packer packerio
popd

%files
%{_bindir}/*

%changelog
* Sun Oct 23 2016 Ben Nied <spacewreckage@gmail.com> - 0.11.0-1
* Thu Sep 22 2016 Ben Nied <spacewreckage@gmail.com> - 0.10.2-1
* Wed May 11 2016 Ben Nied <spacewreckage@gmail.com> - 0.10.1-1
* Fri Mar 25 2016 Ben Nied <spacewreckage@gmail.com> - 0.10.0-1
* Tue Mar 1 2016 Ben Nied <spacewreckage@gmail.com> - 0.9.0-1
* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.8.6-1
- Initial package
