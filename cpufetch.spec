%define _empty_manifest_terminate_build 0

Name: cpufetch
Summary: Simple yet fancy CPU architecture fetching tool
License: GPL-2.0
Group:   Monitoring
Version: 1.03
Release: 2
URL: https://github.com/Dr-Noob/cpufetch
Source0: https://github.com/Dr-Noob/cpufetch/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make

%description
cpufetch is a command-line tool written in C that displays the CPU information in a clean and beautiful way.
It currently supports x86_64 CPUs (both Intel and AMD), ARM, and PowerPC.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

# From Fedora
rm %{buildroot}%{_datadir}/licenses/cpufetch-git/LICENSE
# The man page is not actually gzipped
mv %{buildroot}%{_mandir}/man1/%{name}.1{.gz,}

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
