Summary: LINSTOR packages from the LINSTOR XCP-ng repository
Name: xcp-ng-release-linstor
Version: 1.0
Release: 1%{?dist}
License: GPLv2
Source0: xcp-ng-linstor.repo
BuildArch: noarch

%description
yum configuration for LINSTOR packages from the LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo

%changelog
* Thu Dec 16 2021 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Initial release.
