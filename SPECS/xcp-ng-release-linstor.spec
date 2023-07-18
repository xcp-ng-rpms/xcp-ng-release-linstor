Summary: LINSTOR packages from the LINSTOR XCP-ng repository
Name: xcp-ng-release-linstor
Version: 1.4
Release: 1%{?dist}
License: GPLv2
Source0: xcp-ng-linstor.repo
Source1: drbd.conf
BuildArch: noarch

%description
yum configuration for LINSTOR packages from the LINSTOR XCP-ng repository.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo
install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/modprobe.d/drbd.conf

# Note: Could eventually be moved to the DRBD RPM if we built it ourselves.
%triggerin -- lvm2
sed -i "s/\# \(global_filter\)[[:space:]]*=.*/\1 = [ \"r|^\/dev\/drbd.*|\" ]/g" %{_sysconfdir}/lvm/lvm.conf
sed -i "s/\# \(global_filter\)[[:space:]]*=.*/\1 = [ \"r|^\/dev\/drbd.*|\" ]/g" %{_sysconfdir}/lvm/master/lvm.conf

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/xcp-ng-linstor.repo
%{_prefix}/lib/modprobe.d/drbd.conf

%changelog
* Tue Jul 18 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.4-1
- Change repo URLs for XCP-ng 8.3.

* Wed Apr 05 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.3-1
- Use a new repository on repo.vates.tech.
- Add a testing repository in xcp-ng-linstor.repo.

* Mon Mar 13 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.2-1
- Add kernel module drbd.conf to prevent idle TCP connections from freezing.

* Wed Mar 08 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1-1
- Modify LVM configuration to never scan DRBD devices.

* Thu Dec 16 2021 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Initial release.
