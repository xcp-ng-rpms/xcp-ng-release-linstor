Summary: LINSTOR packages from the LINSTOR XCP-ng repository
Name: xcp-ng-release-linstor
Version: 1.1
Release: 1%{?dist}
License: GPLv2
Source0: xcp-ng-linstor.repo
BuildArch: noarch

%description
yum configuration for LINSTOR packages from the LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo

# Note: Could eventually be moved to the DRBD RPM if we built it ourselves.
%triggerin -- lvm2
sed -i "s/\# \(global_filter\)[[:space:]]*=.*/\1 = [ \"r|^\/dev\/drbd.*|\" ]/g" %{_sysconfdir}/lvm/lvm.conf
sed -i "s/\# \(global_filter\)[[:space:]]*=.*/\1 = [ \"r|^\/dev\/drbd.*|\" ]/g" %{_sysconfdir}/lvm/master/lvm.conf

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo

%changelog
* Wed Mar 08 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-1
- Modify LVM configuration to never scan DRBD devices.

* Thu Dec 16 2021 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Initial release.
